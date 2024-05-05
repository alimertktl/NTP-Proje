from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from home_page import Ui_MainWindow
from yorumlar_code import YorumlarPage
from yorum_yap_code import YorumPage
from okuduklarim_code import Okunan
class HomePage(QMainWindow):
    def __init__(self, kullanici_adi=None):
        super().__init__()
        self.homesayfa = Ui_MainWindow()
        self.homesayfa.setupUi(self)
        self.homesayfa.lineEdit_2.textChanged.connect(self.filter_table)  
        self.homesayfa.pushButton_4.clicked.connect(self.kitapAc)
        self.homesayfa.pushButton_6.clicked.connect(self.yyapilir)
        self.kullanici_adi = kullanici_adi
        self.homesayfa.pushButton_5.clicked.connect(self.kitapOku)  # Kitap oku butonuna fonksiyon ataması
        self.homesayfa.pushButton_8.clicked.connect(self.okunanlar)  # Kitap oku butonuna fonksiyon ataması
        self.okuma = Okunan(self.kullanici_adi)
        self.homesayfa.pushButton_7.clicked.connect(self.acYorumlarPage)  # Örnek buton adı

        self.yorumAc = YorumlarPage()
        self.kitapYukle()  

    def acYorumlarPage(self):
        self.yorumlarPage = YorumlarPage(self.kullanici_adi)
        self.yorumlarPage.show()
        self.close()

    def okunanlar(self):
        self.okuma.show()
        self.close()


    def yorumgit(self):
        self.yorumAc.show()
        self.close()







    def yyapilir(self):
        selected_row = self.homesayfa.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Hata", "Lütfen bir kitap seçin.")
        else:
            kitap_adi = self.homesayfa.tableWidget.item(selected_row, 0).text()
            from yorum_yap_code import YorumPage
            self.yorum_page = YorumPage(self, kitap_adi, self.kullanici_adi)
            self.yorum_page.show()

    def yorumKaydet(self, kitap_adi, kullanici_adi, yorum):
        with open('yorumlar.txt', 'a', encoding='utf-8') as file:
            file.write(f"{kitap_adi},{kullanici_adi},{yorum}\n")
        QMessageBox.information(self, "Başarılı", "Yorumunuz başarıyla kaydedildi.")


    def kitapAc(self):
        from kitap_ekle_code import KitapPage  
        self.kitapAcil = KitapPage(self)
        self.kitapAcil.show()

    def filter_table(self):
        search_text = self.homesayfa.lineEdit_2.text().lower()  
        for row in range(self.homesayfa.tableWidget.rowCount()):
            item = self.homesayfa.tableWidget.item(row, 0)  
            self.homesayfa.tableWidget.setRowHidden(row, search_text not in item.text().lower()) if item else self.tableWidget.setRowHidden(row, True)

    def ekle_kitap(self, kitap_adi, yazar, yayinevi, basim_yili, sayfa_sayisi, uyariver=True):
        for row in range(self.homesayfa.tableWidget.rowCount()):
            if self.homesayfa.tableWidget.item(row, 0) and self.homesayfa.tableWidget.item(row, 0).text() == kitap_adi:
                if uyariver:
                    QMessageBox.warning(self, "Hata", "Bu kitap zaten kayıtlı.")
                return
        row_count = self.homesayfa.tableWidget.rowCount()
        self.homesayfa.tableWidget.insertRow(row_count)
        self.homesayfa.tableWidget.setItem(row_count, 0, QTableWidgetItem(kitap_adi))
        self.homesayfa.tableWidget.setItem(row_count, 1, QTableWidgetItem(yazar))
        self.homesayfa.tableWidget.setItem(row_count, 2, QTableWidgetItem(yayinevi))
        self.homesayfa.tableWidget.setItem(row_count, 3, QTableWidgetItem(basim_yili))
        self.homesayfa.tableWidget.setItem(row_count, 4, QTableWidgetItem(sayfa_sayisi))
        if uyariver:
            self.kaydet(kitap_adi, yazar, yayinevi, basim_yili, sayfa_sayisi)

    def kaydet(self, kitap_adi, yazar, yayinevi, basim_yili, sayfa_sayisi):
        with open('kitaplar.txt', 'a', encoding='utf-8') as file:
            file.write(f"{kitap_adi},{yazar},{yayinevi},{basim_yili},{sayfa_sayisi}\n")

    def kitapYukle(self):
        try:
            with open('kitaplar.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    kitap_adi, yazar, yayinevi, basim_yili, sayfa_sayisi = line.strip().split(',')
                    self.ekle_kitap(kitap_adi, yazar, yayinevi, basim_yili, sayfa_sayisi, uyariver=False)
        except FileNotFoundError:
            pass



    def kitapOku(self):
        selected_row = self.homesayfa.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Hata", "Lütfen bir kitap seçin.")
        else:
            kitap_adi = self.homesayfa.tableWidget.item(selected_row, 0).text()
            self.okunanKitabiKaydet(kitap_adi)
            QMessageBox.information(self, "Başarılı", f"{kitap_adi} başarıyla okundu olarak işaretlendi.")
            self.homesayfa.tableWidget.setItem(selected_row, 4, QTableWidgetItem("Okundu"))
            print("Kitap okuma sırasında kullanıcı adı:", self.kullanici_adi)  # Debug için kullanıcı adını yazdır
            self.okunan_pencere = Okunan(self.kullanici_adi)

    def okunanKitabiKaydet(self, kitap_adi):
        with open('okunan_kitaplar.txt', 'a', encoding='utf-8') as file:
            file.write(f"{self.kullanici_adi},{kitap_adi}\n")