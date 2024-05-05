import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from kayit import Ui_Form

class Kayıtsayfası(QWidget):
     def __init__(self):
        super().__init__()

        self.kayitform = Ui_Form()
        self.kayitform.setupUi(self)

        self.kayitform.pushButton_Kayit.clicked.connect(self.Kayitol)
        self.kayitform.pushButton_iptal.clicked.connect(self.iptal)

     def Kayitol(self):
        kadi = self.kayitform.lineEdit_Kadi.text()
        sifre = self.kayitform.lineEdit_Sifre.text()

        if not kadi or not sifre:
            QMessageBox.warning(self, 'Hata', 'Kullanıcı adı ve şifre boş bırakılamaz!')
            return

        conn = sqlite3.connect('Veritabani.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi=?", (kadi,))
        existing_user = cursor.fetchone()

        if existing_user:
            QMessageBox.warning(self, 'Hata', 'Bu kullanıcı adı zaten mevcut!')
            conn.close()
            return
        
        cursor.execute("INSERT INTO kullanicilar (kullaniciadi, sifre) VALUES (?, ?)", (kadi, sifre))
        conn.commit()
        conn.close()

        QMessageBox.information(self, 'Başarılı', 'Kayıt işlemi başarıyla tamamlandı. Giriş sayfasına yönlendiriliyorsunuz.')
        self.girissayfa()
        self.close()
    
     def girissayfa(self):
        from giris_page import GirisSayfası
        self.girisac = GirisSayfası() 
        self.girisac.show()

     def iptal(self):
        self.girissayfa()
        self.close()