from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from satis_talep import Ui_MainWindow
import random
class SatisPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.satissayfa = Ui_MainWindow()
        self.satissayfa.setupUi(self)
        self.satissayfa.pushButton.clicked.connect(self.geri)
        self.musterileriYukle()
        self.talepleriYukle()
        self.satislariYukle()

    def satisyenile(self):
        self.satislariYukle()
    
    def musteriyenile(self):
        self.musterileriYukle()
    
    def destekyenile(self):
        self.talepleriYukle()
    
    def geri(self):
        from home_code import HomePage
        self.homesayfaAc = HomePage()
        self.homesayfaAc.show()
        self.close()
    
  
    def satislariYukle(self):
        
        try:
            with open('satislar.txt', 'r') as file:
                satislar = [line.strip().split(',') for line in file.readlines()]
                
            self.satissayfa.tableWidget.setRowCount(len(satislar))
            for i, kiralama in enumerate(satislar):
            
                for j, item in enumerate(kiralama):
                    self.satissayfa.tableWidget.setItem(i, j, QTableWidgetItem(item))
        except FileNotFoundError:
            print("kullanıcılar.txt dosyası bulunamadı.")

    def musterileriYukle(self):
        
        try:
            with open('musteriler.txt', 'r') as file:
                musterican = [line.strip().split(',') for line in file.readlines()]
                
            self.satissayfa.tableWidget_3.setRowCount(len(musterican))
            for i, kiralama in enumerate(musterican):
            
                for j, item in enumerate(kiralama):
                    self.satissayfa.tableWidget_3.setItem(i, j, QTableWidgetItem(item))
        except FileNotFoundError:
            print("kullanıcılar.txt dosyası bulunamadı.")


    def talepleriYukle(self):

        try:
            with open('destekler.txt', 'r') as file:
                destekcan = [line.strip().split(',') for line in file.readlines()]
                
            self.satissayfa.tableWidget_2.setRowCount(len(destekcan))
            for i, kiralama in enumerate(destekcan):
                talep_numarasi = random.randint(1, 120) 
                self.satissayfa.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(talep_numarasi)))
                for j, item in enumerate(kiralama):
                    self.satissayfa.tableWidget_2.setItem(i, j + 1, QTableWidgetItem(item))

        except FileNotFoundError:
            print("destekler.txt dosyası bulunamadı.")