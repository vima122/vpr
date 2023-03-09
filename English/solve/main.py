from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, 
                             QWidget, QGridLayout)
from tinydb import TinyDB, Query
import os
import time
import subprocess
from main_0start import Window as start
from main_1audio import Window as audio
from main_2reading import Window as reading
from main_3picture import Window as picture
from main_4titles import Window as titles
from main_5grammar import Window as grammar
from main_6words import Window as words
c = 0
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
        global c
        global t
        os.system("mkdir data"+str(c)+"")
        if c == 0:
            c = 1
            self.mainStart = start(self)
            t = "Start"
            self.mainStart.startButton.clicked.connect(self.close)
            self.mainStart.slushButton.clicked.connect(self.slush)
            self.mainStart.microphoneButton.clicked.connect(self.micro)
            self.mainStart.show()
            self.hide()
    def slush(self):
        f = 5
        p = subprocess.Popen(["py","sub.py","-t 1","-c "+str(self.mainStart.codeLine.text())+""], stdout=subprocess.PIPE)
        for i in range(500):
            time.sleep(0.01)
            self.mainStart.timerBar.setValue(i)
            self.mainStart.timeChet.setText(str(int(f)))
            f -= 0.01
        self.mainStart.timerBar.setValue(0)
    def micro(self):
        global q
        f = 5
        p = subprocess.Popen(["py","sub.py","-t "+q+" ","-c "+str(self.mainStart.codeLine.text())+""], stdout=subprocess.PIPE)
        for i in range(500):
            time.sleep(0.01)
            self.mainStart.timerBar.setValue(i)
            self.mainStart.timeChet.setText(str(int(f)))
            f -= 0.01
        self.mainStart.timerBar.setValue(0)
    def open_audio(self):
        global c
        global t
        global p
        if c == 1:
            c = 2
            self.mainAudio = audio(self)
            t = "Audio"
            p = subprocess.Popen(["py","sub.py","-t 2 ","-c "+str(self.mainStart.codeLine.text())+""], stdout=subprocess.PIPE)
            db = TinyDB("data.json")
            d = db.search(Query().name == 'audio')[0]
            self.mainAudio.label.setText(str(d["data"][0]))
            self.mainAudio.label_3.setText(str(d["data"][1]))
            self.mainAudio.label_4.setText(str(d["data"][2]))
            self.mainAudio.label_5.setText(str(d["data"][3]))
            self.mainAudio.label_6.setText(str(d["data"][4]))
            for i in range(3):
            	self.mainAudio.comboBox.setItemText(i+1,str(d["data"][5]).split(";")[i])
            for i in range(3):
            	self.mainAudio.comboBox_2.setItemText(i+1,str(d["data"][6]).split(";")[i])
            for i in range(3):
            	self.mainAudio.comboBox_3.setItemText(i+1,str(d["data"][7]).split(";")[i])
            for i in range(3):
            	self.mainAudio.comboBox_4.setItemText(i+1,str(d["data"][8]).split(";")[i])
            for i in range(3):
            	self.mainAudio.comboBox_5.setItemText(i+1,str(d["data"][9]).split(";")[i])
            self.mainAudio.startButton.clicked.connect(self.close)
            self.mainAudio.show()
            self.hide()
            
    def open_reading(self):
        global c
        global t
        global q
        q = 4
        if c == 2:
            c = 3
            self.mainReading = reading(self)
            t = "Reading"
            db = TinyDB("data.json")
            d = db.search(Query().name == 'reading')[0]
            self.mainReading.textBrowser.setText(str(d["data"][0]))
            self.mainReading.startButton.clicked.connect(self.close)
            self.mainStart.microphoneButton.clicked.connect(self.micro)
            self.mainReading.show()
            self.hide()

    def open_picture(self):
        global c
        global t
        global q
        q = 5
        if c == 3:
            c = 4
            self.mainPicture = picture(self)
            t = "Picture"
            self.mainPicture.startButton.clicked.connect(self.close)
            self.mainStart.microphoneButton.clicked.connect(self.micro)
            self.mainPicture.show()
            self.hide()
       
    def open_titles(self):
        global c
        global t
        if c == 4:
            c = 5
            self.mainTitles = titles(self)
            t = "Titles"
            db = TinyDB("data.json")
            d = db.search(Query().name == 'titles')[0]
            self.mainTitles.textBrowser.setText(str(d["data"][0]))
            self.mainTitles.startButton.clicked.connect(self.close)
            self.mainTitles.show()
            self.hide()
        
    def open_grammar(self):
        global c
        global t
        if c == 5:
            c = 6
            self.mainGrammar = grammar(self)
            t = "Grammar"
            self.mainGrammar.startButton.clicked.connect(self.close)
            self.mainGrammar.show()
            self.hide()
    
    def open_words(self):
        global c
        global t
        if c == 6:
            c = 7
            self.mainWords = words(self)
            t = "Words"
            self.mainWords.startButton.clicked.connect(self.close)
            self.mainWords.show()
            self.hide()
    def close(self):
        global db
        global t
        global p
        
        if t == "Start":
            db = TinyDB("data"+str(self.mainStart.codeLine.text())+"/"+str(self.mainStart.codeLine.text())+".json")
            db.insert({'name':"code",'data': str(self.mainStart.codeLine.text())})
            self.mainStart.hide()
        if t == "Audio":
            db.insert({'name':"audio",'data': [self.mainAudio.comboBox.currentIndex(),self.mainAudio.comboBox_2.currentIndex(),self.mainAudio.comboBox_3.currentIndex(),self.mainAudio.comboBox_4.currentIndex(),self.mainAudio.comboBox_5.currentIndex()]})
            self.mainAudio.hide()
            p.terminate()
        if t == "Reading":
            self.mainReading.hide()
        if t == "Picture":
            self.mainPicture.hide()
        if t == "Titles":
            db.insert({'name':"titles",'data': [self.mainTitles.comboBox.currentIndex(),self.mainTitles.comboBox_2.currentIndex(),self.mainTitles.comboBox_3.currentIndex(),self.mainTitles.comboBox_4.currentIndex(),self.mainTitles.comboBox_5.currentIndex()]})
            self.mainTitles.hide()
        if t == "Grammar":
            db.insert({'name':"grammar",'data': [self.mainGrammar.comboBox.currentIndex(),self.mainGrammar.comboBox_2.currentIndex(),self.mainGrammar.comboBox_3.currentIndex(),self.mainGrammar.comboBox_4.currentIndex(),self.mainGrammar.comboBox_5.currentIndex()]})
            self.mainGrammar.hide()
        if t == "Words":
            db.insert({'name':"words",'data': [self.mainWords.comboBox.currentIndex(),self.mainWords.comboBox_2.currentIndex(),self.mainWords.comboBox_3.currentIndex(),self.mainWords.comboBox_4.currentIndex(),self.mainWords.comboBox_5.currentIndex()]})
            self.mainWords.hide()
        self.show()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("main.py")
    w.show()
    sys.exit(app.exec())        
