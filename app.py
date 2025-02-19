import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QKeyEvent
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from map_func import scale
from os import remove

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel(self)
        self.spn = ['0.002', '0.002']

        self.img, self.spn = scale(self.spn)

        pixmap = QPixmap(self.img)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_PageUp:
            self.img, self.spn = scale(self.spn, change=True, dir='up')
        elif e.key() == Qt.Key.Key_PageDown:
            self.img, self.spn = scale(self.spn, change=True, dir='down')
        else:
            super().keyPressEvent(e)

    def closeEvent(self):
        remove(self.img)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())