import numpy as np                        # Библиотека математики
from numpy import convolve as conv        # Функция для свертки одномерных массивов
from numpy import random as rd            # Функция для случайных значений
from numpy import dot                     # Функция для перемножения матриц
from numpy import zeros
from actions.GetMatrix import GetMatrix   # Функция, которая делит вектор-сигнала на колл-во-colCount длинну фильтра. Из вектора получается матрица
from GetVector import GetVector   # Функция для объединения векторов
import matplotlib.pyplot as plt           # Функция для работы с двумерными фигурами
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def create_graphics(simBer, color):
    fig, ax = plt.subplots(figsize=(5, 3), dpi=150)
    ax.set_title('BER системы MIMO 2х2 в канале с МСИ, L=3')
    ax.legend(loc='upper left')
    ax.set_ylabel('Битовый коэффициент ошибок')
    ax.set_xlim(0, xmax=osh[-1])
    fig.tight_layout()
    plt.plot(osh, simBer, color="{}".format(color), lw=2, ls="--", marker="*")
    # ax.set_ylim(0.3, ymax = 1)
    plt.yscale("log")
    plt.grid(True)
    canvas = FigureCanvas(fig)
    canvas.draw()
    canvas.show()



zz = 1000
N = 2000
nz = int(N/zz)
inp = 2
send = 2
len = 3
osh =  np.arange(1, 15, dtype = float)
alg = "ZF"
# --- генерация векторо импульсной характеристики
ht = [[0] * inp for i in range(send)]
'''
for i in range(self.send):
    for j in range(self.input):
        ht[i][j] = []
        for k in range(self.len):
            ht[i][j].append(round(random.uniform(-1, 1), 1))
'''
ht[0][0] = [-0.9, 0.7, -0.1]
ht[0][1] = [-0.3, 0.5, -0.4]
ht[1][0] = [0.6, -0.3, 0.2]
ht[1][1] = [0.8, -0.6, 0.3]

# --- end of генерация векторов импульсной характеристики
# --- канальная матрица

hM = [[] for i in range(len)]
for i in range(len):
    for k in range(inp):
        hM[i].append([])
        for j in range(send):
            hM[i][k].append(ht[j][k][i])

# --- end of канальная матриц
# --- пустые вектора принятого сигнала для 2-х алгоритмов
nErrZF = zeros(osh.size, float)
nErrmmse = zeros(osh.size, float)

for ii in range(osh.size):
    ip = rd.standard_normal((N,)) > 0.5
    s = 2 * ip - 1
    ss = GetMatrix(s, zz)

# -- end of пустые вектора принятого сигнала для 2-х алгоритмов
# --- MIMO - канал связи
    ssipZF = zeros((nz, zz), float)
    ssipmmse = zeros((nz, zz), float)

    for ff in range(nz):
        st = ss[ff][:]
# --- end of MIMO - канал связи
# --- делитель потока сигнала делится по колличеству nTx
        ind1 = np.arange(0, st.__len__(), 2)
        ind2 = np.arange(1, st.__len__(), 2)

        s1 =  np.array([st[i] for i in ind1])
        s2 =  np.array([st[i] for i in ind2])
        # --- end of делитель потока сигнала делиться по колличеству nTx
        # --- сигнал прошедший через канал
        chanOut1 = conv(s1, ht[0][0]) + conv(s2, ht[1][0])
        chanOut2 = conv(s1, ht[0][1]) + conv(s2, ht[1][1])

        # --- end of сигнал прошедшик через канал
        # --- генерация отсчетов Гауссовского шума
        n1 = 1 / np.sqrt(2) * (rd.standard_normal((int(zz / 2 + len - 1),)) + 1j * rd.standard_normal((int(zz / 2 + len - 1),)))
        n2 = 1 / np.sqrt(2) * (rd.standard_normal((int(zz / 2 + len - 1),)) + 1j * rd.standard_normal((int(zz / 2 + len - 1),)))

        # --- end of генерация отсчетов Гауссовского шума
        # --- сигнал на входе эквалайзера, прошедший весь канал связи с БГШ
        y1 = chanOut1 + np.power(10, -osh[ii]/20) * n1
        y2 = chanOut2 + np.power(10, -osh[ii] / 20) * n2

        # --- end of сигнал на входе эквалайзера, прошедший весь канал связи с БГШ
        # --- фильтрация
        dl = np.size(y1)
        HM = zeros((2 * dl, zz),float)

        for k in range(0, zz - 1, 2):
            num = 0
            for i in range(len):
                HM[num + k][k] = hM[i][0][0]
                HM[num + k][k + 1] = hM[i][0][1]
                HM[num + 1 + k][k] = hM[i][1][0]
                HM[num + 1 + k][k + 1] = hM[i][1][1]
                num += 2
        yHat = GetVector(y1, y2)  # объединитель потока

        # --- end of фильтрация
        # --- генерация матриц для алгоритмов
        if alg == "ZF":
            HMzf = HM
            WZF = np.linalg.pinv(HMzf)
            ySampZF = dot(WZF, yHat.transpose())
            ipHatZFst = ySampZF.transpose().real > 0
            ssipZF[ff][:] = ipHatZFst

        elif alg == "MMSE":
            HMmmse = HM
            Wmmse = np.linalg.solve((dot(HMmmse.transpose(), HMmmse) + (10 ** (-osh[ii] / 10) * np.identity(zz))), HMmmse.transpose())
            ySampmmse = dot(Wmmse, yHat.transpose())
            ipHatmmsest = ySampmmse.transpose().real > 0
            ssipmmse[ff][:] = ipHatmmsest


    if alg == "ZF":
        ipHatZF = np.reshape(ssipZF.transpose(), N)
        minus = np.subtract(ip, ipHatZF)
        find = minus.ravel().nonzero()
        nErrZF[ii] = np.size(find, axis=1)
    elif alg == "MMSE":
        ipHatmmse = np.reshape(ssipmmse.transpose(), N)


if alg == "ZF":
    simBerZF = [i / N for i in nErrZF]
    print(simBerZF)
else:
    simBermmse = [i / N for i in nErrmmse]