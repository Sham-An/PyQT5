from PyQt5 import QtWidgets, QtCore, QtGui
# Импортируем наш файл
from qline_form_QT5 import Ui_MainWindow
import sys
#https://python-scripts.com/pyqt5?ysclid=lagg1me49i992191830#load-ui-convert-to-py

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Меняем текст Для 1-го QLineEdit
        self.ui.lineEdit.setText("Добро пожаловать на PythonScripts")

        # указать максимальную длину Для 2-го QLineEdit
        self.ui.lineEdit_2.setMaxLength(10)

        # ввод пароля Для 3-го QLineEdit
        self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        # только чтение без изменения содержимого.
        self.ui.lineEdit_4.setReadOnly(True)

        # меняем цвет вводимого текста
        self.ui.lineEdit_5.setStyleSheet("color: rgb(28, 43, 255);")

        # изменение цвета фона QLineEdit
        self.ui.lineEdit_6.setStyleSheet("background-color: rgb(28, 43, 255);")

        self.ui.label.setFont(QtGui.QFont('SansSerif', 30))  # Изменение шрифта и размера
        self.ui.label.setText("PyScripts")  # Меняем текст




app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())