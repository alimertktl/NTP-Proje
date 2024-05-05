from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 461, 341))
        self.label_4.setStyleSheet("background-color: rgb(59, 57, 54);\n"
                                    "border-radius:20\n"
                                    "")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 40, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(59, 57, 54);\n"
                                    "color:White")
        self.label_3.setObjectName("label_3")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(175, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(170, 0, 127);\n"
                                        "color:white;\n"
                                        "border-radius:10;}\n"
                                        "QPushButton::hover{color:black}")
        self.pushButton.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tarihte Yer Edinmiş Şahsiyetler ve Olaylar Çalışması"))
        self.label_3.setText(_translate("MainWindow", "Tarihte Yer Edinmiş Şahsiyetler ve Olaylar Çalışması"))
        self.pushButton.setText(_translate("MainWindow", "GİRİŞ"))

