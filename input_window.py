# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OtherWindow(object):
    def gen(self):
        self.numofinputs = int(self.comboBox_2.currentText())
        for i in range(30):
            self.inputs[i].setVisible(False)
        for i in range(self.numofinputs):
            self.inputs[i].setVisible(True)

    def cleaning(self):
        for i in range(30):
            self.inputs[i].setText("")

    def closewindow(self):
        self.rez = []
        for i in range(self.numofinputs):
            self.rez.append(self.inputs[i].text())



    def setupUi(self, OtherWindow):
        self.inputs = []
        self.numofinputs = 0
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(456, 316)
        OtherWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 10, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.gen)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(10, 260, 93, 28))
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.cleaning)

        self.agree = QtWidgets.QPushButton(self.centralwidget)
        self.agree.setGeometry(QtCore.QRect(340, 260, 93, 28))
        self.agree.setObjectName("agree")
        self.agree.clicked.connect(self.closewindow)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setVisible(False)
        self.lineEdit_1.setGeometry(QtCore.QRect(19, 60, 64, 24))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.inputs.append(self.lineEdit_1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setVisible(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 64, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.inputs.append(self.lineEdit_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setVisible(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(161, 60, 64, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.inputs.append(self.lineEdit_3)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setVisible(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(232, 60, 64, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.inputs.append(self.lineEdit_4)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setVisible(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(303, 60, 64, 24))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.inputs.append(self.lineEdit_5)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setVisible(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(374, 60, 64, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.inputs.append(self.lineEdit_6)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setVisible(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(19, 97, 64, 24))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.inputs.append(self.lineEdit_7)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setVisible(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 97, 64, 24))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.inputs.append(self.lineEdit_8)

        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setVisible(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(161, 97, 64, 24))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.inputs.append(self.lineEdit_9)

        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setVisible(False)
        self.lineEdit_10.setGeometry(QtCore.QRect(232, 97, 64, 24))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.inputs.append(self.lineEdit_10)

        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setVisible(False)
        self.lineEdit_11.setGeometry(QtCore.QRect(303, 97, 64, 24))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.inputs.append(self.lineEdit_11)

        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setVisible(False)
        self.lineEdit_12.setGeometry(QtCore.QRect(374, 97, 64, 24))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.inputs.append(self.lineEdit_12)

        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setVisible(False)
        self.lineEdit_13.setGeometry(QtCore.QRect(19, 134, 64, 24))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.inputs.append(self.lineEdit_13)

        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setVisible(False)
        self.lineEdit_14.setGeometry(QtCore.QRect(90, 134, 64, 24))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.inputs.append(self.lineEdit_14)

        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setVisible(False)
        self.lineEdit_15.setGeometry(QtCore.QRect(161, 134, 64, 24))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.inputs.append(self.lineEdit_15)

        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setVisible(False)
        self.lineEdit_16.setGeometry(QtCore.QRect(232, 134, 64, 24))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.inputs.append(self.lineEdit_16)

        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setVisible(False)
        self.lineEdit_17.setGeometry(QtCore.QRect(303, 134, 64, 24))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.inputs.append(self.lineEdit_17)

        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setVisible(False)
        self.lineEdit_18.setGeometry(QtCore.QRect(374, 134, 64, 24))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.inputs.append(self.lineEdit_18)

        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setVisible(False)
        self.lineEdit_19.setGeometry(QtCore.QRect(19, 171, 64, 24))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.inputs.append(self.lineEdit_19)

        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setVisible(False)
        self.lineEdit_20.setGeometry(QtCore.QRect(90, 171, 64, 24))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.inputs.append(self.lineEdit_20)

        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setVisible(False)
        self.lineEdit_21.setGeometry(QtCore.QRect(161, 171, 64, 24))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.inputs.append(self.lineEdit_21)

        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setVisible(False)
        self.lineEdit_22.setGeometry(QtCore.QRect(232, 171, 64, 24))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.inputs.append(self.lineEdit_22)

        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setVisible(False)
        self.lineEdit_23.setGeometry(QtCore.QRect(303, 171, 64, 24))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.inputs.append(self.lineEdit_23)

        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setVisible(False)
        self.lineEdit_24.setGeometry(QtCore.QRect(374, 171, 64, 24))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.inputs.append(self.lineEdit_24)

        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setVisible(False)
        self.lineEdit_25.setGeometry(QtCore.QRect(19, 208, 64, 24))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.inputs.append(self.lineEdit_25)

        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_26.setVisible(False)
        self.lineEdit_26.setGeometry(QtCore.QRect(90, 208, 64, 24))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.inputs.append(self.lineEdit_26)

        self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_27.setVisible(False)
        self.lineEdit_27.setGeometry(QtCore.QRect(161, 208, 64, 24))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.inputs.append(self.lineEdit_27)

        self.lineEdit_28 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_28.setVisible(False)
        self.lineEdit_28.setGeometry(QtCore.QRect(232, 208, 64, 24))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.inputs.append(self.lineEdit_28)

        self.lineEdit_29 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_29.setVisible(False)
        self.lineEdit_29.setGeometry(QtCore.QRect(303, 208, 64, 24))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.inputs.append(self.lineEdit_29)


        self.lineEdit_30 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_30.setVisible(False)
        self.lineEdit_30.setGeometry(QtCore.QRect(374, 208, 64, 24))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.inputs.append(self.lineEdit_30)



        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Окно для ввода"))
        self.pushButton.setText(_translate("OtherWindow", "Сгенерировать"))
        self.comboBox_2.setItemText(0, _translate("OtherWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("OtherWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("OtherWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("OtherWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("OtherWindow", "5"))
        self.comboBox_2.setItemText(5, _translate("OtherWindow", "6"))
        self.comboBox_2.setItemText(6, _translate("OtherWindow", "7"))
        self.comboBox_2.setItemText(7, _translate("OtherWindow", "8"))
        self.comboBox_2.setItemText(8, _translate("OtherWindow", "9"))
        self.comboBox_2.setItemText(9, _translate("OtherWindow", "10"))
        self.comboBox_2.setItemText(10, _translate("OtherWindow", "11"))
        self.comboBox_2.setItemText(11, _translate("OtherWindow", "12"))
        self.comboBox_2.setItemText(12, _translate("OtherWindow", "13"))
        self.comboBox_2.setItemText(13, _translate("OtherWindow", "14"))
        self.comboBox_2.setItemText(14, _translate("OtherWindow", "15"))
        self.comboBox_2.setItemText(15, _translate("OtherWindow", "16"))
        self.comboBox_2.setItemText(16, _translate("OtherWindow", "17"))
        self.comboBox_2.setItemText(17, _translate("OtherWindow", "18"))
        self.comboBox_2.setItemText(18, _translate("OtherWindow", "19"))
        self.comboBox_2.setItemText(19, _translate("OtherWindow", "20"))
        self.comboBox_2.setItemText(20, _translate("OtherWindow", "21"))
        self.comboBox_2.setItemText(21, _translate("OtherWindow", "22"))
        self.comboBox_2.setItemText(22, _translate("OtherWindow", "23"))
        self.comboBox_2.setItemText(23, _translate("OtherWindow", "24"))
        self.comboBox_2.setItemText(24, _translate("OtherWindow", "25"))
        self.comboBox_2.setItemText(25, _translate("OtherWindow", "26"))
        self.comboBox_2.setItemText(26, _translate("OtherWindow", "27"))
        self.comboBox_2.setItemText(27, _translate("OtherWindow", "28"))
        self.comboBox_2.setItemText(28, _translate("OtherWindow", "29"))
        self.comboBox_2.setItemText(29, _translate("OtherWindow", "30"))
        self.label.setText(_translate("OtherWindow", "Колличество элементов"))
        self.clear.setText(_translate("OtherWindow", "Очистить"))
        self.agree.setText(_translate("OtherWindow", "Подтвердить"))
