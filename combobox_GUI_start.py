from PyQt5 import QtWidgets
#from combobox import Ui_MainWindow
from combobox_qtpy import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Добавляем новые значения
        self.ui.comboBox.addItem("Программист")
        self.ui.comboBox.addItem("Дизайнер")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
