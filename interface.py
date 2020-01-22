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

import numpy                              # Математическая библиотеки
import random                             # Библиотека для генерации случайных чисел
import math                               # Библиотека для математических функций
import matplotlib.pyplot as plt           # Библиотека для графического отображения объектов

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from GetVector import GetVector           # Функция для объединения векторов
#-------------------------------------------------------------------------------



class Ui_MainWindow(object):

    def create_graphics(self, simBer, color):
        fig, ax = plt.subplots()
        ax.set(xlabel='ОСШ', ylabel='Битовый коэффициент ошибок', title='BER системы MIMO 2х2 в канале с МСИ, L=3')
        ax.set_xlim(0, xmax= self.Eb_N0_dB[-1])
        plt.plot(self.Eb_N0_dB, simBer, label = self.alg, color ="{}".format(color), lw = 2, ls="--", marker="*")
        ax.set_ylim(10**-3, ymax = 1.5)
        plt.yscale("log")
        plt.grid(True)
        lgnd = ax.legend(loc = "upper left",)
        lgnd.get_frame().set_facecolor('#ffb19a')
        canvas = FigureCanvas(fig)
        canvas.draw()
        canvas.show()

    def process(self):
        N = self.N
        alg = self.alg
        Eb_N0_dB = self.Eb_N0_dB
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

            ss = numpy.reshape(s, (int(self.N / zz), -1))
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
            self.create_graphics(simBerZF, "blue")
        else:
            self.create_graphics(simBermmse, "red")

    def accept_parametrs(self):
        self.alg = self.comboBox.currentText()
        if len(self.lineEdit.text()) > 0:
            self.N = int(self.lineEdit.text())
        else:
            self.lineEdit.setText("0")
            self.N = 0

        n = int(self.comboBox_2.currentText())
        self.Eb_N0_dB = []
        for i in range(n + 1):
            self.Eb_N0_dB.append(i)

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
        MainWindow.resize(441, 388)
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
        self.SNR.setGeometry(QtCore.QRect(20, 140, 281, 31))
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
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 180, 113, 31))
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
        self.processButton.setGeometry(QtCore.QRect(20, 317, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.processButton.setFont(font)
        self.processButton.setObjectName("processButton")
        self.processButton.clicked.connect(self.accept_parametrs)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(470, 60, 541, 301))
        self.widget.setObjectName("widget")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(340, 140, 51, 31))
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
        self.SNR_2.setGeometry(QtCore.QRect(310, 140, 31, 31))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ZF"))
        self.comboBox.setItemText(1, _translate("MainWindow", "MMSE"))
        self.algoritm.setText(_translate("MainWindow", "Алгоритм ="))
        self.num_of_counts.setText(_translate("MainWindow", "Число отсчетов ="))
        self.lineEdit.setText(_translate("MainWindow", "1000"))
        self.SNR.setText(_translate("MainWindow", "Отношение сигнал/шум ="))
        self.send_anten.setText(_translate("MainWindow", "Передающие антенны ="))
        self.input_anten.setText(_translate("MainWindow", "Принимающие антенны ="))
        self.len_anten.setText(_translate("MainWindow", "Длина памяти ="))
        self.lineEdit_3.setText(_translate("MainWindow", "2"))
        self.lineEdit_4.setText(_translate("MainWindow", "2"))
        self.lineEdit_5.setText(_translate("MainWindow", "3"))
        self.processButton.setText(_translate("MainWindow", "РАССЧИТАТЬ"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "15"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "20"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "25"))
        self.SNR_2.setText(_translate("MainWindow", "0 :"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
            "><span style=\" font-size:14pt; font-weight:600;\">Входные данные</span></p></body></html>")
        )