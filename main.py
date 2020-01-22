#-------------------------------------------------------------------------------
import sys                             # Библиотека обеспечивает доступ к некоторым системным функциям
from interface import *                # Импорт всех аргументов из файла interface.py
import PyQt5.QtWidgets as QtWidgets    # Компоненты для приложения
import PyQt5.QtGui as QtGui            # Графический интерфейс пользователя
#-------------------------------------------------------------------------------

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def settings(ui):
    """Поле ввода для Числа отчетов : lineEdit"""
    ui.lineEdit.setValidator(QtGui.QIntValidator(0, 10 ** 6))

    """Поле ввода для ОСШ (Сигнал/Шум) : lineEdit_2"""

    """Поле ввода для Передавающих антенн : lineEdit_3"""

    """Поле ввода для Принимающих антенн : lineEdit_4"""

    """Поле ввода для Длины антенн : lineEdit_5"""

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    myapp.setFixedSize(441, 388)
    settings(myapp.ui) #Настройка объектов
    sys.exit(app.exec_())