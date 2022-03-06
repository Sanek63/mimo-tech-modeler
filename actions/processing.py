# -------------------------------------------------------------------------------
import numpy  # Математическая библиотеки
import random  # Библиотека для генерации случайных чисел
import math  # Библиотека для математических функций

from actions.getVector import GetVector  # Функция для объединения векторов
from actions.create_graphics import create_graphics  # Функция для создания графика (Matplotlib)


# -------------------------------------------------------------------------------

def process(N, alg, Eb_N0_dB, send, input, l):
    '''
    for i in range(self.send):
        for j in range(self.input):
            ht[i][j] = []
            for k in range(self.len):
                ht[i][j].append(round(random.uniform(-1, 1), 1))
    '''
    ht11 = [-0.9, 0.7, -0.1]
    ht12 = [-0.3, 0.5, -0.4]
    ht21 = [0.6, -0.3, 0.2]
    ht22 = [0.8, -0.6, 0.3]

    L = len(ht11)
    zz = 1000

    nz = N / zz

    HM1 = [[ht11[0], ht21[0]], [ht12[0], ht22[0]]]
    HM2 = [[ht11[1], ht21[1]], [ht12[1], ht22[1]]]
    HM3 = [[ht11[2], ht21[2]], [ht12[2], ht22[2]]]

    nErrZF = []
    nErrmmse = []

    dl = int(zz / 2 + L - 1)
    HM = numpy.empty(shape=[dl * 2, zz])
    HM.fill(0)

    for k in range(0, zz - 2, 2):
        numpy.put(HM[0 + k], (0 + k, 1 + k), HM1[0])
        numpy.put(HM[1 + k], (0 + k, 1 + k), HM1[1])
        numpy.put(HM[2 + k], (0 + k, 1 + k), HM2[0])
        numpy.put(HM[3 + k], (0 + k, 1 + k), HM2[1])
        numpy.put(HM[4 + k], (0 + k, 1 + k), HM3[0])
        numpy.put(HM[5 + k], (0 + k, 1 + k), HM3[1])

    HMzf = HM
    HMmmse = numpy.matrix(HM)
    THMmmse = HMmmse.getH()
    WZF = numpy.linalg.pinv(HMzf)

    im = numpy.identity(zz)

    ind1 = []
    ind2 = []
    for i in range(0, zz, 2): ind1.append(i)
    for i in range(1, zz, 2): ind2.append(i)

    for ii in range(0, len(Eb_N0_dB)):
        ip = [random.randint(0, 1) for i in range(N)]
        s = []
        for i in range(N): s.append((ip[i] * 2) - 1)

        ss = numpy.reshape(s, (int(N / zz), -1))
        ssipZF = []
        ssipmmse = []

        for ff in range(0, int(nz)):
            st = ss[ff]

            s1 = []
            for i in ind1: s1.append(st[i])

            s2 = []
            for i in ind2: s2.append(st[i])

            chanOut1 = numpy.convolve(s1, ht11) + numpy.convolve(s2, ht21)
            chanOut2 = numpy.convolve(s1, ht12) + numpy.convolve(s2, ht22)

            d = int(zz / 2 + L - 1)
            n1 = 1 / math.sqrt(2) * (numpy.random.normal(0, 1, d) + 1j * numpy.random.normal(0, 1, d))
            n2 = 1 / math.sqrt(2) * (numpy.random.normal(0, 1, d) + 1j * numpy.random.normal(0, 1, d))

            y1 = []
            y2 = []
            pw20 = math.pow(10, (-1 * Eb_N0_dB[ii] / 20))
            pw10 = math.pow(10, (-1 * Eb_N0_dB[ii] / 10))

            for i in range(0, d): y1.append(chanOut1[i] + pw20 * n1[i])
            for i in range(0, d): y2.append(chanOut2[i] + pw20 * n2[i])

            yHat = GetVector(y1, y2)
            ySampZF = WZF * yHat.getH()

            A = (THMmmse * HMmmse) + pw10 * im
            Wmmse = numpy.linalg.solve(A, THMmmse)
            ySampmmse = Wmmse * yHat.getH()

            ipHatZFst = ySampZF.getH().real.A1
            ipHatmmsest = ySampmmse.getH().real.A1

            for i in range(0, len(ipHatZFst)):
                if ipHatZFst[i] > 0:
                    ipHatZFst[i] = int(1)
                else:
                    ipHatZFst[i] = 0

            for i in range(0, len(ipHatmmsest)):
                if ipHatmmsest[i] > 0:
                    ipHatmmsest[i] = int(1)
                else:
                    ipHatmmsest[i] = 0

            ssipZF.append(ipHatZFst)
            ssipmmse.append(ipHatmmsest)

        ipHatZF = numpy.matrix(ssipZF).getH().reshape(1, N, order='F')
        ipHatmmse = numpy.matrix(ssipmmse).getH().reshape(1, N, order='F')
        nErrZF.append(len(numpy.nonzero(numpy.array(ip - ipHatZF))[0]))
        nErrmmse.append(len(numpy.nonzero(numpy.array(ip - ipHatmmse))[0]))

    simBerZF = numpy.array(nErrZF) / N
    simBermmse = numpy.array(nErrmmse) / N

    if alg == "ZF":
        create_graphics(Eb_N0_dB, alg, simBerZF, "blue")
    else:
        create_graphics(Eb_N0_dB, alg, simBermmse, "red")
