import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PySide6.QtCore import QFile
from PySide6.QtGui import QFont
import os

basedir = os.path.dirname(__file__)

class mainApp:

    def __init__(self):
        loader = QUiLoader()
        self.window = ''
        self.current = ''

        def mainwindow_setup(w):
            w.setWindowTitle("MainWindow Title")

        app = QtWidgets.QApplication(sys.argv)
        filer = QFile(os.path.join(basedir, 'main.ui'))
        filer.open(QFile.ReadOnly)
        self.window = loader.load(filer, None)
        filer.close()
        mainwindow_setup(self.window)
        self.window.showFullScreen()
        self.triggers()

        app.exec()

    def openFileSystem(self,event):
        file = self.openFileDialog()
        text=open(file).read()
        self.window.textEdit.setPlainText(text)
        self.window.labeltxt.setText(file)

    def openFileDialog(self):
        parent = None # QtGui.QMainWindow()
        filters = "*.txt" # Only allow these file ext to be opened
        title = "Open"
        open_at = "directory/"
        results = QFileDialog.getOpenFileName(parent, title, open_at, filters)
        self.current = results[0]
        return results[0]

    def openSaveAsDialog(self):
        parent = None # QtGui.QMainWindow()
        filters = "*.txt" # Only allow these file ext to be opened
        title = "Save"
        open_at = "directory/"
        results = QFileDialog.getSaveFileName(parent, title, open_at, filters)
        return results[0]
    
    def SaveAsFileSystem(self,event):
        file = self.openSaveAsDialog()
        text = open(file,'w').write(self.window.textEdit.toPlainText())
        self.window.labeltxt.setText(file)

    
    def SaveFileSystem(self,event):
        if self.current == '':
            pass
        else:
            text = open(self.current,'w').write(self.window.textEdit.toPlainText())

    def changeFont(self,event):
        self.window.textEdit.setFontPointSize(self.window.fontSpin.value())

    def boldText(self,event):
        if self.window.bold.isChecked():
            self.window.textEdit.setFontWeight(700)
        else:
            self.window.textEdit.setFontWeight(400)
    
    def italicText(self,event):
        if self.window.italic.isChecked():
            self.window.textEdit.setFontItalic(True)
        else:
            self.window.textEdit.setFontItalic(False)
    
    def underlineText(self,event):
        if self.window.underline.isChecked():
            self.window.textEdit.setFontUnderline(True)
        else:
            self.window.textEdit.setFontUnderline(False)

    def triggers(self):
        self.window.actionOpen.triggered.connect(self.openFileSystem)
        self.window.actionSave_As.triggered.connect(self.SaveAsFileSystem)
        self.window.actionSave.triggered.connect(self.SaveFileSystem)
        self.window.actionExit.triggered.connect(self.exitApp)
        self.window.fontSpin.valueChanged.connect(self.changeFont)
        self.window.bold.clicked.connect(self.boldText)
        self.window.italic.clicked.connect(self.italicText)
        self.window.underline.clicked.connect(self.underlineText)
        self.window.fontBox.currentIndexChanged.connect(self.index_changed)

    def index_changed(self,index):
        if index == 1:
            self.window.textEdit.setCurrentFont(QFont('Times', 10))
        else:
            self.window.textEdit.setCurrentFont(QFont("Courier New", 10))
            

    def exitApp(self,event):
        QApplication.quit()



if __name__ == '__main__':
    app = mainApp()