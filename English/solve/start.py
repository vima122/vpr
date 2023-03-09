# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 535)
        MainWindow.setFixedSize(535, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.startLabel = QtWidgets.QLabel(self.centralwidget)
        self.startLabel.setGeometry(QtCore.QRect(130, 40, 431, 91))
        self.startLabel.setObjectName("startLabel")
        self.microphoneButton = QtWidgets.QPushButton(self.centralwidget)
        self.microphoneButton.setGeometry(QtCore.QRect(60, 150, 411, 311))
        self.microphoneButton.setAutoFillBackground(False)
        self.microphoneButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("voice-search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.microphoneButton.setIcon(icon)
        self.microphoneButton.setIconSize(QtCore.QSize(300, 300))
        self.microphoneButton.setCheckable(False)
        self.microphoneButton.setFlat(True)
        self.microphoneButton.setObjectName("microphoneButton")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(160, 500, 231, 31))
        self.startButton.setObjectName("startButton")
        self.codeLine = QtWidgets.QSpinBox(self.centralwidget)
        self.codeLine.setGeometry(QtCore.QRect(210, 100, 111, 22))
        self.codeLine.setWrapping(False)
        self.codeLine.setAlignment(QtCore.Qt.AlignCenter)
        self.codeLine.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.codeLine.setMaximum(99999)
        self.codeLine.setObjectName("codeLine")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 171, 21))
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
        self.slushButton = QtWidgets.QPushButton(self.centralwidget)
        self.slushButton.setGeometry(QtCore.QRect(160, 472, 231, 31))
        self.slushButton.setObjectName("slushButton")
        self.timerBar = QtWidgets.QProgressBar(self.centralwidget)
        self.timerBar.setGeometry(QtCore.QRect(0, 0, 351, 61))
        self.timerBar.setMaximum(429)
        self.timerBar.setProperty("value", 0)
        self.timerBar.setTextVisible(False)
        self.timerBar.setObjectName("timerBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startLabel.setText(_translate("MainWindow", "Запишите и продиктуйте по цифрам код участника"))
        self.startButton.setText(_translate("MainWindow", "Начать выполнение заданий"))
        self.label_2.setText(_translate("MainWindow", "Времени осталось:"))
        self.timeChet.setText(_translate("MainWindow", "0"))
        self.slushButton.setText(_translate("MainWindow", "Прослушать код"))
