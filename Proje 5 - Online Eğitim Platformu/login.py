from PyQt5.QtWidgets import *
from egitim_py import Ui_MainWindow  # egitim_py dosyasından Ui_MainWindow sınıfını içe aktar
from anapencere import AnapencerePage  # anapencere dosyasından AnapencerePage sınıfını içe aktar
from PyQt5.QtCore import QRegExp  # PyQt5.QtCore modülünden QRegExp sınıfını içe aktar
from PyQt5.QtGui import QRegExpValidator  # PyQt5.QtGui modülünden QRegExpValidator sınıfını içe aktar

class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # UI dosyasını kullanarak arayüzü yükle
        self.loginform = Ui_MainWindow()
        self.loginform.setupUi(self)
        
        # AnapencerePage sınıfından bir örnek oluştur
        self.anapencereac = AnapencerePage()
        
        # Mail alanına geçerli bir e-posta adresi girilip girilmediğini kontrol etmek için bir geçerlilik denetleyici oluştur
        mail_validator = QRegExpValidator(QRegExp(".+@.+"))  
        self.loginform.lineEdit_2_mail.setValidator(mail_validator)
        
        # Giriş düğmesine tıklandığında GirisYap metodunu çağır
        self.loginform.pushButton_Giris.clicked.connect(self.GirisYap)
        
    def GirisYap(self):
        # Kullanıcıdan giriş bilgilerini al
        isim = self.loginform.lineEdit_isim.text()
        mail = self.loginform.lineEdit_2_mail.text()

        # E-posta adresinin geçerli olup olmadığını kontrol et
        if mail.count('@') == 0:  
            QMessageBox.warning(self, "Hata", "Geçerli bir mail adresi girin.")
            return

        # Kullanıcı bilgilerini bir dosyaya kaydet
        with open('kullanici_bilgileri.txt', 'a') as dosya:
            dosya.write(f"İsim: {isim}, Mail: {mail}\n")

        # Giriş ekranını kapat ve ana pencereyi göster
        self.close()
        self.anapencereac.show()
