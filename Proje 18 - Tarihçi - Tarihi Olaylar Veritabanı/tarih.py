from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from tarih_py import Ui_Tarih
import sqlite3


class TarihPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Tarih()
        self.loginform.setupUi(self)

        self.db_connection = sqlite3.connect("tarih.db")
        self.cursor = self.db_connection.cursor()
        self.create_table()

        self.loginform.table_liste.cellClicked.connect(self.tablo_item_tiklandi)
        
        
        self.loginform.btnEkle.clicked.connect(self.kayityap)
        self.loginform.btnSil.clicked.connect(self.sutun_sil)
        self.loginform.btnGuncelle.clicked.connect(self.guncelle)
        self.loginform.lneAra.textChanged.connect(self.ara_tabloda)

        self.loginform.btn_sahsiyet.clicked.connect(self.sahsiyet_sirala)
        self.loginform.btn_yasadigidonem.clicked.connect(self.yasadigi_donem_sirala)
        self.loginform.btn_olayadi.clicked.connect(self.olay_adi_sirala)
        self.loginform.btn_tarihi.clicked.connect(self.tarih_sirala)
        self.loginform.btn_donemadi.clicked.connect(self.donem_adi_sirala)

        self.loginform.btn_listele.clicked.connect(self.verileri_listele)
        self.loginform.btn_cikis.clicked.connect(self.close)

        self.loginform.menuHakkinda.triggered.connect(self.hakkinda_mesaji)


        # Tablo listesinin başlangıçta temizlenmesi
        #self.loginform.table_liste.setRowCount(0)

        self.loginform.table_liste.cellClicked.connect(self.tablo_item_tiklandi)
        
        # Kullanıcıyı sütun düzenlemesini engelleme
        self.loginform.table_liste.setEditTriggers(QTableWidget.NoEditTriggers)
        # Veritabanındaki bilgileri tabloya yansıt
        self.populate_table()

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS tarihler (
            olay_no INTEGER PRIMARY KEY,
            sahsiyet TEXT,
            yasadigi_donem TEXT,
            olay_adi TEXT,
            tarih TEXT,
            olay TEXT,
            donem_adi TEXT,
            baslangic TEXT,
            bitis TEXT
        );
        """
        self.cursor.execute(create_table_query)
        self.db_connection.commit()
        

    def populate_table(self):
        self.cursor.execute("SELECT * FROM tarihler")
        data = self.cursor.fetchall()
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.loginform.table_liste.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def kayityap(self):
        olay_no = self.loginform.line_olayno.text()
        sahsiyet = self.loginform.line_sahsiyet.text()
        yasadigi_donem = self.loginform.line_yasadigidonem.text()
        olay_adi = self.loginform.line_olayadi.text()
        tarih = self.loginform.line_tarih.text()
        donem_adi = self.loginform.line_donemadi.text()
        baslangic = self.loginform.line_baslangictarihi.text()
        bitis = self.loginform.line_bitistarihi.text()

        if olay_no and sahsiyet and yasadigi_donem and olay_adi and tarih and donem_adi and baslangic and bitis:
        # Veritabanında olay_no'ya sahip bir kayıt var mı kontrol et
            self.cursor.execute("SELECT * FROM tarihler WHERE olay_no = ?", (olay_no,))
            existing_record = self.cursor.fetchone()
            if existing_record:
                QMessageBox.warning(self, "Uyarı", "Girdiğiniz olay numarası zaten kullanımda.", QMessageBox.Ok)
            else:
                self.cursor.execute('''INSERT INTO tarihler 
                                (olay_no, sahsiyet, yasadigi_donem, olay_adi, tarih, donem_adi, baslangic, bitis) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                                (olay_no, sahsiyet, yasadigi_donem, olay_adi, tarih, donem_adi, baslangic, bitis))

            # Eklenen veriyi tabloya yerleştirme
                self.tabloyaekle(olay_no, sahsiyet, yasadigi_donem, olay_adi, tarih, donem_adi, baslangic, bitis)
                self.populate_table()
    
            # Veritabanını güncelle
                self.db_connection.commit()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm verileri doldurun.\nBoş alanları N/A (Not Available) olarak doldurun.", QMessageBox.Ok)




    def closeEvent(self, event):
        if self.loginform.table_liste.currentRow() == -1:
            QMessageBox.warning(self, "Uyarı", "Lütfen silmek istediğiniz sütunu seçin.", QMessageBox.Ok)
            event.ignore()
        else:
        # Uygulama kapatılırken veritabanını güncelle
            self.db_connection.commit()
            event.accept()



    def tabloyaekle(self, olay_no, sahsiyet, yasadigi_donem, olay_adi, tarih, donem_adi, baslangic, bitis):
        row_count = self.loginform.table_liste.rowCount()
        self.loginform.table_liste.insertRow(row_count)
        self.loginform.table_liste.setItem(row_count, 0, QTableWidgetItem(str(olay_no)))
        self.loginform.table_liste.setItem(row_count, 1, QTableWidgetItem(sahsiyet))
        self.loginform.table_liste.setItem(row_count, 2, QTableWidgetItem(yasadigi_donem))
        self.loginform.table_liste.setItem(row_count, 3, QTableWidgetItem(olay_adi))
        self.loginform.table_liste.setItem(row_count, 4, QTableWidgetItem(tarih))
        self.loginform.table_liste.setItem(row_count, 5, QTableWidgetItem(donem_adi))
        self.loginform.table_liste.setItem(row_count, 6, QTableWidgetItem(baslangic))
        self.loginform.table_liste.setItem(row_count, 7, QTableWidgetItem(bitis))


    def sutun_sil(self):
        selected_row = self.loginform.table_liste.currentRow()  # Seçili satırın dizinini al
        if selected_row != -1:
            confirmation = QMessageBox.question(self, "Sütun Sil", "Seçili sütunu silmek istediğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
            # Aynı satırı veritabanından da sil
                olay_no_item = self.loginform.table_liste.item(selected_row, 0)  # Olay numarası için hücreyi al
                if olay_no_item is not None:
                    olay_no = olay_no_item.text()  # Olay numarasını al
                    self.cursor.execute("DELETE FROM tarihler WHERE olay_no = ?", (olay_no,))
                    self.db_connection.commit()
                
            # Tablodan satırı sil
                self.loginform.table_liste.removeRow(selected_row)
            else:
                pass
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen silmek istediğiniz sütunu seçin.", QMessageBox.Ok)





    def tablo_item_tiklandi(self, row):
    # Tüm satır seçildiğinde işlem yap
        olay_item = self.loginform.table_liste.item(row, 3)  # Olay sütununu al
        if olay_item is not None:
        # Hücre değeri None değilse, text özelliğine eriş
            olay_metni = olay_item.text() if olay_item else ""

        # Alınan metni line_olay kutusuna yaz
            self.loginform.line_olay.setText(olay_metni)

    def guncelle(self):
        selected_row = self.loginform.table_liste.currentRow()  # Seçili satırın indeksini al
        if selected_row != -1:
        # Seçili satırdaki verileri al
            olay_no = self.loginform.line_olayno.text()
            sahsiyet = self.loginform.line_sahsiyet.text()
            yasadigi_donem = self.loginform.line_yasadigidonem.text()
            olay_adi = self.loginform.line_olayadi.text()
            tarih = self.loginform.line_tarih.text()
            donem_adi = self.loginform.line_donemadi.text()
            baslangic = self.loginform.line_baslangictarihi.text()
            bitis = self.loginform.line_bitistarihi.text()

        # Gerekli alanların dolu olup olmadığını kontrol et
            if not all([sahsiyet, yasadigi_donem, olay_adi, tarih, donem_adi, baslangic, bitis]):
                QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.", QMessageBox.Ok)
                return

        # Seçili satırdaki olay numarasını al
            olay_no_item = self.loginform.table_liste.item(selected_row, 0)
            if olay_no_item is not None:
                olay_no = olay_no_item.text()

        # Veritabanında seçili satırı güncelle
            self.cursor.execute('''UPDATE tarihler SET sahsiyet=?, yasadigi_donem=?, olay_adi=?, tarih=?, 
                                donem_adi=?, baslangic=?, bitis=? WHERE olay_no=?''',
                                (sahsiyet, yasadigi_donem, olay_adi, tarih, donem_adi, baslangic, bitis, olay_no))
            self.db_connection.commit()

        # Tabloyu güncelle
            self.populate_table()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen güncellemek istediğiniz bir satırı seçin.", QMessageBox.Ok)


    def ara_tabloda(self):
        aranan_metin = self.loginform.lneAra.text().strip().lower()
        self.cursor.execute("SELECT * FROM tarihler WHERE lower(sahsiyet) LIKE ? OR lower(olay_adi) LIKE ? OR lower(tarih) LIKE ? OR lower(donem_adi) LIKE ? OR lower(baslangic) LIKE ? OR lower(bitis) LIKE ?", 
                            ('%' + aranan_metin + '%', '%' + aranan_metin + '%', '%' + aranan_metin + '%', '%' + aranan_metin + '%', '%' + aranan_metin + '%', '%' + aranan_metin + '%'))
        data = self.cursor.fetchall()
        self.loginform.table_liste.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.loginform.table_liste.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))



    def sahsiyet_sirala(self):
        self.loginform.table_liste.sortItems(1)

    def yasadigi_donem_sirala(self):
        self.loginform.table_liste.sortItems(2)

    def olay_adi_sirala(self):
        self.loginform.table_liste.sortItems(3)

    def tarih_sirala(self):
        self.loginform.table_liste.sortItems(4)

    def donem_adi_sirala(self):
        self.loginform.table_liste.sortItems(5)

    def verileri_listele(self):
    # Mevcut verileri temizleme
        self.populate_table()


    def hakkinda_mesaji(self):
        QMessageBox.information(self, "Hakkında", "Bu program tarihi olaylar ve tarihi kişilerin bir veritabanı yardımıyla tabloda kaydedilmesini sağlar. Ayrıca bu tablo içerisinde arama yapma olanağıda tanır.")
        