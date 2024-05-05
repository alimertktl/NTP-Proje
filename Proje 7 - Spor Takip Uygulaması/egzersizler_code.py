from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from egzersizler import Ui_MainWindow

class EgzersizPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.egzersizsayfa = Ui_MainWindow()
        self.egzersizsayfa.setupUi(self)