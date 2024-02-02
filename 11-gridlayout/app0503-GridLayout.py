from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import sys

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQT6 บทเรียน GridLayout")
        self.setFont(QFont("Bai Jamjuree",15))
        self.resize(650,580)
        self.setupUI()

    def setupUI(self):

        baseWidget = QFrame()

        # set Layout Grid เต็มจอ
        gridLayout = QGridLayout()

        # set UI
        btn01 = QPushButton("1")
        btn02 = QPushButton("2")
        btn03 = QPushButton("3")
        btn04 = QPushButton("4")
        btn05 = QPushButton("5")
        btn06 = QPushButton("6")
        btn07 = QPushButton("7")


        #2 
        btn01.setFixedSize(QSize(100,100))
        btn02.setFixedSize(QSize(200,315))
        btn03.setFixedSize(QSize(100,430))
        btn04.setFixedSize(QSize(100,200))
        btn05.setFixedSize(QSize(300,100))
        btn06.setFixedSize(QSize(415,100))
        btn07.setFixedSize(QSize(100,550))

        # Add เข้า Layout
        gridLayout.setVerticalSpacing(15)
        gridLayout.setHorizontalSpacing(10)
        gridLayout.addWidget(btn01,0,0)
        gridLayout.addWidget(btn02,0,1,3,0,Qt.AlignmentFlag.AlignTop)
        gridLayout.addWidget(btn03,0,3,0,4,Qt.AlignmentFlag.AlignTop)
        gridLayout.addWidget(btn04,1,0,2,0)        
        gridLayout.addWidget(btn05,3,0,0,3)        
        gridLayout.addWidget(btn06,4,0,0,4)
        gridLayout.addWidget(btn07,0,5,5,0,Qt.AlignmentFlag.AlignTop)


        baseWidget.setLayout(gridLayout)
        self.setCentralWidget(baseWidget)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()