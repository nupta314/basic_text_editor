import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        Editor=QTextEdit()
        self.setCentralWidget(Editor)

        toolbar=QToolBar('Main Toolbar')
        self.addToolBar(toolbar)

        



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
