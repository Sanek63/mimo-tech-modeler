# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# -------------------------------------------------------------------------------
import PyQt5.QtWidgets as QtWidgets  # Компоненты для приложения
import PyQt5.QtGui as QtGui  # Графический интерфейс пользователя
import PyQt5.QtCore as QtCore  # Ядро функциональности

from actions.processing import process


# -------------------------------------------------------------------------------

class Ui_MainWindow(object):

    def accept_parametrs(self):
        """
            Данная функция предназначена
            для получения данных для расчета,
            которые ввел пользователь
        """
        alg = self.comboBox.currentText()
        N = int(self.lineEdit.text()) if int(self.lineEdit.text()) > 0 else 0
        n = int(self.comboBox_2.currentText())

        Eb_N0_dB = list(i for i in range(n + 1))
        send = int(self.lineEdit_3.text()) if int(self.lineEdit_3.text()) > 0 else 0
        input = int(self.lineEdit_4.text()) if int(self.lineEdit_4.text()) > 0 else 0
        l = int(self.lineEdit_5.text()) if int(self.lineEdit_5.text()) > 0 else 0

        process(N, alg, Eb_N0_dB, send, input, l)

        return

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
        font.setPointSize(15)
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
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.algoritm.setFont(font)
        self.algoritm.setObjectName("algoritm")

        self.num_of_counts = QtWidgets.QLabel(self.centralwidget)
        self.num_of_counts.setGeometry(QtCore.QRect(20, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.num_of_counts.setFont(font)
        self.num_of_counts.setObjectName("num_of_counts")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 100, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")

        self.SNR = QtWidgets.QLabel(self.centralwidget)
        self.SNR.setGeometry(QtCore.QRect(20, 140, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
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
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.send_anten.setFont(font)
        self.send_anten.setObjectName("send_anten")

        self.input_anten = QtWidgets.QLabel(self.centralwidget)
        self.input_anten.setGeometry(QtCore.QRect(20, 220, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.input_anten.setFont(font)
        self.input_anten.setObjectName("input_anten")

        self.len_anten = QtWidgets.QLabel(self.centralwidget)
        self.len_anten.setGeometry(QtCore.QRect(20, 260, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.len_anten.setFont(font)
        self.len_anten.setObjectName("len_anten")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 180, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 220, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 260, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.processButton = QtWidgets.QPushButton(self.centralwidget)
        self.processButton.setEnabled(True)
        self.processButton.setGeometry(QtCore.QRect(20, 317, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
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
        font.setPointSize(15)
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
        font.setPointSize(15)
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