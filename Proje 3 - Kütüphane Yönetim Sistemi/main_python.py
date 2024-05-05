from PyQt5.QtWidgets import *
from kutuphane_python import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.qtTasarim=Ui_MainWindow()
        self.qtTasarim.setupUi(self) 
        self.qtTasarim.pushButton_2.clicked.connect(self.OduncAlTikla) 
        self.verileriYukle()  # Başlangıçta verileri yükle

        self.listem = self.listeoku()
        self.tabloyuGuncelle() 
   
    def OduncAlTikla(self):
        satir = self.qtTasarim.tableWidget.selectionModel().selectedRows()
        if satir:
            selectedRow = satir[0].row()
            kitapDurum = self.qtTasarim.tableWidget.item(selectedRow, 2)
            kitaplik = kitapDurum.text() if kitapDurum else ""
            
            if kitaplik == "Mevcut":
                kadi = self.qtTasarim.lineEdit.text()
                soyadi = self.qtTasarim.lineEdit_2.text()
                gsm = self.qtTasarim.lineEdit_3.text()
                kitapadi = self.qtTasarim.tableWidget.item(selectedRow, 0).text()
                ysoyadi = self.qtTasarim.tableWidget.item(selectedRow, 1).text()

                if kadi and soyadi and gsm:  
                    if not self.kullaniciInfo(kadi, soyadi, gsm, kitapadi, ysoyadi):
                        self.listem.append((kadi, soyadi, gsm, kitapadi, ysoyadi, "Alındı"))
                        self.veriDepo(self.listem)
                        self.verileriYukle()  # Verileri yeniden yükle

                        self.qtTasarim.tableWidget.setItem(selectedRow, 2, QTableWidgetItem("Alındı"))
                        QMessageBox.information(self, "Başarılı", "Kullanıcı ve kitap bilgileri kaydedildi, Alındı.")
                    else:
                        QMessageBox.warning(self, "Uyarı", "Bu kullanıcı ve/veya kitap zaten kaydedilmiş.")
                else:
                    QMessageBox.warning(self, "Uyarı", "Lütfen zorunlu alanları doldurun.")
            else:
                QMessageBox.warning(self, "Uyarı", "Bu kitap zaten alınmış veya mevcut değil.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen alınacak bir kitap seçin.")


    def kullaniciInfo(self, kadi, soyadi, gsm, kitapadi, ysoyadi):
        for item in self.listem:
            if item[:3] == (kadi, soyadi, gsm) or item[3:5] == (kitapadi, ysoyadi):
                return True
        return False

    def veriDepo(self, listem):
        with open('kutuphane.txt', 'w') as file:
            for info in listem:
                file.write(",".join(info) + "\n")

    def listeoku(self):
        try:
            with open('kutuphane.txt', 'r') as file:
                return [tuple(line.strip().split(',')) for line in file]
        except FileNotFoundError:
            return []
    def tabloyuGuncelle(self):
       
        for info in self.listem:
            if len(info) >= 6:  
                kitapadi, ysoyadi, durum = info[3], info[4], info[5]
                rowCount = self.qtTasarim.tableWidget.rowCount()
                for row in range(rowCount):
                    if self.qtTasarim.tableWidget.item(row, 0).text() == kitapadi and \
                       self.qtTasarim.tableWidget.item(row, 1).text() == ysoyadi:
                       self.qtTasarim.tableWidget.setItem(row, 2, QTableWidgetItem(durum))


    def verileriYukle(self):
        self.qtTasarim.tableWidget_2 .clearContents()  # Mevcut verileri temizle
        self.qtTasarim.tableWidget_2.setRowCount(0)  # Satır sayısını sıfırla
        veriler = self.listeoku()  # Verileri dosyadan oku veya başka bir kaynaktan al

        for satirIndeksi, satirVerisi in enumerate(veriler):
            self.qtTasarim.tableWidget_2.insertRow(satirIndeksi)
            for sutunIndeksi, sutunVerisi in enumerate(satirVerisi):
                self.qtTasarim.tableWidget_2.setItem(satirIndeksi, sutunIndeksi,QTableWidgetItem(str(sutunVerisi)))




if __name__ == "__main__":
    app = QApplication([])
    pencere = Main()
    pencere.show() 
    app.exec_() 