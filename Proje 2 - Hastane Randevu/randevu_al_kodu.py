from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from Randevu_al import Ui_MainWindow

class RandevuAL(QMainWindow):
    def __init__(self):
        super().__init__()
        self.randevuSayfa = Ui_MainWindow()
        self.randevuSayfa.setupUi(self)
        self.veriler = self.veriOku()
        self.tabloyuGuncelle()
        self.randevuSayfa.pushButton.clicked.connect(self.calistir)
        self.randevuSayfa.pushButton_2.clicked.connect(self.gericik)
        self.randevuSayfa.lineEdit_2.setInputMask('99999999999')
        self.randevuSayfa.lineEdit_3.setMaxLength(15)
        self.randevuSayfa.lineEdit_4.setMaxLength(15)

    def calistir(self):
        satir = self.randevuSayfa.tableWidget.selectionModel().selectedRows()
        if satir:
            secilisatir = satir[0].row()
            doktorDurumItem = self.randevuSayfa.tableWidget.item(secilisatir,3)
            doktorDurum = doktorDurumItem.text()

            if doktorDurum == "Randevusuz":
                tc = self.randevuSayfa.lineEdit_2.text()
                ad = self.randevuSayfa.lineEdit_4.text()
                soyad = self.randevuSayfa.lineEdit_3.text()
                doktorAd = self.randevuSayfa.tableWidget.item(secilisatir,0).text()
                doktorSoyad = self.randevuSayfa.tableWidget.item(secilisatir,1).text()
                doktorAlan = self.randevuSayfa.tableWidget.item(secilisatir,2).text()
                tarih = self.randevuSayfa.dateEdit.date().toString("yyyy-MM-dd")
                saat = self.randevuSayfa.timeEdit.time().toString("HH:mm")

                if tc and ad and soyad and tarih and saat:
                    if self.randevuZamaniKontrol(tarih, saat):
                        QMessageBox.warning(self, "Uyarı", "Bu tarih ve saatte zaten bir randevu var, lütfen başka bir zaman seçiniz.")
                    elif not self.kullaniciInfo(tc, ad, soyad, doktorAd, doktorSoyad, doktorAlan):
                        self.veriler.append((tc, ad, soyad, doktorAd, doktorSoyad, doktorAlan, "Randevuda", tarih, saat))
                        self.veriDepo(self.veriler)
                        self.randevuSayfa.tableWidget.setItem(secilisatir, 3, QTableWidgetItem("Randevuda"))
                        QMessageBox.information(self, "Başarılı", "Hasta ve doktor bilgileri ile randevu zamanı kaydedildi.")
                    else:
                        QMessageBox.warning(self, "Uyarı", "Aktif randevunuz bulunmakta.")
                else:
                    QMessageBox.warning(self, "Uyarı", "Lütfen gerekli bilgileri ve randevu zamanını giriniz.")
            else:
                QMessageBox.warning(self, "Uyarı", "Seçtiğiniz doktora ait başka bir randevu mevcut, lütfen başka bir doktor seçiniz.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen doktorunuzu seçiniz.")

    def kullaniciInfo(self,tc,ad,soyad,doktorAd,doktorSoyad,doktorAlan):
        for item in self.veriler:
            if item[:3] == (tc,ad,soyad) or item[3:6] == (doktorAd,doktorSoyad,doktorAlan):
                return True
        return False

    def randevuZamaniKontrol(self, tarih, saat):
        for veri in self.veriler:
            if len(veri) >= 9 and veri[7] == tarih and veri[8] == saat:
                return True
        return False

    def veriDepo(self,veriler):
        with open ('kullanıcılar.txt',"w") as file:
            for gez  in veriler:
                file.write(",".join(gez) + "\n")
    
    def veriOku(self):
        try:
            with open("kullanıcılar.txt","r") as file:
                return [tuple(line.strip().split(",")) for line in file]
        except FileNotFoundError:
            return[]
            


    def tabloyuGuncelle(self):
        for info in self.veriler:
            if len(info) >= 7:
                doktorAd,doktorSoyad,doktorAlan,doktorDurum = info[3] , info[4], info[5], info[6] 
                satirSayisi = self.randevuSayfa.tableWidget.rowCount()
                for row in range(satirSayisi):
                    if self.randevuSayfa.tableWidget.item(row,0).text() == doktorAd and \
                        self.randevuSayfa.tableWidget.item(row,1).text() == doktorSoyad and \
                        self.randevuSayfa.tableWidget.item(row,2).text() == doktorAlan:
                        self.randevuSayfa.tableWidget.setItem(row,3,QTableWidgetItem(doktorDurum))

        
    def sabit(self):
        from randevu_home_kodu import HomePage
        self.homeac = HomePage()
    def gericik(self):
        self.sabit()
        self.homeac.show()
        self.close()