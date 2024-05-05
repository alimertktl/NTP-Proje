from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from home import Ui_MainWindow
from destek_sayfa_code import DestekPage
from satis_talep_code import SatisPage

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.homesayfa = Ui_MainWindow()
        self.homesayfa.setupUi(self)
        self.desteksayfaAc = DestekPage()
        self.satissayfaAc = SatisPage()
        self.veriler = self.musterioku()
        self.veriler2 = self.satisoku()


        self.homesayfa.pushButton.clicked.connect(self.destektalep)
        self.homesayfa.pushButton_2.clicked.connect(self.satis)
        self.homesayfa.pushButton_4.clicked.connect(self.LineEditler)
        self.homesayfa.pushButton_3.clicked.connect(self.LineEditler2)



    def destektalep(self):
        self.desteksayfaAc.show()

    def satis(self):
        self.satissayfaAc.show()
        self.close()


    def LineEditler(self):
        ad = self.homesayfa.lineEdit_2.text()
        tel = self.homesayfa.lineEdit_4.text()
        cinsiyet = self.homesayfa.lineEdit_3.text()

        if not ad or not tel or not cinsiyet:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm bilgileri eksiksiz giriniz.")
        else:
            if not self.kullaniciInfo(ad, tel, cinsiyet):
                self.veriler.append((ad, tel, cinsiyet))
                self.veriDepo(self.veriler)
                QMessageBox.information(self, "Başarılı", "Müşteri başarıyla kaydedildi.")
                self.satissayfaAc.satisyenile()  
                self.satissayfaAc.musteriyenile()  
                self.satissayfaAc.destekyenile()


            else:
                QMessageBox.warning(self, "Uyarı", "Girilen müşteri bilgileri sistemde kayıtlı.")

    
    def LineEditler2(self):
        satis_no = self.homesayfa.lineEdit_7.text()
        urun_ad = self.homesayfa.lineEdit_5.text()
        urun_kod = self.homesayfa.lineEdit_6.text()

        if not satis_no or not urun_ad or not urun_kod:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm bilgileri eksiksiz giriniz.")
        else:
            if not self.satislar(satis_no, urun_ad, urun_kod):
                self.veriler2.append((satis_no, urun_ad, urun_kod))
                self.satisdepo(self.veriler2)
                QMessageBox.information(self, "Başarılı", "Satış başarıyla kaydedildi.")
                self.satissayfaAc.satisyenile()  
                self.satissayfaAc.musteriyenile()  
                self.satissayfaAc.destekyenile()

            else:
                QMessageBox.warning(self, "Uyarı", "Girilen satış bilgileri sistemde kayıtlı.")


    def satislar(self,satis_no,urun_ad,urun_kod):
        for item in self.veriler2:
            if item[:3] == (satis_no,urun_ad,urun_kod):
                return True
        return False

    def satisdepo(self,veriler):
        with open ('satislar.txt',"w") as file:
            for gez  in veriler:
                file.write(",".join(gez) + "\n")   
    
    
    def kullaniciInfo(self,ad,tel,cinsiyet):
        for item in self.veriler:
            if item[:3] == (ad,tel,cinsiyet):
                return True
        return False

    def veriDepo(self,veriler):
        with open ('musteriler.txt',"w") as file:
            for gez  in veriler:
                file.write(",".join(gez) + "\n")
    
    def musterioku(self):
        try:
            with open("musteriler.txt","r") as file:
                return [tuple(line.strip().split(",")) for line in file]
        except FileNotFoundError:
            return[]

    def satisoku(self):
        try:
            with open("satislar.txt","r") as file:
                return [tuple(line.strip().split(",")) for line in file]
        except FileNotFoundError:
            return[]