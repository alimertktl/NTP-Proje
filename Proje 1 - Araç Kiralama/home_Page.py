from PyQt5.QtWidgets import QMainWindow 
from home import Ui_MainWindow
from kiralama_Page import KiralamaPage
from bilgi_Page import BilgiPage

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.homeform = Ui_MainWindow()
        self.homeform.setupUi(self)


        self.kiralamaAc = KiralamaPage() 
        self.bilgiAc = BilgiPage()         
        self.homeform.pushButton_2.clicked.connect(self.KiralamaSayfasi)
        self.homeform.pushButton_4.clicked.connect(self.bilgiSayfasi)

    def KiralamaSayfasi(self):
        self.kiralamaAc.show()
        self.close()

    def bilgiSayfasi(self):
        self.bilgiAc.show()
        self.close()
