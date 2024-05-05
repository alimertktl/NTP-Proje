from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from okuduklarim import Ui_MainWindow

class Okunan(QMainWindow):
    def __init__(self, kullanici_adi=None):
        super().__init__()
        self.kullanici_adi = kullanici_adi  # Önce kullanıcı adını ayarla
        self.oku = Ui_MainWindow()
        self.oku.setupUi(self)
        self.oku.pushButton_7.clicked.connect(self.geri_git)  # Geri git butonuna fonksiyon ataması
        self.yukleOkunanKitaplar()  # Kullanıcı adı ayarlandıktan sonra kitapları yükle
        self.loadReadBooks()
    
    
    def geri_git(self):
        from home_page_code import HomePage
        self.anasayfa_geri_don = HomePage(self.kullanici_adi)
        self.anasayfa_geri_don.show()
        self.close()

    def yukleOkunanKitaplar(self):
        try:
            with open('okunan_kitaplar.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
            self.oku.tableWidget.setRowCount(0)  # Mevcut satırları temizle
            for line in lines:
                kullanici, kitap = line.strip().split(',')
                if kullanici == self.kullanici_adi:  # Yalnızca giriş yapan kullanıcının kitaplarını yükle
                    row_count = self.oku.tableWidget.rowCount()
                    self.oku.tableWidget.insertRow(row_count)
                    self.oku.tableWidget.setItem(row_count, 0, QTableWidgetItem(kitap))
                    self.oku.tableWidget.setItem(row_count, 1, QTableWidgetItem("Okundu"))
        except FileNotFoundError:
            print("Dosya bulunamadı.")


    def loadReadBooks(self):
        print("Kullanıcı adı:", self.kullanici_adi)


    def showEvent(self, event):
        super().showEvent(event)
        self.yukleOkunanKitaplar()