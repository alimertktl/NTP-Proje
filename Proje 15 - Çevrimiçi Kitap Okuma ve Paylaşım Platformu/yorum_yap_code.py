from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QMessageBox
from yorum_yap import Ui_MainWindow

class YorumPage(QMainWindow):
    def __init__(self, home_page, kitap_adi, kullanici_adi):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.home_page = home_page
        self.kitap_adi = kitap_adi
        self.kullanici_adi = kullanici_adi  # Kullanıcı adını al
        self.ui.pushButton_4.clicked.connect(self.yorumGonder)

    def yorumGonder(self):
        
        yorum = self.ui.lineEdit_2.text().strip()
        if yorum:
            self.home_page.yorumKaydet(self.kitap_adi, self.kullanici_adi, yorum)  # Kullanıcı adını kullanarak yorumu kaydet
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Lütfen yorumunuzu girin.")
