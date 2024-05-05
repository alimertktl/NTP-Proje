from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from seyahat2 import Ui_MainWindow  # Kullanıcı arayüzünü içe aktar
import os

class seyahat2_Page(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.seyahat2 = Ui_MainWindow()  # Kullanıcı arayüzü nesnesini oluştur
        self.seyahat2.setupUi(self)  # Kullanıcı arayüzünü ayarla
        self.seyahat2.pushButton_Seyahat_Sec_3.clicked.connect(self.kaydet)  # Kaydetme düğmesine tıklama olayını bağla
        self.seyahat2.pushButton_Seyahat_Rota.clicked.connect(self.goster)  # Gösterme düğmesine tıklama olayını bağla
        self.seyahat2.pushButton_Seyahat_Sifirla.clicked.connect(self.sifirla)  # Sıfırlama düğmesine tıklama olayını bağla

    def kaydet(self):
        # Dosya adı ve konumu
        dosya_adi = "depolama.txt"

        # Kullanıcı tarafından girilen verileri al
        veriler = ""
        rows = self.seyahat2.tableWidget_3.rowCount()
        cols = self.seyahat2.tableWidget_3.columnCount()
        for row in range(rows):
            rota_adi = self.seyahat2.tableWidget_3.item(row, 0)
            konaklama_tesis = self.seyahat2.tableWidget_3.item(row, 1)
            fiyat = self.seyahat2.tableWidget_3.item(row, 2)

            # Verilerin eksiksiz olduğunu kontrol et
            if (rota_adi is not None and rota_adi.text().strip() != "") or \
               (konaklama_tesis is not None and konaklama_tesis.text().strip() != "") or \
               (fiyat is not None and fiyat.text().strip() != ""):

                if (rota_adi is None or rota_adi.text().strip() == "") or \
                   (konaklama_tesis is None or konaklama_tesis.text().strip() == "") or \
                   (fiyat is None or fiyat.text().strip() == ""):
                    
                    QMessageBox.warning(self, "Uyarı", "Lütfen tüm bilgileri doldurun.")
                    return

                # Verileri biçimlendir ve depolama için hazırla
                veri = f"{rota_adi.text()}\t{konaklama_tesis.text()}\t{fiyat.text()}\n"
                veriler += veri

        # Verileri dosyaya yaz
        with open(dosya_adi, "w") as dosya:
            dosya.write(veriler)

        QMessageBox.information(self, "Bilgi", "Veriler başarıyla kaydedildi.")

    def goster(self):
        # Dosya adı ve konumu
        dosya_adi = "depolama.txt"

        # Dosyayı aç ve verileri oku
        try:
            with open(dosya_adi, "r") as dosya:
                veriler = dosya.read()
            QMessageBox.information(self, "Kaydedilen Veriler", veriler)
        except FileNotFoundError:
            QMessageBox.warning(self, "Uyarı", "Kaydedilen veri bulunamadı.")

    def sifirla(self):
        # Dosya adı ve konumu
        dosya_adi = "depolama.txt"

        # Dosyayı sil
        try:
            os.remove(dosya_adi)
            QMessageBox.information(self, "Bilgi", "Kaydedilen veriler başarıyla silindi.")
        except FileNotFoundError:
            QMessageBox.warning(self, "Uyarı", "Kaydedilen veri bulunamadı.")

# Uygulamayı çalıştır
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
