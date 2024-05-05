from PyQt5.QtWidgets import QMainWindow
from Randevu_home_page import Ui_MainWindow
from randevu_al_kodu import RandevuAL
from randevu_iptal_kodu import Randevuİptal


class HomePage(QMainWindow):
   def __init__(self):
      super().__init__()
      self.anasayfa = Ui_MainWindow()
      self.anasayfa.setupUi(self)
      self.randevuAc = RandevuAL()
      self.randevuİptal = Randevuİptal()
      self.anasayfa.pushButton.clicked.connect(self.calistir)
      self.anasayfa.pushButton_2.clicked.connect(self.calistir2)

   def calistir(self):
      self.randevuAc.show()
      self.close()

   def calistir2(self):
      self.randevuİptal.show()
      self.close()