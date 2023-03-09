from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, 
                             QWidget, QGridLayout)
from tinydb import TinyDB, Query
import os
import time
from main_0start import Window as start
from main_1audio import Window as audio
from main_2reading import Window as reading
from main_3picture import Window as picture
from main_4titles import Window as titles
from main_5grammar import Window as grammar
from main_6words import Window as words
t = None
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.button_start = QPushButton('Open start')
        self.button_start.clicked.connect(self.open_start)
        self.button_audio = QPushButton('Open audio')
        self.button_audio.clicked.connect(self.open_audio)
        self.button_reading = QPushButton('Open reading')
        self.button_reading.clicked.connect(self.open_reading)
        self.button_picture = QPushButton('Open picture')
        self.button_picture.clicked.connect(self.open_picture)
        self.button_titles = QPushButton('Open titles')
        self.button_titles.clicked.connect(self.open_titles)
        self.button_grammar = QPushButton('Open grammar')
        self.button_grammar.clicked.connect(self.open_grammar)
        self.button_words = QPushButton('Open words')
        self.button_words.clicked.connect(self.open_words)

        self.grid = QGridLayout(centralWidget)
        self.grid.addWidget(self.button_start, 0, 0)    
        self.grid.addWidget(self.button_audio, 0, 1)        
        self.grid.addWidget(self.button_reading, 0, 2)
        self.grid.addWidget(self.button_picture, 0, 3)
        self.grid.addWidget(self.button_titles, 0, 4)
        self.grid.addWidget(self.button_grammar, 0, 5)
        self.grid.addWidget(self.button_words, 0, 6)
    
    def open_start(self):
        global t
        os.system("mkdir data")
        self.mainStart = start(self)
        t = "Start"
        self.mainStart.startButton.clicked.connect(self.close)
        self.mainStart.show()
        self.hide()
    def open_audio(self):
        global t
        self.mainAudio = audio(self)
        t = "Audio"
        self.mainAudio.startButton.clicked.connect(self.close)
        self.mainAudio.show()
        self.hide()
            
    def open_reading(self):
        global t
        self.mainReading = reading(self)
        t = "Reading"
        self.mainReading.startButton.clicked.connect(self.close)
        self.mainReading.show()
        self.hide()

    def open_picture(self):
        global t
        self.mainPicture = picture(self)
        t = "Picture"
        self.mainPicture.startButton.clicked.connect(self.close)
        self.mainPicture.show()
        self.hide()
       
    def open_titles(self):
        global t
        self.mainTitles = titles(self)
        t = "Titles"
        self.mainTitles.startButton.clicked.connect(self.close)
        self.mainTitles.show()
        self.hide()
        
    def open_grammar(self):
        global t
        self.mainGrammar = grammar(self)
        t = "Grammar"
        self.mainGrammar.startButton.clicked.connect(self.close)
        self.mainGrammar.show()
        self.hide()
    
    def open_words(self):
        global t
        self.mainWords = words(self)
        t = "Words"
        self.mainWords.startButton.clicked.connect(self.close)
        self.mainWords.show()
        self.hide()
    def close(self):
        global db
        global t
        
        if t == "Start":
            db = TinyDB("data/data.json")
            self.mainStart.hide()
        if t == "Audio":
            db.insert({'name':"audio",'data': [self.mainAudio.lineEdit.text(),self.mainAudio.lineEdit_2.text(),self.mainAudio.lineEdit_3.text(),self.mainAudio.lineEdit_4.text(),self.mainAudio.lineEdit_5.text(),self.mainAudio.lineEdit_6.text(),self.mainAudio.lineEdit_7.text(),self.mainAudio.lineEdit_8.text(),self.mainAudio.lineEdit_9.text(),self.mainAudio.lineEdit_10.text()]})
            self.mainAudio.hide()
        if t == "Reading":
            db.insert({'name':"reading",'data': [self.mainReading.textEdit.toPlainText()]})
            self.mainReading.hide()
        if t == "Picture":
            self.mainPicture.hide()
        if t == "Titles":
            db.insert({'name':"titles",'data': [self.mainTitles.textEdit.toPlainText(),self.mainTitles.lineEdit.text(),self.mainTitles.lineEdit_2.text(),self.mainTitles.lineEdit_3.text(),self.mainTitles.lineEdit_4.text(),self.mainTitles.lineEdit_5.text()]})
            self.mainTitles.hide()
        if t == "Grammar":
            db.insert({'name':"grammar",'data': [self.mainGrammar.lineEdit.text(),self.mainGrammar.lineEdit_2.text(),self.mainGrammar.lineEdit_3.text(),self.mainGrammar.lineEdit_4.text(),self.mainGrammar.lineEdit_5.text()]})
            self.mainGrammar.hide()
        if t == "Words":
            db.insert({'name':"words",'data': [self.mainWords.lineEdit.text(),self.mainWords.lineEdit_2.text(),self.mainWords.lineEdit_3.text(),self.mainWords.lineEdit_4.text(),self.mainWords.lineEdit_5.text()]})
            self.mainWords.hide()
        self.show()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("main.py")
    w.show()
    sys.exit(app.exec())        
