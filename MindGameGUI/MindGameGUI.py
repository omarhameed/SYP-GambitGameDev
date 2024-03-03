import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic

MAX_PER = 100
MID_PER = 49
MIN_PER = 0

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(None)
        uic.loadUi("MindGame.ui", self) #Load design
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.stopButton.setEnabled(False)
        
        #Create delay and then call start function after app is fully executed
        #QtCore.QTimer.singleShot(100, self.start)
        
    def start(self):
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.updateBar(50)
        time.sleep(1)
        self.updateBar(22)
        time.sleep(1)
        self.updateBar(71)
        time.sleep(1)
        self.updateBar(0)
        time.sleep(1)
        self.updateBar(100)
        
    def stop(self):
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.progressBar1.setValue(0)
        self.progressBar2.setValue(0)
    
    def updateBar(self, value):
        if (value > 100):
            percent = 100
        elif (value < 0):
            percent = 0
            
        percent = value
        self.progressBar1.setValue(percent)
        self.progressBar2.setValue(percent)
        
"""
        if (percent == MAX_PER):
            self.changeColor('green')
        elif ((percent < MAX_PER) and (percent > MID_PER)):
            self.changeColor('yellow')
        else:
            self.changeColor('red')
            
    def changeColor(self, color):
        css = ""
            ::chunk{{
                background: {0};
             }}
        "".format(color)
        self.progressBar1.setStyleSheet(css)
"""
        
    #def init(self):
            
  
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()