import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from map_func import scale
from os import remove

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel(self)
        self.spn = ['0.002', '0.002']
        self.ll = ['37.530887', '55.703118']

        self.img, self.spn, self.ll = scale(self.spn, self.ll)

        pixmap = QPixmap(self.img)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_PageUp:
            self.img, self.spn, self.ll = scale(self.spn, self.ll, change=True, dir='p_up')
        elif e.key() == Qt.Key.Key_PageDown:
            self.img, self.spn, self.ll = scale(self.spn, self.ll, change=True, dir='p_down')
        elif e.key() == Qt.Key.Key_Up:
            self.img, self.spn, self.ll = scale(self.spn, self.ll, change=True, dir='up')
        elif e.key() == Qt.Key.Key_Down:
            self.img, self.spn, self.ll = scale(self.spn, self.ll, change=True, dir='down')
        elif e.key() == Qt.Key.Key_Right:
            self.img, self.spn, self.ll = scale(self.spn, self.ll, change=True, dir='right')
        elif e.key() == Qt.Key.Key_Left:
            self.img, self.spn, self.ll = scale(self.spn, self.ll, change=True, dir='left')
        else:
            super().keyPressEvent(e)

    def closeEvent(self, event):
        remove(self.img)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())