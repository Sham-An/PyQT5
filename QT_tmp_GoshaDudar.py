#
# https://www.youtube.com/playlist?list=PL0lO_mIqDDFXeDkOLHmEsL_HAEhw4-xDX

#Изучение PyQT (Python GUI) / Урок #3 – Разработка внутри Qt Designer
#https://youtu.be/CnMfhhx0GBI?list=PL0lO_mIqDDFXeDkOLHmEsL_HAEhw4-xDX
# изменить настройку языка без переустановки, добавив переменную среды LANG со значением en_US (щелкните правой кнопкой мыши "Компьютер", "Свойства", "Дополнительные системные настройки", "Переменные среды"

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        # https://youtu.be/LtgsjK2VnJg?list=PL0lO_mIqDDFXeDkOLHmEsL_HAEhw4-xDX&t=552
        self.main_text.setText("Это Базовая надпись")
        self.main_text.move(100, 100)
        # main_text.setFixedWidth(200)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)


    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()
    #print("add")



def application():
    app = QApplication(sys.argv)
    window = Window()
    #
    # window.setWindowTitle("Простая программа")
    # window.setGeometry(300, 250, 350, 200)
    #
    # main_text = QtWidgets.QLabel(window)
    # #https://youtu.be/LtgsjK2VnJg?list=PL0lO_mIqDDFXeDkOLHmEsL_HAEhw4-xDX&t=552
    # main_text.setText("Это Базовая надпись")
    # main_text.move(100, 100)
    # #main_text.setFixedWidth(200)
    # main_text.adjustSize()
    #
    # btn = QtWidgets.QPushButton(window)
    # btn.move(70, 150)
    # btn.setText("Нажми на меня")
    # btn.setFixedWidth(200)
    # btn.clicked.connect(add_label)
    # #https://youtu.be/LtgsjK2VnJg?list=PL0lO_mIqDDFXeDkOLHmEsL_HAEhw4-xDX&t=840

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()