from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from egitim2_py import Ui_MainWindow  # egitim2_py dosyasından Ui_MainWindow sınıfını içe aktar

class AnapencerePage(QMainWindow):
   
    def __init__(self):
        super().__init__()
        # Arayüzü yükle
        self.anapencereform = Ui_MainWindow()
        self.anapencereform.setupUi(self)

        # Tablodaki hücreye tıklandığında 'hucre_secildi' metodunu bağla
        self.anapencereform.tableWidget.cellClicked.connect(self.hucre_secildi)

        # Takvime tarih seçildiğinde 'tarih_secildi' metodunu bağla
        self.anapencereform.calendarWidget_GunSecimi.selectionChanged.connect(self.tarih_secildi)

        # 'Kurs Oluştur' düğmesine tıklandığında 'kurs_olustur' metodunu bağla
        self.anapencereform.pushButton_KursOlustur.clicked.connect(self.kurs_olustur)

        # 'Liste' düğmesine tıklandığında 'liste_goster' metodunu bağla
        self.anapencereform.pushButton_Liste.clicked.connect(self.liste_goster)

        # Takvim minimum tarihini bugünkü tarih olarak ayarla
        bugun = QDate.currentDate()
        self.anapencereform.calendarWidget_GunSecimi.setMinimumDate(bugun)
        # Maksimum tarih olarak bir ay sonrasını ayarla
        maksimum_tarih = bugun.addMonths(1)
        self.anapencereform.calendarWidget_GunSecimi.setMaximumDate(maksimum_tarih)

    # Tablodaki hücreye tıklandığında çağrılan metod
    def hucre_secildi(self, row, column):
        # Seçilen hücrenin indekslerini al
        selected_indexes = self.anapencereform.tableWidget.selectedIndexes()
        if len(selected_indexes) > 1:
            QMessageBox.warning(self, "Uyarı", "Birden fazla hücre seçtiniz. Lütfen sadece bir hücre seçin.")
            return

        # Sadece belirli sütunlardaki hücreleri seçmeye izin ver
        allowed_columns = [0]
        if column not in allowed_columns:
            QMessageBox.warning(self, "Uyarı", "Sadece sol taraftaki seçenekleri seçebilirsiniz.")
            return

        # Seçilen hücrenin metnini al ve yazdır
        secilen_metin = self.anapencereform.tableWidget.item(row, column).text()
        print("Seçilen metin:", secilen_metin)

    # Takvimden tarih seçildiğinde çağrılan metod
    def tarih_secildi(self):
        # Seçilen tarihi al
        secilen_tarih = self.anapencereform.calendarWidget_GunSecimi.selectedDate().toString("yyyy-MM-dd")
        print("Seçilen tarih:", secilen_tarih)

        

    # 'Kurs Oluştur' düğmesine tıklandığında çağrılan metod
    def kurs_olustur(self):
        # Seçilen tarihi ve hücreyi al
        secilen_tarih = self.anapencereform.calendarWidget_GunSecimi.selectedDate().toString("yyyy-MM-dd")
        secilen_hucre = ""
        selected_indexes = self.anapencereform.tableWidget.selectedIndexes()
        if len(selected_indexes) > 0:
            secilen_hucre_row = selected_indexes[0].row()
            secilen_hucre_column = selected_indexes[0].column()
            secilen_hucre = self.anapencereform.tableWidget.item(secilen_hucre_row, secilen_hucre_column).text()

        # Geçmiş tarih seçilmişse uyarı ver
        bugun = QDate.currentDate()
        if self.anapencereform.calendarWidget_GunSecimi.selectedDate() < bugun:
            QMessageBox.warning(self, "Uyarı", "Geçmiş bir tarih seçtiniz. Lütfen doğru bir tarih seçiniz.")
        # Boş bir tarih veya hücre seçilmişse uyarı ver
        elif not secilen_hucre or not secilen_tarih:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir tarih ve bir kurs seçiniz.")
        else:
            # Kullanıcıyı bilgilendir
            mesaj = f"Seçilen tarih: {secilen_tarih}\nKurs bilgisi: {secilen_hucre}\nSaat 12:00 Kursunuz Kaydedilmiştir"
            QMessageBox.information(self, "Kurs Oluşturuldu", mesaj)
            # Veritabanına kurs bilgisini kaydet
            self.veritabani(selected_indexes)

    # Veritabanına kurs bilgisini kaydeden metod
    def veritabani(self, selected_indexes):
        if len(selected_indexes) > 0:
            secilen_tarih = self.anapencereform.calendarWidget_GunSecimi.selectedDate().toString("yyyy-MM-dd")
            secilen_hucre = ""
            secilen_hucre_row = selected_indexes[0].row()
            secilen_hucre_column = selected_indexes[0].column()
            secilen_hucre = self.anapencereform.tableWidget.item(secilen_hucre_row, secilen_hucre_column).text()
        with open('kullanici_bilgileri.txt', 'a') as dosya:
            dosya.write(f"Kurs {secilen_hucre}, Gün {secilen_tarih}\n")

    # 'Liste' düğmesine tıklandığında çağrılan metod
    def liste_goster(self):
        # Kullanıcı bilgilerini dosyadan oku ve göster
        with open('kullanici_bilgileri.txt', 'r') as dosya:
            icerik = dosya.read()
        QMessageBox.information(self, "Kullanıcı Bilgileri", icerik)

# Ana programın başlangıcı
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # Ana pencereyi oluştur ve göster
    MainWindow = AnapencerePage()
    MainWindow.show()
    sys.exit(app.exec_())
