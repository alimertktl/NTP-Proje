from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from spor_home import Ui_MainWindow
from egzersizler_code import EgzersizPage
from a_takip_code import TakipPage


class SporPage(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.sporsayfa = Ui_MainWindow()
        self.sporsayfa.setupUi(self)
        self.sporsayfa.pushButton_2.clicked.connect(self.egzersizSayfasi)
        self.egzersizAc = EgzersizPage()
        self.takipAc = TakipPage()
        

        self.sporsayfa.pushButton_4.clicked.connect(self.LineEditler)
        self.sporsayfa.pushButton.clicked.connect(self.takipSayfasi)

        self.veriler = self.sporcuOku()
        self.veriler2 = self.antremanOku()

    def egzersizSayfasi(self):
        self.egzersizAc.show()
    
    def takipSayfasi(self):
        self.takipAc.show()



    def LineEditler(self):
        ad_soyad = self.sporsayfa.lineEdit_2.text()
        spor_dali = self.sporsayfa.lineEdit_3.text()
        boy = self.sporsayfa.lineEdit_4.text()
        kilo = self.sporsayfa.lineEdit_5.text()
        yas = self.sporsayfa.lineEdit_6.text()



        egzersiz1 = self.sporsayfa.comboBox.currentText()
        egzersiz2 = self.sporsayfa.comboBox_2.currentText()
        egzersiz3 = self.sporsayfa.comboBox_3.currentText()
        egzersiz4 = self.sporsayfa.comboBox_4.currentText()
        egzersiz5 = self.sporsayfa.comboBox_5.currentText()




        if not ad_soyad or not spor_dali or not boy or not kilo or not yas:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm bilgileri eksiksiz giriniz.")
        else:
            if not self.kullaniciInfo(ad_soyad, spor_dali, boy, kilo, yas):
                self.veriler.append((ad_soyad, spor_dali, boy, kilo, yas,))
                self.veriler2.append((egzersiz1,egzersiz2,egzersiz3,egzersiz4,egzersiz5))
                self.veriDepo2(self.veriler2)
                self.veriDepo(self.veriler)

                QMessageBox.information(self, "Başarılı", "Program oluşturuldu.")
                self.takipAc.sporcuYenile()  
                self.takipAc.antremanYenile()  


            else:
                QMessageBox.warning(self, "Uyarı", "Girilen sporcu bilgileri sistemde kayıtlı.")



    def kullaniciInfo(self,ad_soyad, spor_dali, boy, kilo, yas):
        for item in self.veriler:
            if item[:5] == (ad_soyad, spor_dali, boy, kilo, yas):
                return True
        return False

    def veriDepo(self,veriler):
        with open ('sporcu.txt',"w") as file:
            for gez  in veriler:
                file.write(",".join(gez) + "\n")   

    
    def veriDepo2(self,veriler2):
        with open ('antreman.txt',"w") as file:
            for gez  in veriler2:
                file.write(",".join(gez) + "\n") 
    

    def sporcuOku(self):
        try:
            with open("sporcu.txt","r") as file:
                return [tuple(line.strip().split(",")) for line in file]
        except FileNotFoundError:
            return[]

    def antremanOku(self):
        try:
            with open("antreman.txt","r") as file:
                return [tuple(line.strip().split(",")) for line in file]
        except FileNotFoundError:
            return[]


    