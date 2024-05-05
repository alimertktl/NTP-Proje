from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Randevu_iptal import Ui_MainWindow

class Randevuİptal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.randevuİptalSayfa = Ui_MainWindow()
        self.randevuİptalSayfa.setupUi(self)
        self.kiralamalariYukle()
        self.randevuİptalSayfa.pushButton_2.clicked.connect(self.geridogru)
        self.randevuİptalSayfa.pushButton.clicked.connect(self.kiralamayiIptalEt)
        self.listele()


    def listele(self):
        header = self.randevuİptalSayfa.tableWidget.horizontalHeader() 
        for i in range(self.randevuİptalSayfa.tableWidget.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setDefaultSectionSize(115)



        

    def kiralamalariYukle(self):
        try:
            with open('kullanıcılar.txt', 'r', encoding='utf-8') as file:
                kiralamalar = [line.strip().split(',') for line in file.readlines()]

            self.randevuİptalSayfa.tableWidget.setRowCount(len(kiralamalar))
            for i, kiralama in enumerate(kiralamalar):
                for j, item in enumerate(kiralama):
                    self.randevuİptalSayfa.tableWidget.setItem(i, j, QTableWidgetItem(item))
        except FileNotFoundError:
            print("kullanıcılar.txt dosyası bulunamadı.")
        except UnicodeDecodeError:
            print("Dosya UTF-8 olarak okunamadı, başka bir kodlama deneyin.")



    def kiralamayiIptalEt(self):
        selectedRows = self.randevuİptalSayfa.tableWidget.selectionModel().selectedRows()
        if not selectedRows:
            QMessageBox.warning(self, "Uyarı", "Lütfen iptal etmek istediğiniz saha randevunuzu seçin.")
            return
    
        try:
            with open('kullanıcılar.txt', 'r', encoding='utf-8') as file:
                kiralamalar = [line.strip().split(',') for line in file.readlines()]
    
            guncellenmis_kiralamalar = [kiralama for i, kiralama in enumerate(kiralamalar) if i not in [row.row() for row in selectedRows]]
        
            with open('kullanıcılar.txt', 'w', encoding='utf-8') as file:
                for kiralama in guncellenmis_kiralamalar:
                    file.write(','.join(kiralama) + '\n')
        
            for selectedRow in sorted(selectedRows, reverse=True):
                self.randevuİptalSayfa.tableWidget.removeRow(selectedRow.row())

            QMessageBox.information(self, "Başarılı", "Seçilen randevu iptal edildi.")

            self.kiralamalariYukle()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Bir hata oluştu: {str(e)}")
            return



    def sabit(self):
        from randevu_home_kodu import HomePage
        self.homesayfa = HomePage()

    def geridogru(self):
        self.sabit()
        self.homesayfa.show()
        self.close()



