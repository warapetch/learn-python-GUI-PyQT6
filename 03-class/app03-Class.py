from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("PyQT6 หัวข้อที่ 3")
        self.setFont(QFont("Bai Jamjuree",15))
        self.resize(680,480)

        # set UI
        lb1 = QLabel("สวัสดีครับ")
        lb1.setGeometry(0,5,150,30)

        btn1 = QPushButton("คลิกหน่อย")        
        btn1.setGeometry(0,40,150,30)
        
        # setParent
        lb1.setParent(self)
        btn1.setParent(self)



def main():
    app = QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()