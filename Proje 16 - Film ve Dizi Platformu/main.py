from PyQt5.QtWidgets import QApplication
from giris_page import GirisSayfası


app = QApplication([])
pencere = GirisSayfası()
pencere.show()
app.exec_()