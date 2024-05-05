import sys
from PyQt5.QtWidgets import *
from anasayfaSeyahat import Ui_MainWindow  # Kullanıcı arayüzünü içe aktar
from seyahat2_py import seyahat2_Page  # Seyahat planı sayfasını içe aktar
import importlib
import random

# UnicodeEncodeError hatasını çözmek için gerekli ayarlamaları yap
importlib.reload(sys)

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_MainWindow()  # Kullanıcı arayüzü nesnesini oluştur
        self.loginform.setupUi(self)  # Kullanıcı arayüzünü ayarla
        
        # Tablo satırlarını seçme davranışını ayarla
        self.loginform.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seyahat planı oluşturma düğmesine tıklama olayını bağla
        self.loginform.pushButton_Seyahat_Sec.clicked.connect(self.seyahat_plani_olustur)
        # Seyahat planlama düğmesine tıklama olayını bağla
        self.loginform.pushButton_Seyahat_Planla.clicked.connect(self.ac_seyahat2)
        # Seyahat2 sayfasını oluştur
        self.ac_seyahat2 = seyahat2_Page()
        # Tabloyu düzenleme iznini kapat
        self.loginform.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def seyahat_plani_olustur(self):
        # Kullanıcının seçtiği satırın indeksini al
        secilen_satir = self.loginform.tableWidget.currentRow()

        if secilen_satir == -1:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir seyahat planı seçin veya seyahat planlayın.")
        elif secilen_satir >= self.loginform.tableWidget.rowCount():
            QMessageBox.warning(self, "Uyarı", "Geçersiz bir seyahat planı seçtiniz.")
        else:
            # Seçilen rotanın adını al
            rotanin_adi = self.loginform.tableWidget.item(secilen_satir, 0).text()
            QMessageBox.information(self, "Başarılı", f"{rotanin_adi} rotası için seyahat planınız başarıyla oluşturulmuştur.\n"
                                                       f"Belirlenen rota uzunluğu: {random.randint(70, 150)} km")
            
    def ac_seyahat2(self):
        # Seyahat2 sayfasını aç
        self.seyahat2_page = seyahat2_Page()
        self.seyahat2_page.show()
        # Giriş sayfasını kapat
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login_page = LoginPage()  # LoginPage örneğini bir değişkende sakla
    login_page.show()  # Pencereyi göster
    sys.exit(app.exec_())
