from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Giris(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-50, 0, 1321, 921))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        
        self.groupBox_title = QtWidgets.QGroupBox(self.widget)
        self.groupBox_title.setGeometry(QtCore.QRect(100, 60, 781, 81))
        self.groupBox_title.setStyleSheet("QGroupBox {\n"
"    border: 2px solid rgb(0, 85, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QGroupBox:title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_title.setTitle("")
        self.groupBox_title.setObjectName("groupBox_title")
        
        self.label_5 = QtWidgets.QLabel(self.groupBox_title)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 781, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("KİŞİSEL SAĞLIK TAKİBİ KAYIT BÖLÜMÜ")
        
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(100, 160, 781, 321))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 2px solid rgb(0, 85, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QGroupBox:title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(173, 216, 230);\n"
                                  "border-radius: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(173, 216, 230);\n"
                                  "border-radius: 10px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(173, 216, 230);\n"
                                  "border-radius: 10px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(173, 216, 230);\n"
                                  "border-radius: 10px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        
        self.lineEdit_isim = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_isim.setGeometry(QtCore.QRect(250, 40, 261, 31))
        self.lineEdit_isim.setObjectName("lineEdit_isim")
        
        self.lineEdit_soyisim = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_soyisim.setGeometry(QtCore.QRect(250, 110, 261, 31))
        self.lineEdit_soyisim.setObjectName("lineEdit_soyisim")
        
        self.comboBox_yas = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_yas.setGeometry(QtCore.QRect(250, 180, 261, 31))
        self.comboBox_yas.setObjectName("comboBox_yas")
        for i in range(18, 101):  
            self.comboBox_yas.addItem(str(i))
        
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(250, 250, 261, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Erkek")
        self.comboBox.addItem("Kadın")
        
        self.pushButton_giris = QtWidgets.QPushButton(self.widget)
        self.pushButton_giris.setGeometry(QtCore.QRect(275, 500, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_giris.setFont(font)
        self.pushButton_giris.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                             "border-radius: 25px;\n"
                                             "color: rgb(255, 255, 255);")
        self.pushButton_giris.setObjectName("pushButton_giris")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kişisel Sağlık Takibi"))
        self.label.setText(_translate("MainWindow", "İsim :"))
        self.label_2.setText(_translate("MainWindow", "Soyisim :"))
        self.label_3.setText(_translate("MainWindow", "Yaş :"))
        self.label_4.setText(_translate("MainWindow", "Cinsiyet :"))
        self.pushButton_giris.setText(_translate("MainWindow", "Giriş Yap"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Giris()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
