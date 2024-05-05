from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from a_takip import Ui_MainWindow

class TakipPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.takipsayfa = Ui_MainWindow()
        self.takipsayfa.setupUi(self)
        self.sporcuYukle()
        self.antremanYukle()
        self.takipsayfa.pushButton_5.clicked.connect(self.antremanArttir)
        self.takipsayfa.pushButton_4.clicked.connect(self.raporAl)

    def sporcuYenile(self):
        self.sporcuYukle()
    
    def antremanYenile(self):
        self.antremanYukle()


    def sporcuYukle(self):
        
        try:
            with open('sporcu.txt', 'r') as file:
                takipler = [line.strip().split(',') for line in file.readlines()]
                
            self.takipsayfa.tableWidget.setRowCount(len(takipler))
            for i, kiralama in enumerate(takipler):
            
                for j, item in enumerate(kiralama):
                    self.takipsayfa.tableWidget.setItem(i, j, QTableWidgetItem(item))
        except FileNotFoundError:
            print("sporcu.txt dosyası bulunamadı.")

    def antremanYukle(self):
        
        try:
            with open('antreman.txt', 'r') as file:
                takipler = [line.strip().split(',') for line in file.readlines()]
                
            self.takipsayfa.tableWidget_2.setRowCount(len(takipler))
            for i, kiralama in enumerate(takipler):
            
                for j, item in enumerate(kiralama):
                    self.takipsayfa.tableWidget_2.setItem(i, j, QTableWidgetItem(item))
        except FileNotFoundError:
            print("sporcu.txt dosyası bulunamadı.")

    def antremanArttir(self):
        selected_items = self.takipsayfa.tableWidget_2.selectedItems()
        if not selected_items:
            return 

        row = selected_items[0].row()  

        col = 5  
        current_item = self.takipsayfa.tableWidget_2.item(row, col)
        if current_item is not None:
            current_value = int(current_item.text())
            new_value = current_value + 1
            self.takipsayfa.tableWidget_2.setItem(row, col, QTableWidgetItem(str(new_value)))
        self.antremanKaydet()  

    def antremanKaydet(self):
        with open('antreman.txt', 'w') as file:
            for row in range(self.takipsayfa.tableWidget_2.rowCount()):
                row_data = []
                for col in range(self.takipsayfa.tableWidget_2.columnCount()):
                    item = self.takipsayfa.tableWidget_2.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('0')
                file.write(','.join(row_data) + '\n')


    def raporAl(self):
        toplam_gun = 0
        for row in range(self.takipsayfa.tableWidget_2.rowCount()):
            item = self.takipsayfa.tableWidget_2.item(row, 5)
            if item and item.text().isdigit(): 
                toplam_gun += int(item.text())
    
        QMessageBox.information(self, "Antreman Raporu", f"Sporcuların yaptığı toplam antreman günü: {toplam_gun}")


    def verileriKaydet(self):
        with open('antreman_data.txt', 'w') as file:
            for row in range(self.takipsayfa.tableWidget_2.rowCount()):
                row_data = []
                for col in range(self.takipsayfa.tableWidget_2.columnCount()):
                    item = self.takipsayfa.tableWidget_2.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('0')  # Eğer hücre boşsa 0 olarak kaydet
                file.write(','.join(row_data) + '\n')
