# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#-------------------------------------------------------------------------------
import PyQt5.QtWidgets as QtWidgets       # Компоненты для приложения
import PyQt5.QtGui as QtGui               # Графический интерфейс пользователя
import PyQt5.QtCore as QtCore             # Ядро функциональности

import math                               # Бибилотека математических функций
import random                             # Для генерации случайных чисел
import numpy as np                        # Библиотека математики
from numpy import eye                     # Возвращает диагонали 1
from numpy import convolve as conv        # Функция для свертки одномерных массивов
from numpy import real                    # Функция для возвращения действительной часть аргумента сложного типа данных
from numpy import random as rd            # Функция для случайных значений
from numpy import dot                     # Функция для перемножения матриц
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from scipy.signal import convolve

from actions.GetMatrix import GetMatrix   # Функция, которая делит вектор-сигнала на колл-во-colCount длинну фильтра. Из вектора получается матрица
from actions.GetVector import GetVector   # Функция для объединения векторов
#-------------------------------------------------------------------------------



class Ui_MainWindow(object):

    def indices(self, a, func):
        return [i for (i, val) in enumerate(a) if func(val)]

    def create_graphics(self, simBer, color):

        fig, ax = plt.subplots(figsize=(5, 3), dpi= 150)
        ax.set_title('BER системы MIMO 2х2 в канале с МСИ, L=3')
        ax.legend(loc='upper left')
        ax.set_ylabel('Битовый коэффициент ошибок')
        ax.set_xlim(0, xmax= self.osh[-1])
        fig.tight_layout()
        plt.plot(self.osh, simBer, color = "{}".format(color), lw = 2, ls= "--", marker= "*")
        ax.set_ylim(0.3, ymax = 1)
        plt.yscale("log")
        plt.grid(True)
        canvas = FigureCanvas(fig)
        canvas.draw()
        canvas.show()

    def process(self):
        zz = 1000 # длинна посылки, колличество элементов в строке
        nz = int(self.num/zz)

        # --- генерация векторо импульсной характеристики
        ht = [[0] * self.input for i in range(self.send)]
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
        hM = [[] for i in range(self.len)]
        for i in range(self.len):
            for k in range(self.input):
                hM[i].append([])
                for j in range(self.send):
                    hM[i][k].append(ht[j][k][i])

        # --- end of канальная матриц
        # --- пустые вектора принятого сигнала для 2-х алгоритмов
        nErrZF = [0 for i in range(len(self.osh))]
        nErrmmse = [0 for i in range(len(self.osh))]
        for ii in range(len(self.osh)):
            ip = []
            for i in range(self.num):
                rand = random.random()
                if rand > 0.5: ip.append(1)
                else: ip.append(0)
            s = []
            for i in ip:
                s.append(2 * i - 1)
            ss = GetMatrix(s, zz)

        # -- end of пустые вектора принятого сигнала для 2-х алгоритмов
        # --- MIMO - канал связи
            ssipZF = [[0] * zz for i in range(nz)]
            ssipmmse = [[0] * zz for i in range(nz)]
            for ff in range(nz):
                st = ss[ff][:]

        # --- end of MIMO - канал связи
        # --- делитель потока сигнала делится по колличеству nTx
                ind = []
                s = []
                for i in range(self.send):
                    ind.append([])
                    ind[i] = list(j for j in range(i, len(st), 2))
                for i in range(self.send):
                    s.append([])
                    for j in ind[i]:
                        s[i].append(st[j])

        # --- end of делитель потока сигнала делиться по колличеству nTx
        # --- сигнал прошедший через канал
                chanOut = []
                for i in range(self.input):
                    chanOut.append([0])
                    for j in range(self.send):
                        chanOut[i] += conv(s[j], ht[j][i])

        # --- end of сигнал прошедшик через канал
        # --- генерация отсчетов Гауссовского шума
                n = []
                for i in range(self.send):
                    no = int(zz / 2 + self.len - 1)
                    num = 1 / math.sqrt(2) * (rd.randn(1, no) + 1j * rd.randn(1, no))
                    n.append(num)

        # --- end of генерация отсчетов Гауссовского шума
        # --- сигнал на входе эквалайзера, прошедший весь канал связи с БГШ
                y = []
                for i in range(self.send):
                    y.append(chanOut[i] + 10 ** (-self.osh[ii] / 20) * n[i])

        # --- end of сигнал на входе эквалайзера, прошедший весь канал связи с БГШ
        # --- фильтрация
                dl = len(y[0][0])
                HM = [[0] * zz for i in range(dl*2)]

                for k in range(0, zz - 2, 2):
                    num = 0
                    for i in range(self.len):
                        HM[num + k][k] = hM[i][0][0]
                        HM[num + k][k + 1] = hM[i][0][1]
                        HM[num + 1 + k][k] = hM[i][1][0]
                        HM[num + 1 + k][k + 1] = hM[i][1][1]
                        num += 2
                yHat = np.array(GetVector(y[0][0], y[1][0]))  # объединитель потока

        # --- end of фильтрация
        # --- генерация матриц для алгоритмов
                if self.alg == "ZF":
                    HMzf = np.array(HM)
                    WZF = np.linalg.pinv(HMzf)
                    ySampZF = dot(WZF, yHat.transpose())
                    ipHatZFst = real(ySampZF.transpose()) > 0
                    ssipZF[ff][:] = ipHatZFst

                elif self.alg == "MMSE":
                    HMmmse = np.array(HM)
                    Wmmse = dot(np.linalg.inv(dot(HMmmse.transpose(), HMmmse) + (10 ** (-self.osh[ii] / 10) * eye(zz))), HMmmse.transpose())
                    ySampmmse = dot(Wmmse, yHat.transpose())
                    ipHatmmsest = real(ySampmmse.transpose()) > 0
                    ssipmmse[ff][:] = ipHatmmsest


            if self.alg == "ZF":
                ipHatZF = np.reshape(np.array(ssipZF).transpose(), self.num)
                inds = self.indices(ip - ipHatZF, lambda x: x != 0)
                nErrZF[ii] = np.size(inds)
            elif self.alg == "MMSE":
                ipHatmmse = np.reshape(np.array(ssipmmse).transpose(), self.num)
                inds = self.indices(ip - ipHatmmse, lambda x: x != 0)
                nErrmmse[ii] = np.size(inds)

        if self.alg == "ZF":
            simBerZF = [i / self.num for i in nErrZF]
            self.create_graphics(simBerZF, "blue")
        else:
            simBermmse = [i / self.num for i in nErrmmse]
            self.create_graphics(simBermmse, "red")

        # --- end of подсчет побитовой ошибки
    def accept_parametrs(self):
        self.alg = self.comboBox.currentText()
        if len(self.lineEdit.text()) > 0:
            self.num = int(self.lineEdit.text())
        else:
            self.lineEdit.setText("0")
            self.num = 0

        n = int(self.comboBox_2.currentText())
        self.osh = []
        for i in range(n + 1):
            self.osh.append(i)

        if len(self.lineEdit_3.text()) > 0:
            self.send = int(self.lineEdit_3.text())
        else:
            self.lineEdit_3.setText("0")
            self.send = 0

        if len(self.lineEdit_4.text()) > 0:
            self.input = int(self.lineEdit_4.text())
        else:
            self.lineEdit_4.setText("0")
            self.input = 0

        if len(self.lineEdit_5.text()) > 0:
            self.len = int(self.lineEdit_5.text())
        else:
            self.lineEdit_5.setText("0")
            self.len = 0
        self.process()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 10, 441, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.algoritm = QtWidgets.QLabel(self.centralwidget)
        self.algoritm.setGeometry(QtCore.QRect(20, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.algoritm.setFont(font)
        self.algoritm.setObjectName("algoritm")



        self.num_of_counts = QtWidgets.QLabel(self.centralwidget)
        self.num_of_counts.setGeometry(QtCore.QRect(20, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.num_of_counts.setFont(font)
        self.num_of_counts.setObjectName("num_of_counts")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 100, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.SNR = QtWidgets.QLabel(self.centralwidget)
        self.SNR.setGeometry(QtCore.QRect(20, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SNR.setFont(font)
        self.SNR.setAcceptDrops(False)
        self.SNR.setAutoFillBackground(False)
        self.SNR.setLineWidth(1)
        self.SNR.setTextFormat(QtCore.Qt.AutoText)
        self.SNR.setScaledContents(False)
        self.SNR.setWordWrap(True)
        self.SNR.setObjectName("SNR")
        self.send_anten = QtWidgets.QLabel(self.centralwidget)
        self.send_anten.setGeometry(QtCore.QRect(20, 180, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.send_anten.setFont(font)
        self.send_anten.setObjectName("send_anten")
        self.input_anten = QtWidgets.QLabel(self.centralwidget)
        self.input_anten.setGeometry(QtCore.QRect(20, 220, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_anten.setFont(font)
        self.input_anten.setObjectName("input_anten")
        self.len_anten = QtWidgets.QLabel(self.centralwidget)
        self.len_anten.setGeometry(QtCore.QRect(20, 260, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.len_anten.setFont(font)
        self.len_anten.setObjectName("len_anten")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 180, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 220, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 260, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.processButton = QtWidgets.QPushButton(self.centralwidget)
        self.processButton.setEnabled(True)
        self.processButton.setGeometry(QtCore.QRect(20, 317, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.processButton.setFont(font)
        self.processButton.setObjectName("processButton")
        self.processButton.clicked.connect(self.accept_parametrs)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.SNR_2 = QtWidgets.QLabel(self.centralwidget)
        self.SNR_2.setGeometry(QtCore.QRect(260, 140, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SNR_2.setFont(font)
        self.SNR_2.setAcceptDrops(False)
        self.SNR_2.setAutoFillBackground(False)
        self.SNR_2.setLineWidth(1)
        self.SNR_2.setTextFormat(QtCore.Qt.AutoText)
        self.SNR_2.setScaledContents(False)
        self.SNR_2.setWordWrap(True)
        self.SNR_2.setObjectName("SNR_2")
        self.SNR_3 = QtWidgets.QLabel(self.centralwidget)
        self.SNR_3.setGeometry(QtCore.QRect(280, 140, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SNR_3.setFont(font)
        self.SNR_3.setAcceptDrops(False)
        self.SNR_3.setAutoFillBackground(False)
        self.SNR_3.setLineWidth(1)
        self.SNR_3.setTextFormat(QtCore.Qt.AutoText)
        self.SNR_3.setScaledContents(False)
        self.SNR_3.setWordWrap(True)
        self.SNR_3.setObjectName("SNR_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Входные данные</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ZF"))
        self.comboBox.setItemText(1, _translate("MainWindow", "MMSE"))
        self.algoritm.setText(_translate("MainWindow", "Алгоритм ="))
        self.num_of_counts.setText(_translate("MainWindow", "Число отсчетов ="))
        self.lineEdit.setText(_translate("MainWindow", "1000"))
        self.SNR.setText(_translate("MainWindow", "Сигнал/шум (ОСШ) = "))
        self.send_anten.setText(_translate("MainWindow", "Передавающие антенны ="))
        self.input_anten.setText(_translate("MainWindow", "Принимающие антенны ="))
        self.len_anten.setText(_translate("MainWindow", "Длина антенн ="))
        self.lineEdit_3.setText(_translate("MainWindow", "2"))
        self.lineEdit_4.setText(_translate("MainWindow", "2"))
        self.lineEdit_5.setText(_translate("MainWindow", "3"))
        self.processButton.setText(_translate("MainWindow", "РАССЧИТАТЬ"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "15"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "20"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "25"))
        self.SNR_2.setText(_translate("MainWindow", "0"))
        self.SNR_3.setText(_translate("MainWindow", ":"))
