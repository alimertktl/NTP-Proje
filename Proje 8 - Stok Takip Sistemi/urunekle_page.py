import sqlite3
from PyQt5.QtWidgets import *
from urunekle import Ui_Form
from yönetim_page import YönetimSayfası
from PyQt5.QtGui import QIntValidator

class UrunekleSayfası(QWidget):
    def __init__(self):
        super().__init__()

        self.urunform = Ui_Form()
        self.urunform.setupUi(self)
        
        self.yönetimac = YönetimSayfası()

        self.conn = sqlite3.connect("Bilgiler.db")
        self.cur = self.conn.cursor()

        self.urunform.lineEdit_miktar.setValidator(QIntValidator())  # Stok Miktarına sadece integer değer girilebilmesini sağlar

        self.urunform.pushButton_ekle.clicked.connect(self.ekle)
        self.urunform.pushButton_iptal.clicked.connect(self.iptal)

    def ekle(self):
        urun_adı = self.urunform.lineEdit_ad.text()
        urun_miktar = self.urunform.lineEdit_miktar.text()

        if not urun_adı or not urun_miktar:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return

        self.cur.execute("INSERT INTO urunler (ürünad, stokmiktar) VALUES (?, ?)", (urun_adı, urun_miktar ))
        self.conn.commit()

        QMessageBox.information(self, "Başarılı", "Ürün başarıyla eklendi.")

        self.close()
        self.yönetimac.show()
        self.yönetimac.uruntablosu()

    def iptal(self):
        self.close()
        self.yönetimac.show()

