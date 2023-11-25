import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget
from PyQt5.QtGui import QBrush, QPen, QPainter


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.combobox1 = QtWidgets.QComboBox(self)
        self.combobox2 = QtWidgets.QComboBox(self)
        self.button1 = QtWidgets.QPushButton(self)
        self.title = "PyQt5 mouseEv"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 500

        self.points = []

        self.window()
        self.combobox_1()
        self.button_1()
        self.combobox_2()

    def window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

    def combobox_1(self):
        self.combobox1.setGeometry(400, 450, 70, 20)
        self.combobox1.addItem("")
        self.combobox1.addItem("")
        self.combobox1.addItem("")
        self.combobox1.setItemText(0, "Red")
        self.combobox1.setItemText(1, "Green")
        self.combobox1.setItemText(2, "Blue")

    def button_1(self):
        self.button1.setText('Accept')
        self.button1.move(300, 450)
        self.button1.adjustSize()
        self.button1.clicked.connect(self.disable)

    def disable(self):
        self.combobox1.setEnabled(False)
        self.combobox2.setEnabled(False)
        self.button1.setEnabled(False)

    def enable(self):
        self.combobox1.setEnabled(True)
        self.combobox2.setEnabled(True)
        self.button1.setEnabled(True)

    def combobox_2(self):
        self.combobox2.setGeometry(400, 430, 70, 20)
        self.combobox2.addItem("")
        self.combobox2.addItem("")
        self.combobox2.addItem("")
        self.combobox2.setItemText(0, "3")
        self.combobox2.setItemText(1, "5")
        self.combobox2.setItemText(2, "7")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Space:
            self.clear_all()
            self.enable()
            self.update()

    def clear_all(self):
        self.points = []
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            point = event.pos()
            self.points.append(point)
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        color = self.combobox1.currentText()
        width = self.combobox2.currentText()
        if color == 'Red':
            color = Qt.red
        elif color == 'Green':
            color = Qt.green
        elif color == 'Blue':
            color = Qt.blue
        if width == '3':
            width = 3
        elif width == '5':
            width = 5
        elif width == '7':
            width = 7
        pen = QPen(color, width)
        painter.setPen(pen)
        for point in self.points:
            painter.drawPoint(point)


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
