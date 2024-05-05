from PyQt5.QtWidgets import *
from yönetim import Ui_Form
import sqlite3
import sys



class YönetimSayfası(QWidget):
    def __init__(self):
        super().__init__()

        self.yönetimform = Ui_Form()
        self.yönetimform.setupUi(self)

        self.uruntablosu()
        self.siparistablosu()



        self.yönetimform.pushButton_Geri.clicked.connect(self.geri)
        self.yönetimform.pushButton_Sil.clicked.connect(self.urunsil)
        self.yönetimform.pushButton_Iptal.clicked.connect(self.siparissil)
        self.yönetimform.pushButton_Guncelle.clicked.connect(self.guncelle)
        self.yönetimform.pushButton_Ekle.clicked.connect(self.ekle)


    def uruntablosu(self):
        
        conn = sqlite3.connect("Bilgiler.db")
        cursor = conn.cursor()

        
        cursor.execute("SELECT ürünno, ürünad, stokmiktar FROM urunler")
        self.urun_rows = cursor.fetchall()

        self.yönetimform.tableWidget_Urun.setRowCount(len(self.urun_rows))
        self.yönetimform.tableWidget_Urun.setColumnCount(len(self.urun_rows[0])) 

        for i, row in enumerate(self.urun_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.yönetimform.tableWidget_Urun.setItem(i, j, item)

        self.yönetimform.tableWidget_Urun.setColumnWidth(0, 50)  
        self.yönetimform.tableWidget_Urun.setColumnWidth(1, 190)  
        self.yönetimform.tableWidget_Urun.setColumnWidth(2, 70)
        self.yönetimform.tableWidget_Urun.verticalHeader().setDefaultSectionSize(35)
 

        conn.close()

    def siparistablosu(self):
        
        conn = sqlite3.connect("Bilgiler.db")
        cursor = conn.cursor()

        
        cursor.execute("SELECT * FROM siparisler")
        self.siparis_rows = cursor.fetchall()

        self.yönetimform.tableWidget_Siparis.setRowCount(len(self.siparis_rows))
        self.yönetimform.tableWidget_Siparis.setColumnCount(len(self.siparis_rows[0])) 

        for i, row in enumerate(self.siparis_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.yönetimform.tableWidget_Siparis.setItem(i, j, item)

        self.yönetimform.tableWidget_Siparis.setColumnWidth(0, 65)  
        self.yönetimform.tableWidget_Siparis.setColumnWidth(1, 90)
        self.yönetimform.tableWidget_Siparis.setColumnWidth(2, 45)
        self.yönetimform.tableWidget_Siparis.setColumnWidth(3, 117)
        self.yönetimform.tableWidget_Siparis.verticalHeader().setDefaultSectionSize(35)

        conn.close()

    def urunsil(self):
        selected_row = self.yönetimform.tableWidget_Urun.currentRow()
        if selected_row != -1:  # Eğer bir satır seçildiyse
            ürünno = self.urun_rows[selected_row][0]  # Seçilen satırdaki ürün numarasını al

            conn = sqlite3.connect("Bilgiler.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM urunler WHERE ürünno = ?", (ürünno,))
            conn.commit()
            conn.close()

            self.urun_rows.pop(selected_row)  # Veri listesinden seçilen satırı sil
            self.yönetimform.tableWidget_Urun.removeRow(selected_row)  # Tablodan seçilen satırı sil
            QMessageBox.information(self, "Başarılı", "Ürün başarıyla silindi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir ürün seçin.")

    def siparissil(self):
        selected_row = self.yönetimform.tableWidget_Siparis.currentRow()
        if selected_row != -1:  # Eğer bir satır seçildiyse
            siparisno = self.siparis_rows[selected_row][0]  # Seçilen satırdaki sipariş numarasını al

            conn = sqlite3.connect("Bilgiler.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM siparisler WHERE siparisno = ?", (siparisno,))
            conn.commit()
            conn.close()

            self.siparis_rows.pop(selected_row)  # Veri listesinden seçilen satırı sil
            self.yönetimform.tableWidget_Siparis.removeRow(selected_row)  # Tablodan seçilen satırı sil
            QMessageBox.information(self, "Başarılı", "Sipariş başarıyla silindi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir sipariş seçin.")

    def guncelle(self):
        selected_row = self.yönetimform.tableWidget_Urun.currentRow()
        if selected_row != -1:
            stokmiktar, ok = QInputDialog.getInt(self, "Stok Güncelle", "Stok Miktarını Giriniz:")
            if ok:
                ürünno = self.urun_rows[selected_row][0]

                conn = sqlite3.connect("Bilgiler.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE urunler SET stokmiktar = ? WHERE ürünno = ?", (stokmiktar, ürünno))
                conn.commit()
                conn.close()

                self.urun_rows[selected_row] = (self.urun_rows[selected_row][0], self.urun_rows[selected_row][1], stokmiktar)
                self.yönetimform.tableWidget_Urun.setItem(selected_row, 2, QTableWidgetItem(str(stokmiktar)))
                QMessageBox.information(self, "Başarılı", "Stok başarıyla güncellendi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir ürün seçin.")



    def sabit(self):
        from giris_page import GirisSayfası
        self.girissayfasıac = GirisSayfası() 
        self.girissayfasıac.show()

    def geri(self):
        self.sabit()
        self.close()

    def sabit2(self):
        from urunekle_page import UrunekleSayfası
        self.urunsayfaac = UrunekleSayfası() 
        self.urunsayfaac.show()

    def ekle(self):
        self.sabit2()
        self.close()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YönetimSayfası()
    window.show()
    sys.exit(app.exec_())