from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from bilgi import Ui_MainWindow 
class BilgiPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.kiralamalariYukle()
        self.ui.pushButton.clicked.connect(self.kiralamayiIptalEt)
        self.ui.pushButton_2.clicked.connect(self.gericik)
        self.listele()



    def listele(self):
        header = self.ui.tableWidget.horizontalHeader() 
        for i in range(self.ui.tableWidget.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setDefaultSectionSize(124)
        self.ui.tableWidget.setColumnWidth(2,170)



        

    def kiralamalariYukle(self):
        
        try:
            with open('userinfo.txt', 'r') as file:
                kiralamalar = [line.strip().split(',') for line in file.readlines()]
                
            self.ui.tableWidget.setRowCount(len(kiralamalar))
            for i, kiralama in enumerate(kiralamalar):
            
                for j, item in enumerate(kiralama):
                    self.ui.tableWidget.setItem(i, j, QTableWidgetItem(item))
        except FileNotFoundError:
            print("userinfo.txt dosyası bulunamadı.")

    def sabit(self):
        from home_Page import HomePage
        self.homeAc = HomePage() 
    def gericik(self):
        self.sabit()
        self.homeAc.show()
        self.close()



    def kiralamayiIptalEt(self):
        selectedRows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selectedRows:
            QMessageBox.warning(self, "Uyarı", "Lütfen iptal etmek istediğiniz kiralamayı seçin.")
            return
        
        kiralamalar = []
        with open('userinfo.txt', 'r') as file:
            kiralamalar = [line.strip().split(',') for line in file.readlines()]
        

        guncellenmis_kiralamalar = [kiralama for i, kiralama in enumerate(kiralamalar) if i not in [row.row() for row in selectedRows]]
        
        with open('userinfo.txt', 'w') as file:
            for kiralama in guncellenmis_kiralamalar:
                file.write(','.join(kiralama) + '\n')
        

        for selectedRow in sorted(selectedRows, reverse=True):
            self.ui.tableWidget.removeRow(selectedRow.row())

        QMessageBox.information(self, "Başarılı", "Seçilen kiralama başarıyla iptal edildi.")
  
        self.kiralamalariYukle()


