from Simple_drawing_window import *

class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        super().__init__()
        self.rabbit = QPixmap("rabbit.png")
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,0, 180*16)
        
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
