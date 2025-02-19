import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from map_func import scale
from os import remove

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel(self)

        self.img = scale()

        pixmap = QPixmap(self.img)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

    def closeEvent(self):
        remove(self.img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())