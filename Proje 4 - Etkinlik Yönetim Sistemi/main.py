from PyQt5 import QtWidgets
from kullanici_bilet_code import KullaniciBiletWindow  

if __name__ == "__main__":  
    import sys
    app = QtWidgets.QApplication(sys.argv)
    etkinlik_window = KullaniciBiletWindow()  
    etkinlik_window.show()
    sys.exit(app.exec_())

