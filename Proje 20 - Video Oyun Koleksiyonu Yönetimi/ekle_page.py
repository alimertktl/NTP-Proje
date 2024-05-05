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
        tur = self.ekleform.lineEdit_tur.text()
        yapimci = self.ekleform.lineEdit_yapimci.text()
        platform = self.ekleform.lineEdit_platform.text()

        if not ad or not tur or not yapimci or not platform:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return
        
        self.cur.execute("INSERT INTO oyunlar (ad, tur, yapimci, platform, puan) VALUES (?, ?, ?, ?, ?)", (ad, tur, yapimci, platform, 0 ))
        self.conn.commit()

        QMessageBox.information(self, "Başarılı", "Oyun başarıyla eklendi.")

        self.close()
        self.anasayfaac.show()

    def iptal(self):
        self.close()
        self.anasayfaac.show()