from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from destek_sayfasi import Ui_MainWindow
from satis_talep_code import SatisPage

class DestekPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.desteksayfa = Ui_MainWindow()
        self.desteksayfa.setupUi(self)
        self.dgonder = self.destekOku()
        self.desteksayfa.pushButton.clicked.connect(self.gonder)
        self.satissayfaAc = SatisPage()

    def gonder(self):
        destektalebi = self.desteksayfa.lineEdit_2.text()
        if not destektalebi:
            QMessageBox.warning(self, "Uyarı", "Lütfen destek almak istediğiniz konuyu giriniz.")

        else:
            if not self.Destekler(destektalebi):
                self.dgonder.append(destektalebi)
                self.veriDepo(self.dgonder)
                QMessageBox.information(self, "Başarılı", "Destek talebi oluşturuldu.")
                self.satissayfaAc.talepleriYukle()


            else:
                QMessageBox.warning(self, "Uyarı", "Bu konu hakkında destek talebi zaten mevcut.")

            self.close()


    def Destekler(self, destektalebi):
        for item in self.dgonder:
            if item == destektalebi:
                return True
        return False

    def veriDepo(self, dgonder):
        with open('destekler.txt', 'w') as file:
            for gez in dgonder:
                file.write(gez + "\n")

    def destekOku(self):
        try:
            with open("destekler.txt", "r") as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            return []

