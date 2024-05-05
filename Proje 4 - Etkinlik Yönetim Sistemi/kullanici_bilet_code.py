from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from kullanici_bilet import Ui_MainWindow  
from  bilgi_code import BilgiPage

class KullaniciBiletWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.buy_ticket)
        self.ui.pushButton_2.clicked.connect(self.add_user)
        self.ui.pushButton_5.clicked.connect(self.etkinlikler)
        self.ui.pushButton_4.clicked.connect(self.bilgigit)
        
        self.bilgiAc = BilgiPage()
        self.secilen_etkinlik = "" 

    def bilgigit(self):
        self.bilgiAc.show()
        self.close()

    def buy_ticket(self):
        participant_name = self.ui.lineEdit.text()
        ticket_number = self.ui.lineEdit_6.text()
        if participant_name and ticket_number and self.secilen_etkinlik:  
            QMessageBox.information(self, "Bilgi", f"Bilet satın alındı!\nKatılımcı: {participant_name}\nBilet No: {ticket_number}\nEtkinlik: {self.secilen_etkinlik}")
            with open("bilgi.txt", "a", encoding='utf-8') as file:
                file.write(f"{self.secilen_etkinlik},{participant_name},{ticket_number}\n")  
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm bilgileri (katılımcı adı, bilet numarası ve etkinlik) girin.")

    def add_user(self):
        participant_name = self.ui.lineEdit.text()
        participant_no = self.ui.lineEdit_2.text()
        event_name = self.ui.lineEdit_3.text()
        if participant_name and participant_no and event_name:
            QMessageBox.information(self, "Başarı", f"Kullanıcı eklendi!\nAd: {participant_name}\nNo: {participant_no}\nEtkinlik: {event_name}")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def etkinlikler(self):
        selected_items = self.ui.tableWidget.selectedItems()
        if selected_items:
            self.secilen_etkinlik = selected_items[0].text()
            QMessageBox.information(self, "Bilgi", f"Etkinlik seçildi: {self.secilen_etkinlik}")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir etkinlik seçin!")
