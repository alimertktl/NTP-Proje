from PyQt5.QtWidgets import QApplication
from spor_home_code import SporPage

app = QApplication([])
window = SporPage()
window.show()
app.exec_()