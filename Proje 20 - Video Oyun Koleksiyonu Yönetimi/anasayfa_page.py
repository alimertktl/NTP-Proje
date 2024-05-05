from PyQt5.QtWidgets import *
from anasayfa import Ui_Form
from PyQt5.QtGui import QColor
import random

import sqlite3

class Anasayfa(QWidget):
    def __init__(self, kadi):
        super().__init__()
        self.kadi = kadi

        self.anasayfaform = Ui_Form()
        self.anasayfaform.setupUi(self)

        self.tablo()


        self.anasayfaform.pushButton_koleksiyonekle.clicked.connect(self.koleksiyonekle)
        self.anasayfaform.pushButton_favoriekle.clicked.connect(self.favoriekle)
        self.anasayfaform.pushButton_favorisil.clicked.connect(self.favorisil)
        self.anasayfaform.pushButton_begen.clicked.connect(self.begen)
        self.anasayfaform.pushButton_begenme.clicked.connect(self.begenme)
        self.anasayfaform.pushButton_onerial.clicked.connect(self.onerial)
        self.anasayfaform.lineEdit_arama.textChanged.connect(self.aramafiltre)
        self.anasayfaform.pushButton_oyunekle.clicked.connect(self.ekle)
        self.anasayfaform.pushButton_cikis.clicked.connect(self.cikis)

    def koleksiyonekle(self):
        selected_row_index = self.anasayfaform.tableWidget_oyun.currentRow()

        if selected_row_index == -1:  # Eğer herhangi bir oyun seçilmemişse
            QMessageBox.warning(self, 'Uyarı', 'Koleksiyonunuza eklemek istediğiniz bir oyun seçiniz.')
            return

        selected_table_widget = self.anasayfaform.tableWidget_oyun
        selected_row = [selected_table_widget.item(selected_row_index, column).text() 
                        for column in range(selected_table_widget.columnCount())]

        # Seçilen oyunu koleksiyon tablosuna ekleyin
        self.cur.execute("SELECT * FROM {}_koleksiyon_tablosu WHERE ad=?".format(self.kadi), (selected_row[0],))
        existing_row = self.cur.fetchone()
        if existing_row:
            QMessageBox.warning(self, 'Uyarı', 'Bu oyun zaten koleksiyonunuzda bulunmaktadır.')
        else:
            self.cur.execute("INSERT INTO {}_koleksiyon_tablosu (ad, tur, yapimci, platform) VALUES (?, ?, ?, ?)".format(self.kadi), selected_row[0:4])
            self.conn.commit()
            QMessageBox.information(self, 'Bilgi', 'Oyun başarıyla koleksiyonunuza eklendi.')

        # Tabloyu yenile
        self.tablo()

    def favoriekle(self):
        selected_row_index = self.anasayfaform.tableWidget_koleksiyon.currentRow()

        if selected_row_index == -1:  # Eğer herhangi bir oyun seçilmemişse
            QMessageBox.warning(self, 'Uyarı', 'Favori listenize eklemek için bir oyun seçiniz.')
            return

        selected_table_widget = self.anasayfaform.tableWidget_koleksiyon
        selected_row = [selected_table_widget.item(selected_row_index, column).text() 
                        for column in range(selected_table_widget.columnCount())]

        # Seçilen oyunu koleksiyon tablosuna ekleyin
        self.cur.execute("SELECT * FROM {}_favori_tablosu WHERE ad=?".format(self.kadi), (selected_row[0],))
        existing_row = self.cur.fetchone()
        if existing_row:
            QMessageBox.warning(self, 'Uyarı', 'Bu oyun zaten favori listenizde bulunmaktadır.')
        else:
            self.cur.execute("INSERT INTO {}_favori_tablosu (ad, tur, yapimci, platform) VALUES (?, ?, ?, ?)".format(self.kadi), selected_row[0:4])
            self.conn.commit()
            QMessageBox.information(self, 'Bilgi', 'Oyun başarıyla favori listenize eklendi.')

        # Tabloyu yenile
        self.tablo()

    def favorisil(self):
        selected_row_index = self.anasayfaform.tableWidget_favori.currentRow()

        if selected_row_index == -1:  # Eğer herhangi bir oyun seçilmemişse
            QMessageBox.warning(self, 'Uyarı', 'Favori listenizden silmek için bir oyun seçin.')
            return

        selected_table_widget = self.anasayfaform.tableWidget_favori
        selected_row = [selected_table_widget.item(selected_row_index, column).text() 
                        for column in range(selected_table_widget.columnCount())]

        # Seçilen oyunu favori tablosundan sil
        self.cur.execute("DELETE FROM {}_favori_tablosu WHERE ad=?".format(self.kadi), (selected_row[0],))
        self.conn.commit()
        QMessageBox.warning(self, 'Bilgi', 'Oyun başarıyla favori listenizden silindi.')

        # Tabloyu yenile
        self.tablo()
    
    def begen(self):
        selected_rows = self.anasayfaform.tableWidget_oyun.selectionModel().selectedRows()
        if selected_rows:
            selected_row = selected_rows[0].row()
            oyun_adi = self.anasayfaform.tableWidget_oyun.item(selected_row, 0).text()

            # Kullanıcının daha önce oy kullandığını kontrol et
            self.cur.execute("SELECT * FROM {}_puan_tablosu WHERE ad = ?".format(self.kadi), (oyun_adi,))
            existing_vote = self.cur.fetchone()
            if existing_vote is not None:
                QMessageBox.warning(self, "Uyarı", "Bu oyuna zaten oy kullandınız.")
            else:
                # Oyunun puanını 1 artır ve puan tablosuna ekle
                self.cur.execute("UPDATE oyunlar SET puan = puan + 1 WHERE ad = ?", (oyun_adi,))
                self.cur.execute("INSERT INTO {}_puan_tablosu (ad) VALUES (?)".format(self.kadi), (oyun_adi,))
                self.conn.commit()

                self.tablo()  # Tabloyu yenile
                QMessageBox.information(self, "Bilgi", "Oyun için oy kullandınız.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir oyun seçin.")

    def begenme(self):
        selected_rows = self.anasayfaform.tableWidget_oyun.selectionModel().selectedRows()
        if selected_rows:
            selected_row = selected_rows[0].row()
            oyun_adi = self.anasayfaform.tableWidget_oyun.item(selected_row, 0).text()

            # Kullanıcının daha önce oy kullandığını kontrol et
            self.cur.execute("SELECT * FROM {}_puan_tablosu WHERE ad = ?".format(self.kadi), (oyun_adi,))
            existing_vote = self.cur.fetchone()
            if existing_vote is not None:
                QMessageBox.warning(self, "Uyarı", "Bu oyuna zaten oy kullandınız.")
            else:
                # Oyunun puanını 1 artır ve puan tablosuna ekle
                self.cur.execute("UPDATE oyunlar SET puan = puan - 1 WHERE ad = ?", (oyun_adi,))
                self.cur.execute("INSERT INTO {}_puan_tablosu (ad) VALUES (?)".format(self.kadi), (oyun_adi,))
                self.conn.commit()

                self.tablo()  # Tabloyu yenile
                QMessageBox.information(self, "Bilgi", "Oyun için oy kullandınız.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir oyun seçin.")

    def onerial(self):
        self.cur.execute("SELECT ad FROM oyunlar")
        oyunlar = self.cur.fetchall()

        if oyunlar:
            secilenoyun = random.choice(oyunlar)[0]
            QMessageBox.information(self, 'Oyun Önerisi', f"Siz için önerilen oyun: {secilenoyun}")
        else:
            QMessageBox.warning(self, 'Uyarı', 'Veritabanında oyun bulunmamaktadır.')

    def aramafiltre(self):
        filtre_text = self.anasayfaform.lineEdit_arama.text()  
        self.cur.execute("SELECT * FROM oyunlar WHERE ad LIKE ?", ('%' + filtre_text + '%',))
        filtered_rows = self.cur.fetchall()

        self.anasayfaform.tableWidget_oyun.clearContents()
        self.anasayfaform.tableWidget_oyun.setRowCount(len(filtered_rows))
        for i, row in enumerate(filtered_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor("white"))
                self.anasayfaform.tableWidget_oyun.setItem(i, j, item)          

        

    def tablo(self):
        self.conn = sqlite3.connect("Veritabani.db")
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT * FROM oyunlar")
        oyun_rows = self.cur.fetchall()

        self.cur.execute("SELECT * FROM {}_koleksiyon_tablosu".format(self.kadi))
        koleksiyon_rows = self.cur.fetchall()

        self.anasayfaform.tableWidget_koleksiyon.setRowCount(len(koleksiyon_rows))

        self.cur.execute("SELECT * FROM {}_favori_tablosu".format(self.kadi))
        favori_rows = self.cur.fetchall()

        self.anasayfaform.tableWidget_favori.setRowCount(len(favori_rows))

        for i, row in enumerate(koleksiyon_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor("white"))
                self.anasayfaform.tableWidget_koleksiyon.setItem(i, j, item)

        self.anasayfaform.tableWidget_oyun.setRowCount(len(oyun_rows))
    
        for i, row in enumerate(oyun_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor("white"))
                self.anasayfaform.tableWidget_oyun.setItem(i, j, item)
        
        for i, row in enumerate(favori_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor("white"))
                self.anasayfaform.tableWidget_favori.setItem(i, j, item)

        self.anasayfaform.tableWidget_oyun.setColumnWidth(0, 142)  # Sütun büyüklüklerini ayarlar.
        self.anasayfaform.tableWidget_oyun.setColumnWidth(1, 75)  
        self.anasayfaform.tableWidget_oyun.setColumnWidth(2, 110)
        self.anasayfaform.tableWidget_oyun.setColumnWidth(3, 55)
        self.anasayfaform.tableWidget_oyun.setColumnWidth(4, 50)
        self.anasayfaform.tableWidget_oyun.verticalHeader().setDefaultSectionSize(40)

        self.anasayfaform.tableWidget_koleksiyon.setColumnWidth(0, 160)  
        self.anasayfaform.tableWidget_koleksiyon.setColumnWidth(1, 90)  
        self.anasayfaform.tableWidget_koleksiyon.setColumnWidth(2, 135)
        self.anasayfaform.tableWidget_koleksiyon.setColumnWidth(3, 70)
        self.anasayfaform.tableWidget_koleksiyon.verticalHeader().setDefaultSectionSize(40)

        self.anasayfaform.tableWidget_favori.setColumnWidth(0, 160)
        self.anasayfaform.tableWidget_favori.setColumnWidth(1, 90)  
        self.anasayfaform.tableWidget_favori.setColumnWidth(2, 135)
        self.anasayfaform.tableWidget_favori.setColumnWidth(3, 70)
        self.anasayfaform.tableWidget_favori.verticalHeader().setDefaultSectionSize(40)

    
    
    
    
    
    
    
    
    
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