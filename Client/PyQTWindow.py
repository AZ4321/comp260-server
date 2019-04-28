from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QPlainTextEdit)
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Enter', self)
        self.btn.move(218, 194)

        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("Text goes here\n")
        self.b.move(10, 195)
        self.b.resize(200, 20)

        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("Text goes here\n")
        self.b.move(10, 195)
        self.b.resize(200, 20)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('MUD')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

