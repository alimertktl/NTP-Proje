from PyQt5.QtWidgets import *
from kayit_ol import Ui_MainWindow
from giris_yap_code import GirisYapEkran

class KayitOlEkran(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kayitEkran = Ui_MainWindow()
        self.kayitEkran.setupUi(self)
        self.kayitEkran.pushButton_5.clicked.connect(self.girisyap)
        self.GirisAc = GirisYapEkran() 
        self.kayitEkran.pushButton_4.clicked.connect(self.handle_register)

    def girisyap(self):
        self.GirisAc.show()
        self.close()

    def register_user(self, username, email, password):
        with open("users.txt", "a+") as file:
            file.seek(0)
            users = file.readlines()
            for user in users:
                stored_username, stored_email, _ = user.strip().split(',')
                if stored_username == username or stored_email == email:
                    return False  # Kullanıcı adı veya e-posta zaten kayıtlı
            file.write(f"{username},{email},{password}\n")
            return True

    def handle_register(self):
        username = self.kayitEkran.lineEdit_2.text()
        email = self.kayitEkran.lineEdit_3.text()
        password = self.kayitEkran.lineEdit_4.text()
        if not (username and email and password):
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")
        elif self.register_user(username, email, password):
            QMessageBox.information(self, "Başarılı", "Kayıt başarılı!")
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya e-posta zaten kullanılıyor.")
