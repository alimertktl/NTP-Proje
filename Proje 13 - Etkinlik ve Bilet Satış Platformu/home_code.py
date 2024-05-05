from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from home import Ui_MainWindow
from satis_talep_code import SatisPage

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.homesayfa = Ui_MainWindow()
        self.homesayfa.setupUi(self)
        self.satissayfaAc = SatisPage()
        self.veriler = self.musterioku()
        self.veriler2 = self.satisoku()
        self.veriler3 = self.kullanicioku()


        self.homesayfa.pushButton_4.clicked.connect(self.LineEditler)
        self.homesayfa.pushButton_6.clicked.connect(self.LineEditler2)
        self.homesayfa.pushButton_5.clicked.connect(self.LineEditler3)
         
        self.homesayfa.pushButton_7.clicked.connect(self.satissayfasi)

        
    def satissayfasi(self):
        self.satissayfaAc.show()
        self.close()

        



    



    def satis(self):
        self.satissayfaAc.show()
        self.close()


    def LineEditler(self):
        ad = self.homesayfa.lineEdit_2.text()
        tarih = self.homesayfa.lineEdit_4.text()
        mekan = self.homesayfa.lineEdit_3.text()

        if not ad or not tarih or not mekan:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm bilgileri eksiksiz giriniz.")
        else:
            if not self.kullaniciInfo(ad, tarih, mekan):
                self.veriler.append((ad, tarih, mekan))
                self.veriDepo(self.veriler)
                QMessageBox.information(self, "Başarılı", "Etkinlik başarıyla kaydedildi.")
                self.satissayfaAc.satisyenile()  
                self.satissayfaAc.musteriyenile()  
                self.satissayfaAc.kullaniciyenile()


            else:
                QMessageBox.warning(self, "Uyarı", "Girilen etkinlik bilgileri sistemde kayıtlı.")

    
    def LineEditler2(self):
        bilet_no = self.homesayfa.lineEdit_7.text()
        etkinlik_bilgi = self.homesayfa.lineEdit_5.text()
        

        if not bilet_no or not etkinlik_bilgi :
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm bilgileri eksiksiz giriniz.")
        else:
            if not self.satislar(bilet_no, etkinlik_bilgi ):
                self.veriler2.append((bilet_no, etkinlik_bilgi ))
                self.satisdepo(self.veriler2)
                QMessageBox.information(self, "Başarılı", "Bilet başarıyla kaydedildi.")
                self.satissayfaAc.satisyenile()  
                self.satissayfaAc.musteriyenile()  
                self.satissayfaAc.kullaniciyenile()

            else:
                QMessageBox.warning(self, "Uyarı", "Girilen bilet bilgileri sistemde kayıtlı.")


    def LineEditler3(self):
        k_ad= self.homesayfa.lineEdit_10.text()
        k_no = self.homesayfa.lineEdit_9.text()
        b_alim= self.homesayfa.lineEdit_8.text()

        if not k_ad or not k_no or not b_alim:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm bilgileri eksiksiz giriniz.")
        else:
            if not self.durum(k_ad, k_no, b_alim):
                self.veriler3.append((k_ad, k_no, b_alim))
                self.kullancidepo(self.veriler3)
                QMessageBox.information(self, "Başarılı", "Kullanıcılar başarıyla kaydedildi.")
                self.satissayfaAc.satisyenile()  
                self.satissayfaAc.musteriyenile()  
                self.satissayfaAc.kullaniciyenile()


            else:
                QMessageBox.warning(self, "Uyarı", "Girilen kullanıcı bilgileri sistemde kayıtlı.")



    


    def satislar(self,bilet_no,etkinlik_bilgi):
        for item in self.veriler2:
            if item[:3] == (bilet_no,etkinlik_bilgi):
                return True
        return False

    def satisdepo(self,veriler):
        with open ('satislar.txt',"w") as file:
            for gez  in veriler:
                file.write(",".join(gez) + "\n")   
    
    
    def kullaniciInfo(self,ad,tarih,mekan):
        for item in self.veriler:
            if item[:3] == (ad,tarih,mekan):
                return True
        return False

    def veriDepo(self,veriler):
        with open ('musteriler.txt',"w") as file:
            for gez  in veriler:
                file.write(",".join(gez) + "\n")


    def durum(self,k_ad,k_no,b_alim):
        for item in self.veriler:
            if item[:3] == (k_ad,k_no,b_alim):
                return True
        return False

    def kullancidepo(self,veriler):
        with open ('kullanicilar.txt',"w") as file:
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
        

    def kullanicioku(self):
        try:
            with open("kullanicilar.txt","r") as file:
                return [tuple(line.strip().split(",")) for line in file]
        except FileNotFoundError:
            return[]