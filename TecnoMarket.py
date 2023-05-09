import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QMainWindow
import pyqtdesign2

class KirishPagee(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui=pyqtdesign2.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.eventbtn)
        self.ui.pushButton_2.clicked.connect(self.eventbtn)
        
    def eventbtn(self):
        if self.sender().text()=="Sign up":
            pass
        
        
        
        
        
        
app=QApplication([])
win=KirishPagee()
win.show()
sys.exit(app.exec_())