from PyQt5.QtWidgets import *
from giris import Ui_Form
from siparis_page import SiparisSayfası
from yönetim_page import YönetimSayfası

class GirisSayfası(QWidget):
    def __init__(self):
        super().__init__()

        self.girisform = Ui_Form()
        self.girisform.setupUi(self)
        
        self.siparissayfasıac = SiparisSayfası()
        self.yonetimsayfasıac = YönetimSayfası()
        self.girisform.pushButton_Siparis.clicked.connect(self.siparis)
        self.girisform.pushButton_Yonetim.clicked.connect(self.yonetim)

    def siparis(self):
        self.hide()
        self.siparissayfasıac.show()

    def yonetim(self):
        self.hide()
        self.yonetimsayfasıac.show()

