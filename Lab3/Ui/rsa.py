# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 897)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 110, 61, 21))
        self.label.setObjectName("label")
        self.PlainText_txt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PlainText_txt.setGeometry(QtCore.QRect(190, 110, 371, 71))
        self.PlainText_txt.setObjectName("PlainText_txt")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 61, 21))
        self.label_2.setObjectName("label_2")
        self.CipherText_txt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.CipherText_txt.setGeometry(QtCore.QRect(190, 230, 371, 71))
        self.CipherText_txt.setObjectName("CipherText_txt")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Sig_txt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Sig_txt.setGeometry(QtCore.QRect(710, 230, 371, 71))
        self.Sig_txt.setObjectName("Sig_txt")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 110, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 230, 61, 21))
        self.label_5.setObjectName("label_5")
        self.Infor_txt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Infor_txt.setGeometry(QtCore.QRect(710, 110, 371, 71))
        self.Infor_txt.setObjectName("Infor_txt")
        self.En_btn = QtWidgets.QPushButton(self.centralwidget)
        self.En_btn.setGeometry(QtCore.QRect(240, 370, 75, 23))
        self.En_btn.setObjectName("En_btn")
        self.De_btn = QtWidgets.QPushButton(self.centralwidget)
        self.De_btn.setGeometry(QtCore.QRect(410, 370, 75, 23))
        self.De_btn.setObjectName("De_btn")
        self.Sign_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Sign_btn.setGeometry(QtCore.QRect(750, 370, 75, 23))
        self.Sign_btn.setObjectName("Sign_btn")
        self.Verify_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Verify_btn.setGeometry(QtCore.QRect(930, 370, 75, 23))
        self.Verify_btn.setObjectName("Verify_btn")
        self.Gen_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Gen_btn.setGeometry(QtCore.QRect(660, 40, 91, 23))
        self.Gen_btn.setObjectName("Gen_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
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
        self.label.setText(_translate("MainWindow", "Plain Text:"))
        self.label_2.setText(_translate("MainWindow", "CipherText:"))
        self.label_3.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_4.setText(_translate("MainWindow", "Infomation"))
        self.label_5.setText(_translate("MainWindow", "Signature"))
        self.En_btn.setText(_translate("MainWindow", "Encrypt"))
        self.De_btn.setText(_translate("MainWindow", "Decrypt"))
        self.Sign_btn.setText(_translate("MainWindow", "Sign"))
        self.Verify_btn.setText(_translate("MainWindow", "Verify"))
        self.Gen_btn.setText(_translate("MainWindow", "Generate Keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
