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
from numpy import convolve as conv        # Функция для свертки одномерных массивов
from numpy import real                    # Функция для возвращения действительной часть аргумента сложного типа данных
from numpy import random as rd            # Функция для случайных значений
from numpy import dot                     # Функция для перемножения матриц
from numpy import eye                     # Возвращает диагонали 1
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from input_window import Ui_OtherWindow   # Импортируем класс второго окна (Окна для ввода отношений Сигнал/Шум)
from actions.GetMatrix import GetMatrix   # Функция, которая делит вектор-сигнала на колл-во-colCount длинну фильтра. Из вектора получается матрица
from actions.GetVector import GetVector   # Функция для объединения векторов
#-------------------------------------------------------------------------------

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def create_graphics(self):
        fig = plt.Figure()
        ax = fig.add_subplot(111)
        ax.bar(1, 2, 1)

        canvas = FigureCanvas(fig)
        #canvas.draw()
        #canvas.show()

        self.widget.addWidget(canvas)

    def matrixT(self, a):
        matrix = [[0] * len(a) for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a)):
                matrix[i][j] = a[j][i]
        return matrix

    def process(self):
        zz = 1000 # длинна посылки, колличество элементов в строке
        nz = int(self.num/zz)

        # --- генерация векторо импульсной характеристики
        ht = [[0] * self.input for i in range(self.send)]
        for i in range(self.send):
            for j in range(self.input):
                ht[i][j] = []
                for k in range(self.len):
                    ht[i][j].append(round(random.uniform(-1, 1), 1))

        # --- end of генерация векторов импульсной характеристики
        # --- канальная матрица
        hM = [[] for i in range(self.len)]
        for i in range(self.len):
            for k in range(self.input):
                for j in range(self.send):
                    hM[i].append(ht[j][k][i])

        # --- end of канальная матриц
        # --- длина интервала обработки принимаемых сигналов
        dl = (zz / self.input) + self.len - 1

        # --- end of длина интервала обработки принимаемых сигналов
        # --- пустая канальная матрица
        HM = [[0] * zz for i in range(int(2 * dl))]
        num = 0
        for k in range(0, zz-2, 2):
            for i in range(self.len):
                HM[num + k][k] = hM[i]
                HM[num + k][k + 1] = hM[i]
                HM[num + 1 + k][k] = hM[i]
                HM[num + 1 + k][k + 1] = hM[i]
                num += 2
            num = 0

        # --- end of пустаня канальная матрица
        # --- пустые вектора принятого сигнала для 2-х алгоритмов
        nErrZF = [0 for i in range(len(self.osh))]
        nErrmmse = [0 for i in range(len(self.osh))]
        ip = []
        for ii in range(len(self.osh)):
            for i in range(self.num):
                rand = random.random()
                if rand > 0.5: ip.append(1)
                else: ip.append(0)
            s = []
            for i in ip:
                s.append(2 * ip[i] - 1)
            ss = GetMatrix(s, zz)

        # -- end of пустые вектора принятого сигнала для 2-х алгоритмов
        # --- MIMO - канал связи
            ssipZF = [[0] for i in range(nz)]
            ssipmmse = [[0] for i in range(nz)]
            for ff in range(nz):
                st = ss[ff][:]
        # --- end of MIMO - канал связи
        # --- делитель потока сигнала делится по колличеству nTx
                ind = []
                s = []
                for i in range(self.send):
                    ind = list(j for j in range(i, len(st), 2))
                for i in ind:
                    s.append(st[i])

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
                    num = 1 / math.sqrt(2) * rd.randn(1, int(zz / 2 + self.len - 1)) + 1j * rd.randn(1, int(zz / 2 + self.len - 1))
                    n.append(num)

        # --- end of генерация отсчетов Гауссовского шума
        # --- сигнал на входе эквалайзера, прошедший весь канал связи с БГШ
                y = []
                for i in range(self.send):
                    y.append(chanOut[i] + 10 ** (self.osh[ii] / 20) * n[i])

        # --- end of сигнал на входе эквалайзера, прошедший весь канал связи с БГШ

        # --- генерация матриц для алгоритмов
                if self.alg == "ZF":
                    HMzf = HM
                elif self.alg == "MMSE":
                    HMmmse = HM

        # --- end of генерация матриц для алгоритмов
        # --- эквалайзер для zf алгоритма
                WZF = np.array(dot(self.matrixT(HMzf), HMzf)) / np.array(self.matrixT(HMzf))

        # --- end of эквалайзер для zf алгоритма
        # --- эквалайзер для mmse алгоритма
                Wmmse = (np.array(dot(self.matrixT(HMmmse), HMmmse)) + (10 ** (-self.osh[ii] / 10) * eye(zz))) / np.array(self.matrixT(HMmmse))

        # --- end of эквалайзер для mmse алгоритма
        # --- фильтрация
                yHat = GetVector(y[0], y[1]) # объединитель потока
                ySampZF = ord(WZF, self.matrixT(yHat)) # результат работы ZF алгоритма, сигнал после "очистки " эквалайзером
                ySampmmse = ord(Wmmse, self.matrixT(yHat)) # результат работы MMSE алгоритма, сигнал после "очистки " эквалайзером

        # --- end of фильтрация
        # --- декодирование
                ipHatZFst = real(self.matrixT(ySampZF)) > 0
                ipHatmmsest = real(self.matrixT(ySampmmse)) > 0

        # --- end of декодирование
        # --- объединение посылок
                ssipZF[ff] = ipHatZFst
                ssipmmse[ff] = ipHatmmsest
        # --- end of объединение посылок
        # --- подсчет ошибки
            ipHatZF = np.reshape(self.matrixT(ssipZF), 1, self.num)
            ipHatmmse = np.reshape(self.matrixT(ssipmmse), 1, self.num)

        # --- end of подсчет ошибки
        # --- подсчет абсолютной ошибки
            nErrZF[ii] = np.size(np.argwhere(ip - ipHatZF), 2)
            nErrmmse[ii] = np.size(np.argwhere(ip - ipHatmmse), 2)

        # --- end of подсчет абсолютной ошибки
        # --- подсчет побитовой ошибки
        simBerZF = [i / self.num for i in nErrZF]
        simBermmse = [i / self.num for i in nErrmmse]

        # --- end of подсчет побитовой ошибки
    def accept_parametrs(self):
        self.alg = self.comboBox.currentText()

        if len(self.lineEdit.text()) > 0:
            self.num = int(self.lineEdit.text())
        else:
            self.lineEdit.setText("0")
            self.num = 0

        try:
            self.osh = self.ui.rez
            for i, elem in enumerate(self.osh):
                self.osh[i] = int(elem)
        except: self.osh = []

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
        MainWindow.resize(1021, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 10, 441, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(470, 10, 541, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")

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

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(479, 59, 521, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.widget = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.widget.setContentsMargins(0, 0, 0, 0)
        self.widget.setObjectName("widget")

        self.processButton = QtWidgets.QPushButton(self.centralwidget)
        self.processButton.setEnabled(True)
        self.processButton.setGeometry(QtCore.QRect(20, 317, 401, 41))
        self.processButton.clicked.connect(self.accept_parametrs)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.processButton.setFont(font)
        self.processButton.setObjectName("processButton")
        self.enterToNewWindow = QtWidgets.QPushButton(self.centralwidget)
        self.enterToNewWindow.setGeometry(QtCore.QRect(260, 140, 93, 31))
        self.enterToNewWindow.setObjectName("enterToNewWindow")

        self.enterToNewWindow.clicked.connect(self.openWindow)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.enterToNewWindow.setFont(font)
        self.enterToNewWindow.setObjectName("enterToNewWindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное окно"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Входные данные</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Построение графиков</span></p></body></html>"))
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
        self.enterToNewWindow.setText(_translate("MainWindow", "Перейти..."))
