from PyQt5.Qt import (
QApplication, QWidget, QSplitter, QTreeView, QTextEdit,
QFileSystemModel, QVBoxLayout, QDir, QTextBrowser
)
import os


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Direct tree')

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index('/'))
        self.tree.doubleClicked.connect(self._on_double_clicked)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.resize(60, 40)

        self.textEdit = QTextEdit()
        #self.textView = QTextBrowser()
        self.text_browser = QTextBrowser(self)

        splitter = QSplitter()
        splitter.addWidget(self.tree)
        splitter.addWidget(self.textEdit)
        splitter.setSizes([80, 200])

        main_layout = QVBoxLayout()
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)

    def _on_double_clicked(self, index):
        file_name = self.model.filePath(index)

        with open(file_name, encoding='utf-8') as f:
            text = f.read()
            self.textEdit.setPlainText(text)
            #self.textView.s

if __name__ == "__main__":
    app = QApplication([])

    win = MyWidget()
    win.resize(600, 600)
    win.show()

    app.exec()