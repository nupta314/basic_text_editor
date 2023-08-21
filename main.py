import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTextEdit
)  # <1>


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # <2>

        self.setWindowTitle("My App")

        Editor=QTextEdit('Type Here...')

        # Set the central widget of the Window.
        self.setCentralWidget(Editor)  # <3>


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
