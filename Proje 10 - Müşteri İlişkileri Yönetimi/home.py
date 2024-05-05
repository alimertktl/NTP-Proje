from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 601)
        MainWindow.setStyleSheet("#centralwidget{background-color: rgb(127, 153, 255);}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 821, 521))
        self.label.setStyleSheet("background-color: rgb(174, 34, 53);\n"
"border-radius:15\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(8, 196, 255);\n"
"color:white;\n"
"border-radius:10;}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 34, 53);}\n"
"\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setIndent(-1)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 150, 201, 41))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_2.setMaxLength(25)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 230, 201, 41))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_4.setMaxLength(11)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 310, 201, 41))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(5)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(460, 230, 201, 41))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_5.setMaxLength(20)
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setDragEnabled(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(460, 310, 201, 41))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setMaxLength(4)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setDragEnabled(False)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(460, 150, 201, 41))
        self.lineEdit_7.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_7.setMaxLength(3)
        self.lineEdit_7.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_7.setClearButtonEnabled(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setIndent(-1)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 380, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(125, 117, 116);\n"
"color:white;\n"
"border-radius:10;}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 34, 53);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 380, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"QPushButton{\n"
"color:white;\n"
"    background-color: rgb(125, 117, 116);\n"
"border-radius:10;}\n"
"QPushButton::hover{background-color: rgb(0, 34, 53);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 490, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(8, 196, 255);\n"
"color:white;\n"
"border-radius:10;}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 34, 53);}\n"
"\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "İKU CRM Sistemi"))
        self.pushButton.setText(_translate("MainWindow", "Destek Talebi Oluştur"))
        self.label_3.setText(_translate("MainWindow", "Müşteri Ekleme "))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Müşteri Adı"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Müşteri İletişim Bilgisi"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Müşteri Cinsiyeti"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Ürün Adı"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Ürün Kodu"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Satış Numarası"))
        self.label_4.setText(_translate("MainWindow", "Satış Ekleme"))
        self.pushButton_3.setText(_translate("MainWindow", "Satış Ekle"))
        self.pushButton_4.setText(_translate("MainWindow", "Müşteri Ekle"))
        self.pushButton_2.setText(_translate("MainWindow", "Destek Talepleri Ve Satılan Ürünler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
