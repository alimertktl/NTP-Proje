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

        self.ekleform.pushButton_ekle.clicked.connect(self.icerikekle)
        self.ekleform.pushButton_iptal.clicked.connect(self.iptal)

    def icerikekle(self):
        tur = self.ekleform.lineEdit_tur.text()
        ad = self.ekleform.lineEdit_ad.text()
        yonetmen = self.ekleform.lineEdit_yonetmen.text()
        sure = self.ekleform.lineEdit_sure.text()

        if not tur or not ad or not yonetmen or not sure:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return
        
        self.cur.execute("INSERT INTO icerikler (tur, ad, yonetmen, sure) VALUES (?, ?, ?, ?)", (tur, ad, yonetmen, sure ))
        self.conn.commit()

        QMessageBox.information(self, "Başarılı", "İçerik başarıyla eklendi.")

        self.close()
        self.anasayfaac.show()

    def iptal(self):
        self.close()
        self.anasayfaac.show()

