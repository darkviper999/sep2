import sys
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("rabbit.png")
        self.tu = QPixmap("tu.jpg")
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())


