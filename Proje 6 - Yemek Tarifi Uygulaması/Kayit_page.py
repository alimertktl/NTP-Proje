import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from kayit import Ui_Form



class Kayıtsayfası(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.kayıtsayfasıform = Ui_Form()
        self.kayıtsayfasıform.setupUi(self)
        self.kayıtsayfasıform.pushButton_Kayit.clicked.connect(self.Kayitol)
        self.kayıtsayfasıform.pushButton_iptal.clicked.connect(self.iptal)

    def Kayitol(self):
        kadi = self.kayıtsayfasıform.lineEdit_Kadi.text()
        sifre = self.kayıtsayfasıform.lineEdit_Sifre.text()

        if not kadi or not sifre:
            QMessageBox.warning(self, 'Hata', 'Kullanıcı adı ve şifre boş bırakılamaz!')
            return
        
        conn = sqlite3.connect('Bilgiler.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM kullanıcılar WHERE kullaniciadi=?", (kadi,))
        existing_user = cursor.fetchone()

        if existing_user:
            QMessageBox.warning(self, 'Hata', 'Bu kullanıcı adı zaten mevcut!')
            conn.close()
            return
        
        cursor.execute("INSERT INTO kullanıcılar (kullaniciadi, sifre) VALUES (?, ?)", (kadi, sifre))
        conn.commit()
        conn.close()

        QMessageBox.information(self, 'Başarılı', 'Kayıt işlemi başarıyla tamamlandı. Giriş sayfasına yönlendiriliyorsunuz.')
        self.sabit()
        self.close()
    
    def sabit(self):
        from giriş_page import GirişSayfası
        self.girisac = GirişSayfası() 
        self.girisac.show()

    def iptal(self):
        self.sabit()
        self.close()