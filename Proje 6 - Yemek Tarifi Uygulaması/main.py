from PyQt5.QtWidgets import QApplication
from giriş_page import GirişSayfası
from Kayit_page import Kayıtsayfası
app = QApplication([])
pencere = GirişSayfası()
pencere.show()
app.exec_() 