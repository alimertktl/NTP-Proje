from PyQt5.QtWidgets import QApplication
from randevu_home_kodu import HomePage

app = QApplication([])
window = HomePage()
window.show()
app.exec_()