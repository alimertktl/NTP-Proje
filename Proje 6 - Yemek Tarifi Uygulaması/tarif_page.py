import sqlite3
import sys
from PyQt5.QtWidgets import *
from tarif import Ui_Form
from anasayfa_page import Anasayfa

class Tarif(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.tarifform = Ui_Form()
        self.tarifform.setupUi(self)
        self.anasayfaac = Anasayfa()

        self.conn = sqlite3.connect("Tarifler.db")
        self.cur = self.conn.cursor()

        self.tarifform.pushButton_ekle.clicked.connect(self.tarifekle)
        self.tarifform.pushButton_iptal.clicked.connect(self.iptal)

    def tarifekle(self):
        tarif_adi = self.tarifform.lineEdit_yemekadi.text()
        tarif_malzemeler = self.tarifform.lineEdit_malzemeler.text()
        tarif_aciklama = self.tarifform.lineEdit_tarif.text()

        if not tarif_adi or not tarif_malzemeler or not tarif_aciklama:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return

        self.cur.execute("INSERT INTO Tarif (yemekadı, malzemeler, tarif) VALUES (?, ?, ?)", (tarif_adi, tarif_malzemeler, tarif_aciklama ))
        self.conn.commit()

        QMessageBox.information(self, "Başarılı", "Tarif başarıyla eklendi.")

        self.close()
        self.anasayfaac.show()

    def iptal(self):
        self.close()
        self.anasayfaac.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tarif()
    window.show()
    sys.exit(app.exec_())

        