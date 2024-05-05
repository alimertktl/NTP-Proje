from PyQt5.QtWidgets import *
from ekle import Ui_Form
import sqlite3
from anasayfa_page import Anasayfa

class Eklesayfa(QWidget):
    def __init__(self,kadi):
        super().__init__()

        self.ekleform = Ui_Form()
        self.ekleform.setupUi(self)
        self.kadi = kadi

        self.anasayfaac = Anasayfa(kadi)

        self.conn = sqlite3.connect("Veritabani.db")
        self.cur = self.conn.cursor()

        self.ekleform.pushButton_ekle.clicked.connect(self.oyunekle)
        self.ekleform.pushButton_iptal.clicked.connect(self.iptal)

    def oyunekle(self):
        ad = self.ekleform.lineEdit_ad.text()
        fiyat = self.ekleform.lineEdit_fiyat.text()
        stok = self.ekleform.lineEdit_stok.text()

        if not ad or not fiyat or not stok:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return
        
        self.cur.execute("INSERT INTO menu (ad, fiyat, stok) VALUES (?, ?, ?)", (ad, fiyat, stok))
        self.conn.commit()

        QMessageBox.information(self, "Başarılı", "Ürün Başarıyla Eklendi.")

        self.close()
        self.anasayfaac.show()

    def iptal(self):
        self.close()
        self.anasayfaac.show()