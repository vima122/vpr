# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'picture.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(160, 500, 231, 31))
        self.startButton.setObjectName("startButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 171, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.timeChet = QtWidgets.QLineEdit(self.centralwidget)
        self.timeChet.setGeometry(QtCore.QRect(460, 0, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.timeChet.setFont(font)
        self.timeChet.setReadOnly(True)
        self.timeChet.setObjectName("timeChet")
        self.timerBar = QtWidgets.QProgressBar(self.centralwidget)
        self.timerBar.setGeometry(QtCore.QRect(0, 0, 351, 61))
        self.timerBar.setMaximum(429)
        self.timerBar.setProperty("value", 0)
        self.timerBar.setTextVisible(False)
        self.timerBar.setObjectName("timerBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 72, 520, 190))
        self.pushButton.setIconSize(QtCore.QSize(520, 190))
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 270, 320, 221))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("voice-search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(312, 215))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Готово"))
        self.label_2.setText(_translate("MainWindow", "Времени осталось:"))
        self.timeChet.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить изображение"))
