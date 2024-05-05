from PyQt5.QtWidgets import *
from anasayfa import Ui_Form

import sqlite3

class Anasayfa(QWidget):
    def __init__(self, kadi):
        super().__init__()
        self.kadi = kadi

        self.anasayfaform = Ui_Form()
        self.anasayfaform.setupUi(self)

        self.tablo()

        self.anasayfaform.pushButton_guncelle.clicked.connect(self.guncelle)
        self.anasayfaform.pushButton_sipariset.clicked.connect(self.siparis)            
        self.anasayfaform.pushButton_yemekekle.clicked.connect(self.ekle)
        self.anasayfaform.pushButton_cikis.clicked.connect(self.cikis)

    def tablo(self):
        self.conn = sqlite3.connect("Veritabani.db")
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT * FROM menu")
        menu_rows = self.cur.fetchall()

        self.cur.execute("SELECT * FROM siparisler".format(self.kadi))
        siparis_rows = self.cur.fetchall()

        self.anasayfaform.tableWidget_siparis.setRowCount(len(siparis_rows))

        self.cur.execute("SELECT * FROM {}_siparis_gecmisi".format(self.kadi))
        gecmis_rows = self.cur.fetchall()

        self.anasayfaform.tableWidget_gecmis.setRowCount(len(gecmis_rows))

        for i, row in enumerate(siparis_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.anasayfaform.tableWidget_siparis.setItem(i, j, item)

        self.anasayfaform.tableWidget_menu.setRowCount(len(menu_rows))
    
        for i, row in enumerate(menu_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.anasayfaform.tableWidget_menu.setItem(i, j, item)
        
        for i, row in enumerate(gecmis_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.anasayfaform.tableWidget_gecmis.setItem(i, j, item)

        self.menu_rows = menu_rows

        self.anasayfaform.tableWidget_menu.setColumnWidth(0, 306)  # Sütun büyüklüklerini ayarlar.
        self.anasayfaform.tableWidget_menu.setColumnWidth(1, 75)  
        self.anasayfaform.tableWidget_menu.setColumnWidth(2, 75)
        self.anasayfaform.tableWidget_menu.verticalHeader().setDefaultSectionSize(30)

        self.anasayfaform.tableWidget_siparis.setColumnWidth(0, 65)  # Sütun büyüklüklerini ayarlar.
        self.anasayfaform.tableWidget_siparis.setColumnWidth(1, 120)  
        self.anasayfaform.tableWidget_siparis.setColumnWidth(2, 120)
        self.anasayfaform.tableWidget_siparis.setColumnWidth(3, 151)
        self.anasayfaform.tableWidget_siparis.verticalHeader().setDefaultSectionSize(30)

        self.anasayfaform.tableWidget_gecmis.setColumnWidth(0, 65)  # Sütun büyüklüklerini ayarlar.
        self.anasayfaform.tableWidget_gecmis.setColumnWidth(1, 120)  
        self.anasayfaform.tableWidget_gecmis.setColumnWidth(2, 120)
        self.anasayfaform.tableWidget_gecmis.setColumnWidth(3, 151)
        self.anasayfaform.tableWidget_gecmis.verticalHeader().setDefaultSectionSize(30)

    def guncelle(self):
        conn = sqlite3.connect("Veritabani.db")
        cursor = conn.cursor()

        selected_row = self.anasayfaform.tableWidget_menu.currentRow()
        if selected_row != -1:
            stokmiktar, ok = QInputDialog.getInt(self, "Stok Güncelle", "Stok Miktarını Giriniz:")
            if ok:
                ürünad = self.menu_rows[selected_row][0]

                cursor.execute("UPDATE menu SET stok = ? WHERE ad = ?", (stokmiktar, ürünad))
                conn.commit()
                conn.close()

                self.menu_rows[selected_row] = (self.menu_rows[selected_row][0], self.menu_rows[selected_row][1], stokmiktar)
                self.anasayfaform.tableWidget_menu.setItem(selected_row, 2, QTableWidgetItem(str(stokmiktar)))
                QMessageBox.information(self, "Başarılı", "Stok başarıyla güncellendi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir ürün seçin.")

    def siparis(self):
        selected_row = self.anasayfaform.tableWidget_menu.currentRow()
        
    
        if selected_row != -1:
            urun_ad = self.menu_rows[selected_row][0]
            stok_miktar = int(self.menu_rows[selected_row][2])
    
            siparis_miktar, ok = QInputDialog.getInt(self, "Sipariş Miktarı", f"{urun_ad} için sipariş miktarını giriniz:", min=1, max=stok_miktar)
            
            if ok:               
                    conn = sqlite3.connect("Veritabani.db")
                    cursor = conn.cursor()
                
                    try:
                        # Kullanıcı adını ve adresini çek
                        cursor.execute("SELECT kullaniciadi, adres FROM kullanicilar WHERE kullaniciadi = ?", (self.kadi,))
                        kullanici_bilgisi = cursor.fetchone()
                        musteri_ad = kullanici_bilgisi[0]
                        adres = kullanici_bilgisi[1]
                
                        cursor.execute("INSERT INTO siparisler (icerik, musteriad, adres) VALUES (?, ?, ?)", (f"{siparis_miktar} {urun_ad}", musteri_ad, adres))
                        conn.commit()

                        cursor.execute("SELECT last_insert_rowid()")
                        siparis_no = cursor.fetchone()[0]

                        cursor.execute("INSERT INTO {}_siparis_gecmisi (siparisno, icerik, ad, adres) VALUES (?, ?, ?, ?)".format(self.kadi), (siparis_no, f"{siparis_miktar} {urun_ad}", musteri_ad, adres))
                        conn.commit()                        
                
                        # Stok miktarını güncelle
                        cursor.execute("UPDATE menu SET stok = stok - ? WHERE ad = ?", (siparis_miktar, urun_ad))
                        conn.commit()
                
                        QMessageBox.information(self, "Başarılı", "Sipariş başarıyla oluşturuldu.")
                    except sqlite3.Error as e:
                        QMessageBox.warning(self, "Hata", f"Veritabanı hatası: {e}")
            
                    conn.close()
                    self.tablo()  # Tabloyu güncellemek için
        
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir ürün seçin.")



    def eklesayfasıac(self,kadi):
        self.kadi = kadi
        from ekle_page import Eklesayfa
        self.eklesayfaac = Eklesayfa(kadi)
        self.eklesayfaac.show()

    def ekle(self):
        self.eklesayfasıac(self.kadi)
        self.close()

    def cikisyap(self):
        from giris_page import GirisSayfası
        self.cikis = GirisSayfası()
        self.cikis.show()

    def cikis(self):
        self.cikisyap()
        self.close()
