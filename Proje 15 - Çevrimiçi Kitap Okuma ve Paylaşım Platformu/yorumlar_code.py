from PyQt5.QtWidgets import *
from yorumlar import Ui_MainWindow


class YorumlarPage(QMainWindow):
    def __init__(self, kullanici_adi=None):
        super().__init__()
        self.yorum = Ui_MainWindow()
        self.yorum.setupUi(self)
        self.kullanici_adi = kullanici_adi  # Kullanıcı adını önceden tanımla
        self.yorum.pushButton_7.clicked.connect(self.geriDon)  # Doğru metod adını kullan
        self.yorumlariYukle()
        self.yorum.tableWidget.setColumnCount(3)
        self.yorum.tableWidget.setHorizontalHeaderLabels(["Kitap Adı", "Yorum Yapan Kullanıcı", "Yorumu"])
        self.yorum.tableWidget.horizontalHeader().setStretchLastSection(True)

    def geriDon(self):
        from home_page_code import HomePage
        self.close()

        self.dene = HomePage(self.kullanici_adi)
        self.dene.show()


    
    def yorumlariYukle(self):
        try:
            with open('yorumlar.txt', 'r', encoding='utf-8') as file:
                yorumlar = [line.strip().split(',') for line in file.readlines()]

            self.yorum.tableWidget.setRowCount(len(yorumlar))
            for i, yorum in enumerate(yorumlar):
                for j, item in enumerate(yorum):
                    self.yorum.tableWidget.setItem(i, j, QTableWidgetItem(item))
        except FileNotFoundError:
            QMessageBox.warning(self, "Hata", "Yorumlar dosyası bulunamadı.")



    