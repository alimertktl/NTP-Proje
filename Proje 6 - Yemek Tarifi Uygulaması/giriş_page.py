import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from giriş import Ui_Form
from anasayfa_page import Anasayfa
from Kayit_page import Kayıtsayfası

class GirişSayfası(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.anasayfaac = Anasayfa()
        self.kayitsayfasıac = Kayıtsayfası()
        self.loginform.pushButton_Giris.clicked.connect(self.GirisYap)
        self.loginform.pushButton_Kayit.clicked.connect(self.Kayit)

    def GirisYap(self):
        kadi = self.loginform.lineEdit_Kadi.text()
        sifre = self.loginform.lineEdit_Sifre.text()

        conn = sqlite3.connect('Bilgiler.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM kullanıcılar WHERE kullaniciadi=? AND sifre=?", (kadi, sifre))
        user = cursor.fetchone()

        if user:
            self.hide()
            self.anasayfaac.show()
        else:
            QMessageBox.warning(self, 'Hata', 'Geçersiz kullanıcı adı veya şifre!')
        
        conn.close()

    def Kayit(self):
        self.close()
        self.kayitsayfasıac.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GirişSayfası()
    window.show()
    sys.exit(app.exec_())
        