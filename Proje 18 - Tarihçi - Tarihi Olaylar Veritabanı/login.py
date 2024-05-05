from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from giris_py import Ui_MainWindow
from tarih import TarihPage

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_MainWindow()
        self.loginform.setupUi(self)


        self.loginform.pushButton.clicked.connect(self.tarihsayfasi)


    def tarihsayfasi(self):
        self.window = TarihPage()
        self.window.show()
        self.close()
