from PyQt5.QtWidgets import *
from bisiklet import Ui_MainWindow

class BisikletPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bisikletform = Ui_MainWindow()
        self.bisikletform.setupUi(self)
        self.bisikletform.pushButton.clicked.connect(self.satinAl)
        self.stokyukle() 
        self.bisikletform.pushButton_2.clicked.connect(self.geridonus)
        self.bisikletform.tableWidget.setColumnWidth(2,140)
        self.bisikletform.tableWidget.setColumnWidth(1,140)
        self.bisikletform.tableWidget.setColumnWidth(6,140)



    def sabit(self):
        from home_Page import HomePage
        self.homeAc = HomePage() 
    def geridonus(self):
        self.sabit()
        self.homeAc.show()
        self.close()
        

    def satinAl(self):

        selected_row = self.bisikletform.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Hata", "Bir bisiklet seçiniz.")
            return

        bisiklet_fiyati = int(self.bisikletform.tableWidget.item(selected_row, 3).text()) 
        musteri_no, ok = QInputDialog.getText(self, "Müşteri No", "Müşteri numaranızı giriniz:")

        if not ok or not musteri_no.isdigit():
            QMessageBox.warning(self, "Hata", "Geçersiz müşteri numarası.")
            return

        bakiyeler = self.bakiyeYukle()

        stok = int(self.bisikletform.tableWidget.item(selected_row, 6).text())
        if stok <= 0:
            QMessageBox.warning(self, "Stokta Yok", "Bu ürün stokta bulunmamaktadır.")
            return

        if musteri_no in bakiyeler and bakiyeler[musteri_no] >= bisiklet_fiyati:
            bakiyeler[musteri_no] -= bisiklet_fiyati
            stok -= 1
            self.bisikletform.tableWidget.item(selected_row, 6).setText(str(stok))
        
            if stok == 0:
                self.bisikletform.tableWidget.item(selected_row, 7).setText("Stokta Yok")
        
            self.stokkayit()  
            self.bakiyeKaydet(bakiyeler)  
        
            QMessageBox.information(self, "Başarılı", f"Bakiyenizden {bisiklet_fiyati} TL düşüldü. Kalan bakiye: {bakiyeler[musteri_no]} TL")
        else:
            QMessageBox.warning(self, "Yetersiz Bakiye", "Bakiyeniz bu işlem için yetersiz.")



                
    def stokkayit(self):
        with open("stoklar.txt", "w") as file:
            for row in range(self.bisikletform.tableWidget.rowCount()):
                item = self.bisikletform.tableWidget.item(row, 6)
                if item:
                    stock = item.text()
                else:
                    stock = "0"
                status = self.bisikletform.tableWidget.item(row, 7).text()
                file.write(f"{stock},{status}\n")


    def stokyukle(self):
        try:
            with open("stoklar.txt", "r") as file:
                for row, line in enumerate(file.readlines()):
                    stock, status = line.strip().split(',')
                    if self.bisikletform.tableWidget.rowCount() > row:
                        self.bisikletform.tableWidget.item(row, 6).setText(stock)
                        self.bisikletform.tableWidget.item(row, 7).setText(status)
        except FileNotFoundError:
            print("Stok bilgisi dosyası bulunamadı.")



    def bakiyeYukle(self):
        bakiyeler = {}
        try:
            with open("bakiyeler.txt", "r") as file:
                for line in file:
                    no, bakiye = line.strip().split(',')
                    bakiyeler[no] = int(bakiye)
        except FileNotFoundError:
            print("Bakiye dosyası bulunamadı.")
        return bakiyeler

    def bakiyeKaydet(self, bakiyeler):
        with open("bakiyeler.txt", "w") as file:
            for no, bakiye in bakiyeler.items():
                file.write(f"{no},{bakiye}\n")
