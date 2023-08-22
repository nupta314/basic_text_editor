import sys
import os

from PySide6.QtGui import QAction
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    filename='new.txt'
    Saved=False #if saved = false then show warning before open another or new file
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.filename)

        self.Editor=QTextEdit()
        self.Editor.textChanged.connect(self.contentchanged)
        self.setCentralWidget(self.Editor)

        toolbar=QToolBar('Main Toolbar')
        self.addToolBar(toolbar)

        new_action=QAction('New',self)
        new_action.setStatusTip('Open New File')
        new_action.triggered.connect(self.newfile)
        toolbar.addAction(new_action)

        open_action=QAction('Open',self)
        open_action.setStatusTip('Open Another File')
        open_action.triggered.connect(self.openfile)
        toolbar.addAction(open_action)

        save_action=QAction('Save',self)
        save_action.setStatusTip('Save Current File')
        save_action.triggered.connect(self.savefile)
        toolbar.addAction(save_action)

        saveas_action=QAction('Save As',self)
        saveas_action.setStatusTip('Save Current File as')
        saveas_action.triggered.connect(self.savefileas)
        toolbar.addAction(saveas_action)

        self.status=QStatusBar(self)
        self.savedstatus=QLabel('File Saved : '+str(self.Saved),self.status)
        self.status.addWidget(self.savedstatus)
        self.setStatusBar(self.status)

    def newfile(self):
        if not self.checksaved():
            return
        self.filename='new.txt'
        self.Editor.setText('')
        print('New File Created')
        self.setWindowTitle(self.filename)
        self.Saved=False
        self.savedstatus.setText('File Saved : '+str(self.Saved))

    def openfile(self):
        if not self.checksaved():
            return
        fname,fltr=QFileDialog.getOpenFileName(
            self,
            caption='Open File',
        )
        if fname:
            self.filename=fname.split('/')[-1]
            print(fname,' Opended!')
            with open(fname,'r') as f:
                self.Editor.setText(f.read())
            self.setWindowTitle(self.filename)
            self.Saved=True
            self.savedstatus.setText('File Saved : '+str(self.Saved))

    def savefile(self):
        if os.path.exists(self.filename):
            '''with open(fname,'w') as f:
                f.write(self.Editor.toPlainText())'''
            return
        fname,fltr=QFileDialog.getSaveFileName(
            self,
            caption='Save File',
            dir=self.filename
        )
        if fname:
            self.filename=fname.split('/')[-1]
            print(fname,' Saved!')
            '''with open(fname,'w') as f:
                f.write(self.Editor.toPlainText())'''
            self.setWindowTitle(self.filename)
            self.Saved=True
            self.savedstatus.setText('File Saved : '+str(self.Saved))

    def savefileas(self):
        fname,fltr=QFileDialog.getSaveFileName(
            self,
            caption='Save File as',
            dir=self.filename
        )
        if fname:
            self.filename=fname.split('/')[-1]
            print(fname,' Saved!')
            '''with open(fname,'w') as f:
                f.write(self.Editor.toPlainText())'''
            self.setWindowTitle(self.filename)
            self.Saved=True
            self.savedstatus.setText('File Saved as : '+str(self.Saved))
    
    def contentchanged(self):
        self.Saved=False
        self.savedstatus.setText('File Saved : '+str(self.Saved))

    def checksaved(self):
        if self.Saved:
            return True
        warn=QMessageBox.question(self,'Warning','Continue without saving?')
        return warn==QMessageBox.Yes
        #write code to warn of unsaved file        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
