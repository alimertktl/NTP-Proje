import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from egzersiz_py import Ui_Egzersiz

class EgzersizPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Egzersiz()
        self.ui.setupUi(self)

        # Egzersiz ekleme ve silme butonlarına tıklama olayları
        self.ui.pushButton_egzersizekle.clicked.connect(self.egzersiz_ekle)
        self.ui.pushButton_egzersizekle_2.clicked.connect(self.egzersiz_sil)
        self.ui.pushButton_egzersizekle_3.clicked.connect(self.geri)

        # TableWidget hücrelerine tıklandığında olaylar
        self.ui.tableWidget.cellClicked.connect(self.show_cell_content)

    def egzersiz_ekle(self):
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)

    def egzersiz_sil(self):
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Uyarı", "Lütfen silmek istediğiniz satırı seçin.")
            return

        for row in reversed(selected_rows):
            self.ui.tableWidget.removeRow(row.row())

    def show_cell_content(self, row, column):
        item = self.ui.tableWidget.item(row, column)
        if item is not None:
            content = item.text()
            self.show_popup(content)

    def show_popup(self, content):
        popup = QMessageBox()
        popup.setWindowTitle("Egzersiz Açıklaması")
        popup.setText(content)
        popup.setIcon(QMessageBox.Information)
        popup.exec_()

    def geri(self):
        self.hide()  # Egzersiz sayfasını gizle
        if self.parent():
            self.parent().show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EgzersizPage()
    window.show()
    sys.exit(app.exec_())
