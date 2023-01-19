import sys
import os
from wquality import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_2.clicked.connect(self.rfc)
     self.ui.pushButton.clicked.connect(self.qfacts)
     self.ui.pushButton_3.clicked.connect(self.svm)
     self.ui.pushButton_4.clicked.connect(self.comp)
     self.ui.pushButton_5.clicked.connect(self.wepnts)
      

  def rfc(self):
    os.system("python rforest1.py")

  def wepnts(self):
    os.system("python extrpoints1.py")

  def qfacts(self):
    os.system("python qualfactors1.py")

  def svm(self):
    os.system("python svm1.py")

  def comp(self):
    os.system("python datasubset1.py")

      
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
