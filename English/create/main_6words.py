from PyQt5.QtWidgets import QMainWindow, QApplication

# pyuic5 gui_rus.ui -o gui_rus.py
from words import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.parent = parent 

        self.setupUi(self)

    def closeEvent(self, event):
        self.hide()
        self.parent.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Window()
    w.setWindowTitle("main_mydesing1.py")
    w.show()
    sys.exit(app.exec_())