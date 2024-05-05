from PyQt5.QtWidgets import QApplication
from home_Page import HomePage

calistir = QApplication([])
pencere = HomePage()
pencere.show()
calistir.exec_()
