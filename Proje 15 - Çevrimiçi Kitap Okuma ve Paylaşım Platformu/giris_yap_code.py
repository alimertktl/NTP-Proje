from PyQt5.QtWidgets import *
from giris_yap import Ui_MainWindow
from home_page_code import HomePage
class GirisYapEkran(QMainWindow):
    def __init__(self):
        super().__init__()
        self.giris = Ui_MainWindow()
        self.giris.setupUi(self)
        self.giris.pushButton_5.clicked.connect(self.kayitol)
        self.giris.pushButton_4.clicked.connect(self.handle_login)
        self.homeAc = HomePage() 
        self.kullanici_adi = None  



    def kayitol(self):
        from kayit_ol_code import KayitOlEkran
        self.kayitAc = KayitOlEkran() 

        self.kayitAc.show()
        self.close()

    def login_user(self, username, password):
        kullanici = False
        sifre_kontrol = False
        try:
            with open("users.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    stored_username, _, stored_password = user.strip().split(',')
                    if stored_username == username:
                        kullanici = True
                        if stored_password == password:
                            sifre_kontrol = True
                            break
        except FileNotFoundError:
            pass
        return kullanici, sifre_kontrol



    
    def handle_login(self):
        username = self.giris.lineEdit_2.text()
        password = self.giris.lineEdit_4.text()
        if not (username and password):
            QMessageBox.warning(self, "Hata", "Lütfen kullanıcı adınızı ve şifrenizi girin.")
        else:
            kullanici, sifre_kontrol = self.login_user(username, password)
            if kullanici and sifre_kontrol:
                self.kullanici_adi = username
                self.open_home_page()
            elif kullanici and not sifre_kontrol:
                QMessageBox.warning(self, "Hata", "Yanlış şifre girdiniz.")
            else:
                QMessageBox.warning(self, "Hata", "Kullanıcı bulunamadı.")


    def open_home_page(self):
        if self.kullanici_adi is not None:
            self.homePage = HomePage(self.kullanici_adi)
            self.homePage.show()
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı yüklenemedi.")