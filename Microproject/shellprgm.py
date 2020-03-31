import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication,QTextEdit
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Show')
        
        impMenu = QMenu('Kernel Modules', self)
        impAct = QAction('Currently Loaded', self) 
        impMenu.addAction(impAct)
        impAct.triggered.connect(self.moDule)
        
        fileMenu.addMenu(impMenu)
   
        self.textbox = QTextEdit(self)
        self.textbox.move(25, 20)
        self.textbox.resize(750,600)

        self.setGeometry(800, 800, 800, 800)
        self.setWindowTitle('Shell Program')    
        self.show()
    def moDule(self):
       
        p1 = subprocess.run('lsmod', stdout=subprocess.PIPE)
        self.textbox.moveCursor(QtGui.QTextCursor.End)
        self.textbox.insertPlainText(p1.stdout.decode())

        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
