# Qt-Designer
# D:\anaconda3\envs\envPyQT\Lib\site-packages\qt6_applications\Qt\bin

from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import sys

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQT6 หัวข้อที่ 3")
        self.setFont(QFont("Bai Jamjuree",15))
        self.resize(680,480)
        self.setupUI()


    def setupUI(self):

        baseWidget = QWidget() # Background
        
        # set Layout VBox แนวตั้ง
        vLayout = QVBoxLayout()

        # set UI
        lb1 = QLabel("ชื่อ")
        lb2 = QLabel("นามสกุล")
        btn1 = QPushButton("บันทึก")       
        btn2 = QPushButton("ยกเลิก")

        #2 
        lb1.setFixedSize(QSize(120,50))
        lb2.setFixedSize(QSize(120,50))

        lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lb2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter)


        # QSS (CSS) 
        #lb1.setStyleSheet("color: rgb(255, 0, 0);background-color: rgb(170, 255, 0);font: 20px;font-family:'Bai Jamjuree';")
        #lb2.setStyleSheet("background: yellow;color: black;font: 20px;font-family:'Bai Jamjuree';")

        btn1.setFixedSize(QSize(120,50))
        btn2.setFixedSize(QSize(120,50))
        
        #3 
        vLayout.addWidget(lb1)
        vLayout.addWidget(lb2)
        vLayout.addWidget(btn1)
        vLayout.addWidget(btn2)

        vLayout.setSpacing(20)
        vLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)        

        baseWidget.setLayout(vLayout)
        self.setCentralWidget(baseWidget)

        """
        ใช้ baseWidget แก้ไขปัญหา
        - widget not shown
        - QWidget::setLayout: Attempting to set QLayout "" on MainWindow "", which already has a layout
        """



def main():
    app = QApplication([])

    app.setStyleSheet("""
        QLabel{
        color: blue;
        background-color: red;
        }

""")
    app.setFont(QFont('Bai Jamjuree',15))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()