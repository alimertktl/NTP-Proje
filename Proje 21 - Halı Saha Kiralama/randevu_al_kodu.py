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
            sahaDurum = self.randevuSayfa.tableWidget.item(secilisatir,3)
            sahaDurum = sahaDurum.text()

            if sahaDurum == "Randevusuz":
                uyelik_id = self.randevuSayfa.lineEdit_2.text()
                ad = self.randevuSayfa.lineEdit_4.text()
                soyad = self.randevuSayfa.lineEdit_3.text()
                saha_ad = self.randevuSayfa.tableWidget.item(secilisatir,0).text()
                saha_konum = self.randevuSayfa.tableWidget.item(secilisatir,1).text()
                saha_fiyat = self.randevuSayfa.tableWidget.item(secilisatir,2).text()
                tarih = self.randevuSayfa.dateEdit.date().toString("yyyy-MM-dd")
                saat = self.randevuSayfa.timeEdit.time().toString("HH:mm")

                if uyelik_id and ad and soyad and tarih and saat:
                    if self.randevuZamaniKontrol(tarih, saat):
                        QMessageBox.warning(self, "Uyarı", "Bu tarih ve saatte zaten bir maç randevusu var, lütfen başka bir zaman seçiniz.")
                    elif not self.kullaniciInfo(uyelik_id, ad, soyad, saha_ad, saha_konum, saha_fiyat):
                        self.veriler.append((uyelik_id, ad, soyad, saha_ad, saha_konum, saha_fiyat, "Saha Dolu", tarih, saat))
                        self.veriDepo(self.veriler)
                        self.tabloyuGuncelle()  

                        self.randevuSayfa.tableWidget.setItem(secilisatir, 3, QTableWidgetItem("Saha Dolu"))
                        QMessageBox.information(self, "Başarılı", "Saha randevunuz kaydedildi.")
                    else:
                        QMessageBox.warning(self, "Uyarı", "Aktif saha randevunuz bulunmakta.")
                else:
                    QMessageBox.warning(self, "Uyarı", "Lütfen gerekli bilgileri ve randevu zamanını giriniz.")
            else:
                QMessageBox.warning(self, "Uyarı", "Seçtiğiniz sahaya ait başka bir randevu mevcut, lütfen başka bir saha seçiniz.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen sahayı seçiniz.")

    def kullaniciInfo(self,uyelik_id,ad,soyad,saha_ad,saha_konum,saha_fiyat):
        for item in self.veriler:
            if item[:3] == (uyelik_id,ad,soyad) or item[3:6] == (saha_ad,saha_konum,saha_fiyat):
                return True
        return False

    def randevuZamaniKontrol(self, tarih, saat):
        for veri in self.veriler:
            if len(veri) >= 9 and veri[7] == tarih and veri[8] == saat:
                return True
        return False

    def veriDepo(self, veriler):
        try:
            with open('kullanıcılar.txt', "w", encoding='utf-8') as file:
                for gez in veriler:
                    temiz_gez = [str(g).strip() for g in gez]
                    veri_satiri = ",".join(temiz_gez)
                    file.write(veri_satiri + "\n")
        except Exception as e:
            print("Veri kaydetme sırasında bir hata oluştu:", e)

    
    def veriOku(self):
        dosya_yolu = 'kullanıcılar.txt'
        try:
            with open(dosya_yolu, 'r', encoding='utf-8') as file:
                return [tuple(line.strip().split(',')) for line in file]
        except UnicodeDecodeError:
            try:
                with open(dosya_yolu, 'r', encoding='iso-8859-1') as file:
                    return [tuple(line.strip().split(',')) for line in file]
            except Exception as e:
                print(f"Başka bir hata meydana geldi: {str(e)}")
                return []

            


    def tabloyuGuncelle(self):
        self.veriler = self.veriOku() 

        for info in self.veriler:
            if len(info) >= 7:
                saha_ad,saha_konum,saha_fiyat,sahaDurum = info[3] , info[4], info[5], info[6] 
                satirSayisi = self.randevuSayfa.tableWidget.rowCount()
                for row in range(satirSayisi):
                    if self.randevuSayfa.tableWidget.item(row,0).text() == saha_ad and \
                        self.randevuSayfa.tableWidget.item(row,1).text() == saha_konum and \
                        self.randevuSayfa.tableWidget.item(row,2).text() == saha_fiyat:
                        self.randevuSayfa.tableWidget.setItem(row,3,QTableWidgetItem(sahaDurum))

        
    def sabit(self):
        from randevu_home_kodu import HomePage
        self.homeac = HomePage()
    def gericik(self):
        self.sabit()
        self.homeac.show()
        self.close()