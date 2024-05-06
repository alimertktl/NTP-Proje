from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from home import Ui_MainWindow
from satis_talep_code import SatisPage
from destek_sayfa_code import DestekPage
import sys

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.homesayfa = Ui_MainWindow()
        self.homesayfa.setupUi(self)

        # SatisPage ve DestekPage sayfalarını tanımlayın
        self.satissayfaAc = SatisPage()
        self.desteksayfaAc = DestekPage()

        # Veri okuma fonksiyonları
        self.veriler = self.musterioku()  # Müşterileri oku
        self.veriler2 = self.ensturmanoku()  # Enstrümanları oku
        self.veriler3 = self.satisoku()  # Satışları oku

        # Buton bağlantıları
        self.homesayfa.pushButton.clicked.connect(self.destektalep)  # Destek talebi
        self.homesayfa.pushButton_4.clicked.connect(self.LineEditler)  # Müşteri ekle
        self.homesayfa.pushButton_3.clicked.connect(self.LineEditler2)  # Enstrüman ekle
        self.homesayfa.pushButton_5.clicked.connect(self.LineEditler3)  # Satış ekle
        self.homesayfa.pushButton_6.clicked.connect(self.showSatisPage)  # Bilgiler butonu

    # Destek talebi sayfasını açan fonksiyon
    def destektalep(self):
        self.desteksayfaAc.show()

    # Müşterileri dosyadan okuyan fonksiyon
    def musterioku(self):
        try:
            with open("musteriler.txt", "r") as file:
                return [tuple(line.strip().split(",")) for line in file]
        except FileNotFoundError:
            return []

    # Enstrümanları dosyadan okuyan fonksiyon
    def ensturmanoku(self):
        try:
            with open("ensturmanlar.txt", "r") as file:
                return [tuple(line.strip().split(",")) for line in file]
        except FileNotFoundError:
            return []

    # Satışları dosyadan okuyan fonksiyon
    def satisoku(self):
        try:
            with open("satislar.txt", "r") as file:
                return [tuple(line.strip().split(",")) for line in file]
        except FileNotFoundError:
            return []

    # Müşteri ekleme kontrolü
    def LineEditler(self):
        ad = self.homesayfa.lineEdit_2.text().strip()
        tel = self.homesayfa.lineEdit_4.text().strip()
        gecmis = self.homesayfa.lineEdit_3.text().strip()

        if any(x == "" for x in [ad, tel, gecmis]):
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return  # Boş alan kontrolü

        if not self.kullaniciInfo(ad, tel, gecmis):
            self.veriler.append((ad, tel, gecmis))
            self.veriDepo(self.veriler)
            QMessageBox.information(self, "Başarılı", "Müşteri başarıyla kaydedildi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Bu müşteri zaten sistemde kayıtlı.")

    # Müşteri bilgilerini kontrol eden fonksiyon
    def kullaniciInfo(self, ad, tel, gecmis):
        for item in self.veriler:
            if item[:3] == (ad, tel, gecmis):
                return True
        return False

    # Müşteri verilerini dosyaya kaydeden fonksiyon
    def veriDepo(self, veriler):
        try:
            with open("musteriler.txt", "w") as file:
                for item in veriler:
                    file.write(",".join(item) + "\n")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Veri kaydetme hatası: {e}")

    # Enstrüman ekleme kontrolü
    def LineEditler2(self):
        ensturman_ad = self.homesayfa.lineEdit_7.text().strip()
        stok_miktar = self.homesayfa.lineEdit_5.text().strip()
        ensturman_kod = self.homesayfa.lineEdit_6.text().strip()

        if any(x == "" for x in [ensturman_ad, stok_miktar, ensturman_kod]):
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return

        if not self.ensturmanKayıtlı(ensturman_ad, stok_miktar, ensturman_kod):
            self.veriler2.append((ensturman_ad, stok_miktar, ensturman_kod))
            self.ensturmanDepo(self.veriler2)
            QMessageBox.information(self, "Başarılı", "Enstrüman başarıyla kaydedildi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Bu enstrüman zaten sistemde kayıtlı.")

    # Enstrüman verilerini kaydeden fonksiyon
    def ensturmanDepo(self, veriler):
        try:
            with open("ensturmanlar.txt", "w") as file:
                for item in veriler:
                    file.write(",".join(item) + "\n")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Veri kaydetme hatası: {e}")

    # Enstrümanların kayıtlı olup olmadığını kontrol eden fonksiyon
    def ensturmanKayıtlı(self, ensturman_ad, stok_miktar, ensturman_kod):
        for item in self.veriler2:
            if item[:3] == (ensturman_ad, stok_miktar, ensturman_kod):
                return True
        return False

    # Satış ekleme kontrolü
    def LineEditler3(self):
        satis_no = self.homesayfa.lineEdit_10.text().strip()
        urun_ad = self.homesayfa.lineEdit_9.text().strip()
        urun_kod = self.homesayfa.lineEdit_8.text().strip()

        if any(x == "" for x in [satis_no, urun_ad, urun_kod]):
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return

        if not self.satisKayıtlı(satis_no, urun_ad, urun_kod):
            self.veriler3.append((satis_no, urun_ad, urun_kod))
            self.satisDepo(self.veriler3)
            QMessageBox.information(self, "Başarılı", "Satış başarıyla kaydedildi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Bu satış zaten sistemde kayıtlı.")

    # Satış verilerini kaydeden fonksiyon
    def satisDepo(self, veriler):
        try:
            with open("satislar.txt", "w") as file:
                for item in veriler:
                    file.write(",".join(item) + "\n")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Veri kaydetme hatası: {e}")

    # Satışların kayıtlı olup olmadığını kontrol eden fonksiyon
    def satisKayıtlı(self, satis_no, urun_ad, urun_kod):
        for item in self.veriler3:
            if item[:3] == (satis_no, urun_ad, urun_kod):
                return True
        return False

    # Bilgiler butonu ile diğer sayfaya geçiş
    def showSatisPage(self):
        try:
            self.satissayfaAc.satislariYukle()
            self.satissayfaAc.musterileriYukle()
            self.satissayfaAc.talepleriYukle()
            self.satissayfaAc.show()  # Yeni pencereyi göster
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Geçiş hatası: {e}")
