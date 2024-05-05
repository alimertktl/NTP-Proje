from PyQt5.QtWidgets import *
from kiralama import Ui_MainWindow

class KiralamaPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kiralamaform = Ui_MainWindow()
        self.kiralamaform.setupUi(self)
        self.kiralamaform.pushButton.clicked.connect(self.calistir)
        self.listem = self.listeoku()
        self.tabloyuGuncelle() 
        self.kiralamaform.pushButton_2.clicked.connect(self.geridonus)

    def sabit(self):
        from home_Page import HomePage
        self.homeAc = HomePage() 
    def geridonus(self):
        self.sabit()
        self.homeAc.show()
        self.close()
        

    def calistir(self):
        satir = self.kiralamaform.tableWidget.selectionModel().selectedRows()
        if satir:
            selectedRow = satir[0].row()
            aracDurumuItem = self.kiralamaform.tableWidget.item(selectedRow, 2)
            aracDurumu = aracDurumuItem.text() 
            
            if aracDurumu == "Mevcut":
                kadi = self.kiralamaform.lineEdit.text()
                soyadi = self.kiralamaform.lineEdit_2.text()
                eposta = self.kiralamaform.lineEdit_3.text()
                marka = self.kiralamaform.tableWidget.item(selectedRow, 0).text()
                model = self.kiralamaform.tableWidget.item(selectedRow, 1).text()

                if kadi and soyadi and eposta:  
                    if not self.kullaniciInfo(kadi, soyadi, eposta, marka, model):
                        self.listem.append((kadi, soyadi, eposta, marka, model, "Kiralandı"))
                        self.veriDepo(self.listem)
                        self.kiralamaform.tableWidget.setItem(selectedRow, 2, QTableWidgetItem("Kiralandı"))
                        QMessageBox.information(self, "Başarılı", "Kullanıcı ve araç bilgileri kaydedildi, araç kiralandı.")
                    else:
                        QMessageBox.warning(self, "Uyarı", "Bu kullanıcı ve/veya araç zaten kaydedilmiş.")
                else:
                    QMessageBox.warning(self, "Uyarı", "Lütfen zorunlu alanları doldurun.")
            else:
                QMessageBox.warning(self, "Uyarı", "Bu araç zaten kiralanmış veya mevcut değil.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen kiralanacak bir araç seçin.")

    def kullaniciInfo(self, kadi, soyadi, eposta, marka, model):
        for item in self.listem:
            if item[:3] == (kadi, soyadi, eposta) or item[3:5] == (marka, model):
                return True
        return False

    def veriDepo(self, listem):
        with open('userinfo.txt', 'w') as file:
            for info in listem:
                file.write(",".join(info) + "\n")

    def listeoku(self):
        try:
            with open('userinfo.txt', 'r') as file:
                return [tuple(line.strip().split(',')) for line in file]
        except FileNotFoundError:
            return []
    
    def tabloyuGuncelle(self):
       
        for info in self.listem:
            if len(info) >= 6:  
                marka, model, durum = info[3], info[4], info[5]
                rowCount = self.kiralamaform.tableWidget.rowCount()
                for row in range(rowCount):
                    if self.kiralamaform.tableWidget.item(row, 0).text() == marka and \
                       self.kiralamaform.tableWidget.item(row, 1).text() == model:
                        self.kiralamaform.tableWidget.setItem(row, 2, QTableWidgetItem(durum))


