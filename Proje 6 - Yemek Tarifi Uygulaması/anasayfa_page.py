import sqlite3
import sys
from PyQt5.QtWidgets import *
from anasayfa import Ui_Form

class Anasayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.anasayfaform = Ui_Form()
        self.anasayfaform.setupUi(self)

        self.conn = sqlite3.connect("Tarifler.db")
        self.cur = self.conn.cursor()
        self.tablo()

        self.anasayfaform.lineEdit_arama.textChanged.connect(self.aramafiltre)
        self.anasayfaform.pushButton_Ekle.clicked.connect(self.ekle)
        self.anasayfaform.pushButton_cikis.clicked.connect(self.cikis)
        self.anasayfaform.pushButton_like.clicked.connect(self.like)
        self.anasayfaform.pushButton_dislike.clicked.connect(self.dislike)
 
 
    def tablo(self):
        # Veritabanından veri çekmek için kullanılır.
        self.cur.execute("SELECT * FROM Tarif")
        rows = self.cur.fetchall()

        self.anasayfaform.tableWidget.setRowCount(len(rows))
        

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.anasayfaform.tableWidget.setItem(i, j, item)

        self.anasayfaform.tableWidget.setColumnWidth(0, 100)  # Sütun büyüklüklerini ayarlar.
        self.anasayfaform.tableWidget.setColumnWidth(1, 172)  
        self.anasayfaform.tableWidget.setColumnWidth(2, 430)
        self.anasayfaform.tableWidget.setColumnWidth(3, 50)
        self.anasayfaform.tableWidget.verticalHeader().setDefaultSectionSize(400)





    def aramafiltre(self):
        filtre_text = self.anasayfaform.lineEdit_arama.text()  
        self.cur.execute("SELECT * FROM Tarif WHERE yemekadı LIKE ?", ('%' + filtre_text + '%',))
        filtered_rows = self.cur.fetchall()

        self.anasayfaform.tableWidget.clearContents()
        self.anasayfaform.tableWidget.setRowCount(len(filtered_rows))
        for i, row in enumerate(filtered_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.anasayfaform.tableWidget.setItem(i, j, item)


    verilen_puanlar = []
    def like(self):
        satir = self.anasayfaform.tableWidget.selectionModel().selectedRows()
        if satir:
            selected_row = satir[0].row()
            yemek_adi = self.anasayfaform.tableWidget.item(selected_row, 0).text()

            
            if yemek_adi not in self.verilen_puanlar:
                self.cur.execute("UPDATE Tarif SET puan = puan + 1 WHERE yemekadı = ?", (yemek_adi,))
                self.conn.commit()
                self.verilen_puanlar.append(yemek_adi)

                self.tablo() 
            else:
                QMessageBox.warning(self, "Uyarı", "Bu yemeğe zaten puan verdiniz.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir yemek seçin.")



    def dislike(self):
        satir = self.anasayfaform.tableWidget.selectionModel().selectedRows()
        if satir:
            selected_row = satir[0].row()
            yemek_adi = self.anasayfaform.tableWidget.item(selected_row, 0).text()

            
            if yemek_adi not in self.verilen_puanlar:
                self.cur.execute("UPDATE Tarif SET puan = puan - 1 WHERE yemekadı = ?", (yemek_adi,))
                self.conn.commit()
                self.verilen_puanlar.append(yemek_adi)

                self.tablo() 
            else:
                QMessageBox.warning(self, "Uyarı", "Bu yemeğe zaten puan verdiniz.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir yemek seçin.")


    def sabit(self):
        from tarif_page import Tarif
        self.tarifsayfaac = Tarif() 
        self.tarifsayfaac.show()
 
    def sabit2(self):
        from giriş_page import GirişSayfası
        self.girissayfaac = GirişSayfası()
        self.girissayfaac.show()

    def ekle(self):
        self.sabit()
        self.hide()

    def cikis(self):
        self.sabit2()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Anasayfa()
    window.show()
    sys.exit(app.exec_())
