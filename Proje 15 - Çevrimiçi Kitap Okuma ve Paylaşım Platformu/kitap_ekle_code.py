from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from kitap_ekle import Ui_MainWindow

class KitapPage(QMainWindow):
    def __init__(self, home_page):
        super().__init__()
        self.kitapekle = Ui_MainWindow()
        self.kitapekle.setupUi(self)
        self.home_page = home_page
        self.kitapekle.pushButton_4.clicked.connect(self.kitap_ekle)

    def kitap_ekle(self):
        kitap_adi = self.kitapekle.lineEdit_2.text()
        yazar = self.kitapekle.lineEdit_3.text()
        yayinevi = self.kitapekle.lineEdit_4.text()
        basim_yili = self.kitapekle.lineEdit_5.text()
        sayfa_sayisi = self.kitapekle.lineEdit_6.text()


        if not all([kitap_adi, yazar, yayinevi,basim_yili, sayfa_sayisi]):
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurunuz.")
            return

        if not sayfa_sayisi.isdigit():
            QMessageBox.warning(self, "Hata", "Sayfa sayısı rakamlardan oluşmalıdır.")
            return
            
        self.home_page.ekle_kitap(kitap_adi, yazar, yayinevi,basim_yili, sayfa_sayisi)
        QMessageBox.information(self, "Başarılı", "Kitap başarıyla eklendi.")
        self.close()
