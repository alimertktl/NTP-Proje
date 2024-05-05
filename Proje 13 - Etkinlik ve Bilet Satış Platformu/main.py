from PyQt5.QtWidgets import QApplication
from home_code import HomePage

app = QApplication([])
window = HomePage()
window.show()
app.exec_()