# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titles.ui'
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
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(6, 72, 501, 321))
        self.textBrowser.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(15, 390, 501, 101))
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 420, 491, 61))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.comboBox_2 = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setDuplicatesEnabled(False)
        self.comboBox_3.setFrame(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setDuplicatesEnabled(False)
        self.comboBox_4.setFrame(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setDuplicatesEnabled(False)
        self.comboBox_5.setFrame(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "?????????????????? ??????????????"))
        self.label_2.setText(_translate("MainWindow", "?????????????? ????????????????:"))
        self.timeChet.setText(_translate("MainWindow", "0"))
        self.textBrowser.setText(_translate("MainWindow", "This text deals with ???\n"
"1.???Out-of-town shopping.\n"
"2.???Bargain hunters.\n"
"3.???The best shopping street.\n"
"4.???A convenient way of paying.\n"
"5.???Internet shopping.\n"
"6.???The key to success.\n"
"\n"
"A.???Mary has already started doing her Christmas shopping on-line. She usually spends about ??300 on presents\n"
" and pays for them on her debit card. She is buying food from supermarket shopping services and has ordered\n"
" books and CDs from on-line bookshops. Buying on-line saves her a lot of money, and it???s a lot nicer staying at home than having to go out in the High Street.\n"
"B.???A recent survey has shown that the busiest shopping street in the world is in Warsaw. It???s called Nowy Swiat,\n"
" which means New World. An incredible 15,000 Poles walk down this main street every hour. It is a lovely place\n"
" to shop. It is now possible to buy almost everything in Warsaw. There are a lot of shops from the West, but the interesting thing is that Polish manufacturers are now producing high quality goods.\n"
"C.???Many small street and comer shops are closing because people prefer to drive to shopping complex outside\n"
" town. There they can park their cars without any problems and do all their shopping in one place. In a British\n"
" shopping complex, you usually find a supermarket, a branch of most of the chain-stores, some smaller shops, and a few cafes. Most of the new shopping complexes are built near big roads.\n"
"D.???Mail-order shopping has become very popular because it saves time. Shoppers use credit cards to pay for\n"
" something over the telephone after they have seen it advertised in a mail-order catalogue, on TV,\n"
" or in a newspaper or magazine. A number of mail-order companies accept phone orders twenty-four hours a day and most have toll-free numbers.\n"
"E.???Many Americans like sales. They shop at stores that sell goods at a discount. An item on sale can cost as\n"
" little as hall the normal price. Sales are advertized in newspapers, on radio on TV, or by mail. Stores compete\n"
" with each other by reducing their prices and staying open in the evening. Many arc open seven days a week and sometimes until 10.00 at night"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????????"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
