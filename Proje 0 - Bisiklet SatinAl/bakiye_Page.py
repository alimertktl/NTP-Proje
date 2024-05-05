from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from bakiye import Ui_MainWindow 
class BakiyePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.gericik)
        self.ui.pushButton.clicked.connect(self.bakiyeYukle)


        
    def sabit(self):
        from home_Page import HomePage
        self.homeAc = HomePage() 
    def gericik(self):
        self.sabit()
        self.homeAc.show()
        self.close()


    def bakiyeYukle(self):
        admin_id = "7292"  
        user_id, ok = QInputDialog.getText(self, "Admin Doğrulama", "Admin kullanıcı ID giriniz:")
        if not ok or user_id != admin_id:
            QMessageBox.warning(self, "Yetkisiz Erişim", "Bu işlemi yapmak için yetkiniz yok.")
            return

        musteri_no = self.ui.lineEdit_2.text()
        yuklenecek_bakiye = self.ui.spinBox.value()
        if not musteri_no.isdigit() or int(musteri_no) <= 0:
            QMessageBox.warning(self, "Hata", "Geçersiz müşteri numarası.")
            return

    
        bakiyeler = {}
        try:
            with open("bakiyeler.txt", "r") as file:
                for line in file:
                    no, bakiye = line.strip().split(',')
                    bakiyeler[no] = int(bakiye)
        except FileNotFoundError:
            pass
    
        if musteri_no in bakiyeler:
            bakiyeler[musteri_no] += yuklenecek_bakiye
        else:
            bakiyeler[musteri_no] = yuklenecek_bakiye
    
        with open("bakiyeler.txt", "w") as file:
            for no, bakiye in bakiyeler.items():
                file.write(f"{no},{bakiye}\n")
    
    
        güncel_bakiye = bakiyeler[musteri_no]
        QMessageBox.information(self, "Başarılı", f"Bakiye başarıyla yüklendi. Güncel bakiyeniz: {güncel_bakiye} TL")







