import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QStatusBar,
    QToolBar,
    QFileDialog,
)


class MainWindow(QMainWindow):
    filename='new.txt'
    Saved=True #if saved = false then show warning before open another or new file
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.filename)

        self.Editor=QTextEdit()
        self.setCentralWidget(self.Editor)

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
        fname,fltr=QFileDialog.getSaveFileName(
            self,
            caption='Save File',
            dir=self.filename
        )
        self.filename=fname.split('/')[-1]
        self.setWindowTitle(self.filename)
        with open(fname,'w') as f:
            f.write(self.Editor.toPlainText())
        print(fname,' Saved!')
    
    def openfile(self):
        print('File Opened')

    def newfile(self):
        print('New File')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
