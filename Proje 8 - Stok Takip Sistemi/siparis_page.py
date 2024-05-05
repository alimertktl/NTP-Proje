from PyQt5.QtWidgets import *
from siparis import Ui_Form
import sqlite3
import sys

class SiparisSayfası(QWidget):
    def __init__(self):
        super().__init__()

        self.siparisform = Ui_Form()
        self.siparisform.setupUi(self)
        
        self.uruntablosu()

        self.siparisform.pushButton_Geri.clicked.connect(self.geri)
        self.siparisform.pushButton_Siparis.clicked.connect(self.siparis)

    def uruntablosu(self):
        
        conn = sqlite3.connect("Bilgiler.db")
        cursor = conn.cursor()

        
        cursor.execute("SELECT ürünno, ürünad, stokmiktar FROM urunler")
        self.urun_rows = cursor.fetchall()

        self.siparisform.tableWidget_Urun.setRowCount(len(self.urun_rows))
        self.siparisform.tableWidget_Urun.setColumnCount(len(self.urun_rows[0])) 

        for i, row in enumerate(self.urun_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.siparisform.tableWidget_Urun.setItem(i, j, item)

        self.siparisform.tableWidget_Urun.setColumnWidth(0, 54)  
        self.siparisform.tableWidget_Urun.setColumnWidth(1, 180)  
        self.siparisform.tableWidget_Urun.setColumnWidth(2, 76)
        self.siparisform.tableWidget_Urun.verticalHeader().setDefaultSectionSize(35)
 

        conn.close()

    def siparis(self):
        selected_row = self.siparisform.tableWidget_Urun.currentRow()
    
        if selected_row != -1:
            urun_no = self.urun_rows[selected_row][0]
            urun_ad = self.urun_rows[selected_row][1]
            stok_miktar = int(self.urun_rows[selected_row][2])
        
            siparis_miktar, ok = QInputDialog.getInt(self, "Sipariş Miktarı", f"{urun_ad} için sipariş miktarını giriniz:", min=1, max=stok_miktar)
        
            if ok:
                siparis_detay, ok = QInputDialog.getText(self, "Sipariş Detayı", f"{urun_ad} için lütfen adınızı giriniz:")
            
                if ok:
                    siparis_aciklama = f"{siparis_detay}"
                
                    conn = sqlite3.connect("Bilgiler.db")
                    cursor = conn.cursor()
                
                    try:
                        cursor.execute("INSERT INTO siparisler (siparisurun, siparismiktar, siparisacıklama) VALUES (?, ?, ?)", (urun_ad, siparis_miktar, siparis_aciklama))
                        conn.commit()
                    
                        # Stok miktarını güncelle
                        cursor.execute("UPDATE urunler SET stokmiktar = stokmiktar - ? WHERE ürünno = ?", (siparis_miktar, urun_no))
                        conn.commit()
                    
                        QMessageBox.information(self, "Başarılı", "Sipariş başarıyla oluşturuldu.")
                    except sqlite3.Error as e:
                        QMessageBox.warning(self, "Hata", f"Veritabanı hatası: {e}")
                
                    conn.close()
                    self.uruntablosu()  # Tabloyu güncellemek için
            
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir ürün seçin.")



    def sabit(self):
        from giris_page import GirisSayfası
        self.girissayfasıac = GirisSayfası() 
        self.girissayfasıac.show()

    def geri(self):
        self.sabit()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SiparisSayfası()
    window.show()
    sys.exit(app.exec_())


