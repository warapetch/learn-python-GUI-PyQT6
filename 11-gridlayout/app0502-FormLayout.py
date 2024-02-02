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
        self.setWindowTitle("PyQT6 บทเรียน 02")
        self.setFont(QFont("Bai Jamjuree",15))
        self.resize(680,480)

        # background
        ctlwidget = QWidget(self)
        ctlwidget.setObjectName(u"centralwidget")        

        bgwidget = QWidget(ctlwidget)
      
        formLayout = QFormLayout(bgwidget)
        # set Layout HBox แนวนอน ไปทางขวามือ
        hLayout = QHBoxLayout(bgwidget)

        # set UI
        lb1 = QLabel(text="ชื่อ",parent=bgwidget,)
        lb2 = QLabel(parent=bgwidget,text="นามสกุล") # สลับ

        ed1 = QLineEdit(text="ชื่อ",parent=bgwidget)
        ed2 = QLineEdit(text="นามสกุล",parent=bgwidget)

        btn1 = QPushButton(text="บันทึก",parent=bgwidget)
        btn2 = QPushButton(text="ยกเลิก",parent=bgwidget)

        #2 
        lb1.setFixedSize(QSize(120,50))
        lb2.setFixedSize(QSize(120,50))
        btn1.setFixedSize(QSize(120,50))
        btn2.setFixedSize(QSize(120,50))
        
        hLayout.addWidget(btn1)
        hLayout.addWidget(btn2)
        
        formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, lb1)
        formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, ed1)
        formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, lb2)
        formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, ed2)      
        formLayout.setLayout(3, QFormLayout.ItemRole.FieldRole, hLayout)
        
        ctlwidget.setLayout(formLayout)
        self.setCentralWidget(ctlwidget)

        """
        widget not shown
        QWidget::setLayout: Attempting to set QLayout "" on MainWindow "", which already has a layout
        """

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()