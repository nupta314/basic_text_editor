import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
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

        new_action=QAction('&New',self)
        new_action.setStatusTip('Open New File')
        new_action.triggered.connect(self.newfile)
        toolbar.addAction(new_action)

        open_action=QAction('&Open',self)
        open_action.setStatusTip('Open Another File')
        open_action.triggered.connect(self.openfile)
        toolbar.addAction(open_action)

        save_action=QAction('&Save',self)
        save_action.setStatusTip('Save Current File')
        save_action.triggered.connect(self.savefile)
        toolbar.addAction(save_action)

        self.setStatusBar(QStatusBar(self))

    def savefile(self):
        print('File Saved')
    
    def openfile(self):
        print('File Opened')

    def newfile(self):
        print('New File')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
