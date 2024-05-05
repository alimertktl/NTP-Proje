from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from bilgi import Ui_MainWindow  
class BilgiPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.bilgiler = Ui_MainWindow()
        self.bilgiler.setupUi(self)  
        self.tabloyacek()
        self.bilgiler.pushButton.clicked.connect(self.gerigit)


    def gerigit(self):
        from kullanici_bilet_code import KullaniciBiletWindow
        self.deneme = KullaniciBiletWindow()

        self.deneme.show()
        self.close()

    def tabloyacek(self):
        
        try:
            with open('bilgi.txt', 'r',encoding='utf-8') as file:
                etkinlikci = [line.strip().split(',') for line in file.readlines()]
                
            self.bilgiler.tableWidget.setRowCount(len(etkinlikci))
            for i, etkin in enumerate(etkinlikci):
            
                for j, item in enumerate(etkin):
                    self.bilgiler.tableWidget.setItem(i, j, QTableWidgetItem(item))
        except FileNotFoundError:
            print("bilgi.txt dosyası bulunamadı.")