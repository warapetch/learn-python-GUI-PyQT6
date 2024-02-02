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
        
        # set Layout HBox แนวนอน
        hLayout = QHBoxLayout()

        # set UI
        lb1 = QLabel("ชื่อ")
        lb2 = QLabel("นามสกุล")
        btn1 = QPushButton("บันทึก")       
        btn2 = QPushButton("ยกเลิก")

        #2 
        lb1.setFixedSize(QSize(120,50))
        lb2.setFixedSize(QSize(120,50))
        btn1.setFixedSize(QSize(120,50))
        btn2.setFixedSize(QSize(120,50))
        
        #3 
        hLayout.addWidget(lb1)
        hLayout.addWidget(lb2)
        hLayout.addWidget(btn1)
        hLayout.addWidget(btn2)

        baseWidget.setLayout(hLayout)
        self.setCentralWidget(baseWidget)

        """
        ใช้ baseWidget แก้ไขปัญหา
        - widget not shown
        - QWidget::setLayout: Attempting to set QLayout "" on MainWindow "", which already has a layout
        """



def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()