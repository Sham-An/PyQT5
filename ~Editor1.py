import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 400, 300)
        self.setWindowTitle('Текстовый редактор')

        self.str_write = QLineEdit(self)
        self.str_write.resize(100, 20)
        self.str_write.move(20, 5)

        self.make_new = QPushButton(self)
        self.make_new.setText('Создать новый')
        self.make_new.resize(100, 20)
        self.make_new.move(20, 40)
        self.make_new.clicked.connect(self.make_new_file)

        self.save_file = QPushButton(self)
        self.save_file.setText('Сохранить файл')
        self.save_file.resize(100, 20)
        self.save_file.move(20, 70)
        self.save_file.clicked.connect(self.save_new_file)

        self.open_file = QPushButton(self)
        self.open_file.setText('Открыть файл')
        self.open_file.resize(100, 20)
        self.open_file.move(20, 100)

        self.text_output = QLineEdit(self)
        self.text_output.resize(200, 280)
        self.text_output.move(180, 10)

    def make_new_file(self):
        file = open(self.str_write.text(), mode='wr')
        data = file.readline()
        file.close()

    def save_new_file(self):
        pass

    def file_open(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())