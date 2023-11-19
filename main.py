import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QMainWindow
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from UI import Ui_MainWindow
import random


class CircleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black']

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.verticalLayout.addWidget(self.view)

        self.btnCreateCircle.clicked.connect(self.createCircle)

    def createCircle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.view.width() - diameter)
        y = random.randint(0, self.view.height() - diameter)

        circle = QGraphicsEllipseItem(x, y, diameter, diameter)
        circle.setBrush(QColor(random.choice(self.colors)))
        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleApp()
    ex.show()
    sys.exit(app.exec_())