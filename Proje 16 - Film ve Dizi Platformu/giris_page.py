from PyQt5.QtWidgets import *
from giris import Ui_Form

import sqlite3
from anasayfa_page import Anasayfa
from kayit_page import Kayıtsayfası

class GirisSayfası(QWidget):
    def __init__(self):
        super().__init__()

        self.girisform = Ui_Form()
        self.girisform.setupUi(self)
        self.anasayfaac = None
        self.kayitsayfasıac = Kayıtsayfası()

        self.girisform.pushButton_Giris.clicked.connect(self.GirisYap)
        self.girisform.pushButton_Kayit.clicked.connect(self.Kayit)

    def GirisYap(self):
        kadi = self.girisform.lineEdit_Kadi.text()
        sifre = self.girisform.lineEdit_Sifre.text()

        conn = sqlite3.connect('Veritabani.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi=? AND sifre=?", (kadi, sifre))
        user = cursor.fetchone()

        if user:
            cursor.execute("CREATE TABLE IF NOT EXISTS {}_izleme_tablosu (tur text, ad TEXT UNIQUE, yonetmen TEXT, sure INTEGER)".format(kadi))
            cursor.execute("CREATE TABLE IF NOT EXISTS {}_izleme_gecmisi_tablosu (tur TEXT, ad TEXT UNIQUE, yonetmen TEXT, sure INTEGER)".format(kadi))
            self.anasayfaac = Anasayfa(kadi)
            self.hide()
            self.anasayfaac.show()
        else:
            QMessageBox.warning(self, 'Hata', 'Geçersiz kullanıcı adı veya şifre!')

        conn.close()
           
    def Kayit(self):
        self.close()
        self.kayitsayfasıac.show()


