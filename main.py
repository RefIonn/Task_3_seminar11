import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QBrush, QPen, QPainter


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.combobox1 = QtWidgets.QComboBox(self)

        self.title = "PyQt5 mouseEvent"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 500

        self.check = False
        self.mouse_x = 0
        self.mouse_y = 0

        self.combobox_width()
        self.window()

    def window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def combobox_width(self):
        self.combobox1.setGeometry(150, 30, 50, 25)
        self.combobox1.setObjectName("Choose")
        self.combobox1.addItem("")
        self.combobox1.addItem("")
        self.combobox1.addItem("")
        self.combobox1.setItemText(0, "1")
        self.combobox1.setItemText(1, "3")
        self.combobox1.setItemText(2, "5")

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.check = True
            self.update()

    def mouseMoveEvent(self, event):
        coordinate = []
        self.mouse_x = event.x()
        self.mouse_y = event.y()
        coordinate.append(f"X - {self.mouse_x}")
        coordinate.append(f"Y - {self.mouse_y}")
        print(f"Координаты новой точки:{coordinate}")

    def paintEvent(self, event):
        wid = self.combobox1.currentText()
        painter = QPainter(self)
        if self.check:
            if wid == "1":
                width = 1
            elif wid == "3":
                width = 3
            elif wid == "5":
                width = 5
            pen = QPen(Qt.black)
            pen.setWidth(width)
            pen.setStyle(Qt.SolidLine)
            painter.setPen(pen)
            painter.drawPoint(self.mouse_x, self.mouse_y)


def application():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
