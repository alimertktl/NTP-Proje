from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from giris_py import Ui_Giris
from anaekran import AnaPage
import sqlite3

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Giris()
        self.loginform.setupUi(self)

        self.loginform.pushButton_giris.clicked.connect(self.save_to_database)

    def save_to_database(self):
        isim = self.loginform.lineEdit_isim.text()
        soyisim = self.loginform.lineEdit_soyisim.text()
        yas = self.loginform.comboBox_yas.currentText()
        cinsiyet = self.loginform.comboBox.currentText()

        if not isim or not soyisim:
            QMessageBox.warning(self, 'Uyarı', 'İsim ve soyisim alanları zorunludur.')
            return

        conn = sqlite3.connect('kullanici_veritabani.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Kullanicilar 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, isim TEXT, soyisim TEXT, yas TEXT, cinsiyet TEXT)''')
        cursor.execute("INSERT INTO Kullanicilar (isim, soyisim, yas, cinsiyet) VALUES ( ?, ?, ?, ?)",
                       (isim, soyisim, yas, cinsiyet))
        conn.commit()
        conn.close()

        self.open_main_page()

    def open_main_page(self):
        self.main_window = AnaPage()  # AnaPage sınıfından bir nesne oluştur
        self.main_window.show()
        self.close()  # Giriş sayfasını kapat

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec_())
