from Simple_drawing_window import *

class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        super().__init__()

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
##cookie
        p.setPen(QColor(168,101,9))
        p.setBrush(QColor(168,101,9))
        p.drawPie(50,150,100,100,0,360*16)
        p.setPen(QColor(77,31,10))
        p.setBrush(QColor(77,31,10))
        p.drawPie(100,175,10,10,0,360*16)
        p.drawPie(125,200,10,10,0,360*16)
        p.drawPie(133,188,10,10,0,360*16)
        p.drawPie(100,215,10,10,0,360*16)
        p.drawPie(76,222,10,10,0,360*16)
        p.drawPie(86,235,10,10,0,360*16)
        p.drawPie(59,216,10,10,0,360*16)
        p.drawPie(66,175,10,10,0,360*16)
        p.drawPie(68,168,10,10,0,360*16)
        p.drawPie(133,188,10,10,0,360*16)
        p.drawPie(79,213,10,10,0,360*16)
        p.drawPie(76,222,10,10,0,360*16)
        p.drawPie(86,235,10,10,0,360*16)
        p.drawPie(59,216,10,10,0,360*16)
##        p.setPen(QColor(255,127,0))


##        p.drawPolygon(
##            QPoint(50,200),QPoint(150,200),QPoint(100,400),
##            )
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()
        
def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window1()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
