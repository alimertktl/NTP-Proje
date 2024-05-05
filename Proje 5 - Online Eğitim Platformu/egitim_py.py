from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Arka plan rengi
        self.centralwidget.setStyleSheet("background-color: rgb(240, 240, 240);")

        # Çerçeve widget'i oluştur
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 170, 591, 281))
        self.frame.setStyleSheet("background-color: rgb(200, 200, 255); border: 2px solid black; border-radius: 10px;")

        self.pushButton_Giris = QtWidgets.QPushButton(self.frame)
        self.pushButton_Giris.setGeometry(QtCore.QRect(170, 210, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.pushButton_Giris.setFont(font)
        self.pushButton_Giris.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_Giris.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_Giris.setStyleSheet("background-color: rgb(255, 165, 0); border-radius: 15px;")
        self.pushButton_Giris.setObjectName("pushButton_Giris")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 41))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(200, 200, 255);\n"
                                  "border-radius: 10px;")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 151, 41))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; \n"
                                    "border-radius: 10px;\n"
                                    "background-color: rgb(200, 200, 255);")
        self.label_2.setObjectName("label_2")

        self.lineEdit_isim = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_isim.setGeometry(QtCore.QRect(190, 30, 371, 41))
        self.lineEdit_isim.setObjectName("lineEdit_isim")

        self.lineEdit_2_mail = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_mail.setGeometry(QtCore.QRect(190, 90, 371, 41))
        self.lineEdit_2_mail.setObjectName("lineEdit_2_mail")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 30, 641, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_isim, self.lineEdit_2_mail)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Giris.setText(_translate("MainWindow", "GİRİŞ YAP"))
        self.label.setText(_translate("MainWindow", "İsim Soyisim :"))
        self.label_2.setText(_translate("MainWindow", "Mail Adresi :"))
        self.label_3.setText(_translate("MainWindow", "İKÜ ONLİNE EĞİTİM PLATFORMU"))


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
