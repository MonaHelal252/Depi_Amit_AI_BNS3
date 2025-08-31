from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
import time
 
class Main_App(QMainWindow):
    def __init__(self):
        super(Main_App,self).__init__()
        uic.loadUi('D:\Depi_DS_BS\DEPI_BNS_DS_R3\Sourses\DS\Linear_Algebra\std.ui',self)
        self.InitUI()
        self.handle_btn()
    def InitUI(self):
        self.setWindowTitle("Student System")
       
    def handle_btn(self):
        self.std_add_btn.clicked.connect(self.add_std_info)
       
    def add_std_info(self):
        print('welcome to my app')    
 
 
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_App()
    window.show()
    sys.exit(app.exec_())
 
