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

        self.anasayfaform.lineEdit_arama.textChanged.connect(self.aramafiltre)
        self.anasayfaform.pushButton_izle.clicked.connect(self.izle)
        self.anasayfaform.pushButton_izlemelisteekle.clicked.connect(self.listeekle)
        self.anasayfaform.pushButton_izlemelistesil.clicked.connect(self.listesil)
        self.anasayfaform.pushButton_ekle.clicked.connect(self.ekle)
        self.anasayfaform.pushButton_cikis.clicked.connect(self.cikis)

    def aramafiltre(self):
        filtre_text = self.anasayfaform.lineEdit_arama.text()  
        self.cur.execute("SELECT * FROM icerikler WHERE ad LIKE ?", ('%' + filtre_text + '%',))
        filtered_rows = self.cur.fetchall()

        self.anasayfaform.tableWidget_icerik.clearContents()
        self.anasayfaform.tableWidget_icerik.setRowCount(len(filtered_rows))
        for i, row in enumerate(filtered_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.anasayfaform.tableWidget_icerik.setItem(i, j, item)

    def izle(self):
        selected_row_index = self.anasayfaform.tableWidget_izleliste.currentRow()
        selected_table_widget = self.anasayfaform.tableWidget_izleliste

        if selected_row_index == -1:  # Eğer izleme listesinden bir film seçilmemişse
            selected_row_index = self.anasayfaform.tableWidget_icerik.currentRow()
            selected_table_widget = self.anasayfaform.tableWidget_icerik

            if selected_row_index == -1:  # Eğer izleme geçmişi tablosundan bir film seçilmemişse
                selected_row_index = self.anasayfaform.tableWidget_izlegecmis.currentRow()
                selected_table_widget = self.anasayfaform.tableWidget_izlegecmis

        if selected_row_index == -1:  # Eğer herhangi bir film seçilmemişse
            QMessageBox.warning(self, 'Uyarı', 'İzlemek istediğiniz bir film seçiniz.')
            return

        selected_row = [selected_table_widget.item(selected_row_index, column).text() 
                    for column in range(selected_table_widget.columnCount())]

        # İzlenen filmin adının izleme geçmişi tablosunda olup olmadığını kontrol et
        self.cur.execute("SELECT * FROM {}_izleme_gecmisi_tablosu WHERE ad=?".format(self.kadi), (selected_row[1],))
        existing_row = self.cur.fetchone()
        if existing_row:
            QMessageBox.information(self, 'Bilgi', 'Film başarıyla izlendi.')
        else:
            # İzlenen filmin bilgilerini izleme geçmişi tablosuna ekle
            self.cur.execute("INSERT INTO {}_izleme_gecmisi_tablosu (tur, ad, yonetmen, sure) VALUES (?, ?, ?, ?)".format(self.kadi), selected_row)
            self.conn.commit()
            QMessageBox.information(self, 'Bilgi', 'Film başarıyla izlendi.')

        # Tabloyu yenile
        self.tablo()

    def listeekle(self):
        satir = self.anasayfaform.tableWidget_icerik.selectionModel().selectedRows()
        if not satir:
            QMessageBox.warning(self, 'Uyarı', 'Lütfen bir içerik seçin.')
            return

        selected_row = satir[0].row()
        tur = self.anasayfaform.tableWidget_icerik.item(selected_row, 0).text()
        ad = self.anasayfaform.tableWidget_icerik.item(selected_row, 1).text()
        yonetmen = self.anasayfaform.tableWidget_icerik.item(selected_row, 2).text()
        sure = self.anasayfaform.tableWidget_icerik.item(selected_row, 3).text()

        # İçeriğin izleme listesinde olup olmadığını kontrol et
        self.cur.execute("SELECT * FROM {}_izleme_tablosu WHERE ad=?".format(self.kadi), (ad,))
        existing_row = self.cur.fetchone()
        if existing_row:
            QMessageBox.warning(self, 'Uyarı', 'Seçtiğiniz içerik zaten izleme listesinde.')

        else:
            # İçeriği izleme listesine ekle
            self.cur.execute("INSERT INTO {}_izleme_tablosu (tur,ad,yonetmen,sure) VALUES (?,?,?,?)".format(self.kadi), (tur,ad,yonetmen,sure,))
            self.conn.commit()
            QMessageBox.information(self, 'Bilgi', 'İçerik başarıyla izleme listesine eklendi.')

        self.tablo()

    def listesil(self):
        satir = self.anasayfaform.tableWidget_izleliste.selectionModel().selectedRows()
        if not satir:
            QMessageBox.warning(self, 'Uyarı', 'Lütfen bir içerik seçin.')
            return

        selected_row = satir[0].row()
        icerik = self.anasayfaform.tableWidget_izleliste.item(selected_row, 1).text()

        # İçeriği izleme listesinden sil
        self.cur.execute("DELETE FROM {}_izleme_tablosu WHERE ad=?".format(self.kadi), (icerik,))
        self.conn.commit()
        QMessageBox.information(self, 'Bilgi', 'İçerik izleme listesinden silindi.')

        # İzleme listesini yenile
        self.tablo()

    def tablo(self):
        self.conn = sqlite3.connect("Veritabani.db")
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT * FROM icerikler")
        icerik_rows = self.cur.fetchall()

        self.cur.execute("SELECT * FROM {}_izleme_tablosu".format(self.kadi))
        izleliste_rows = self.cur.fetchall()

        self.anasayfaform.tableWidget_izleliste.setRowCount(len(izleliste_rows))

        self.cur.execute("SELECT * FROM {}_izleme_gecmisi_tablosu".format(self.kadi))
        izlegecmis_rows = self.cur.fetchall()

        self.anasayfaform.tableWidget_izlegecmis.setRowCount(len(izlegecmis_rows))

        for i, row in enumerate(izleliste_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.anasayfaform.tableWidget_izleliste.setItem(i, j, item)

        self.anasayfaform.tableWidget_icerik.setRowCount(len(icerik_rows))
    
        for i, row in enumerate(icerik_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.anasayfaform.tableWidget_icerik.setItem(i, j, item)
        
        for i, row in enumerate(izlegecmis_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.anasayfaform.tableWidget_izlegecmis.setItem(i, j, item)

        self.anasayfaform.tableWidget_icerik.setColumnWidth(0, 85)  # Sütun büyüklüklerini ayarlar.
        self.anasayfaform.tableWidget_icerik.setColumnWidth(1, 200)  
        self.anasayfaform.tableWidget_icerik.setColumnWidth(2, 106)
        self.anasayfaform.tableWidget_icerik.setColumnWidth(3, 50)
        self.anasayfaform.tableWidget_icerik.verticalHeader().setDefaultSectionSize(40)

        self.anasayfaform.tableWidget_izleliste.setColumnWidth(0, 100)  
        self.anasayfaform.tableWidget_izleliste.setColumnWidth(1, 200)  
        self.anasayfaform.tableWidget_izleliste.setColumnWidth(2, 106)
        self.anasayfaform.tableWidget_izleliste.setColumnWidth(3, 50)
        self.anasayfaform.tableWidget_izleliste.verticalHeader().setDefaultSectionSize(30)

        self.anasayfaform.tableWidget_izlegecmis.setColumnWidth(0, 100)
        self.anasayfaform.tableWidget_izlegecmis.setColumnWidth(1, 200)  
        self.anasayfaform.tableWidget_izlegecmis.setColumnWidth(2, 106)
        self.anasayfaform.tableWidget_izlegecmis.setColumnWidth(3, 50)
        self.anasayfaform.tableWidget_izlegecmis.verticalHeader().setDefaultSectionSize(30)

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


    

        
