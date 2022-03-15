import sys
from PyQt5 import QtCore, QtWidgets

editorProgram = 'notepad'                                            # notepad

class ListenWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ListenWindow, self).__init__(parent)

        self.button_listen = QtWidgets.QPushButton('Выбрать файл', self)
        font1 = self.button_listen.font()
        font1.setPointSize(10)
        self.button_listen.setFont(font1)
        self.button_listen.setFixedSize(200, 50)
        self.button_listen.clicked.connect(self.startToListen)

        self.v_box1 = QtWidgets.QVBoxLayout(self)
        self.v_box1.addWidget(self.button_listen)

    def startToListen(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                        'Open File',
                        './',
                        'py Files (*.py);;Text Files (*.txt);;CSV Files (*.csv)')
        if not file:
            return

        process = QtCore.QProcess(self)
        process.start(editorProgram, [file])

        self.setEnabled(False)
        process.finished.connect(lambda: self.setEnabled(True))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ListenWindow()
    window.setWindowTitle('notepad file-listener')
    window.show()
    sys.exit(app.exec_())

#Magic;010460702275050821001EAcl2qQpCX91EE0692czdQMCwODqV3JuE/9w6wMnpYxl21pG4BUZ3yRKPo0CY=;04607022750508;001EAcl2qQpCX;;;