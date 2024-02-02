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


        baseWidget = QWidget()
        # set Layout Grid เต็มจอ
        formLayout = QGridLayout()

        # set UI
        lb1 = QLabel("ชื่อ")
        lb2 = QLabel("นามสกุล")

        ed1 = QLineEdit("ชื่อ")
        ed2 = QLineEdit("นามสกุล")

        lb3 = QLabel("เพศ")
        cb1 = QComboBox()
        cb1.addItem('ไม่ระบุ')
        cb1.addItems(["ชาย", "หญิง", "-"])
        
        chkBox1 = QCheckBox("มีจักรยาน")
        chkBox2 = QCheckBox("มีรถยนต์")
        chkBox3 = QCheckBox("มีบ้าน")
                        
        btn1 = QPushButton("บันทึก")
        btn2 = QPushButton("ยกเลิก")
               
        #2 
        lb1.setFixedSize(QSize(120,50))
        lb2.setFixedSize(QSize(120,50))
        btn1.setFixedSize(QSize(120,50))
        btn2.setFixedSize(QSize(120,50))
     
        # Add เข้า Layout
        formLayout.addWidget(lb1,0,0)
        formLayout.addWidget(ed1,0,1)
        formLayout.addWidget(lb2,1,0)
        formLayout.addWidget(ed2,1,1)

        formLayout.addWidget(lb3,2,0)
        formLayout.addWidget(cb1,2,1)

        formLayout.addWidget(chkBox1,3,1)
        formLayout.addWidget(chkBox2,3,2)
        formLayout.addWidget(chkBox3,3,3)

        formLayout.addWidget(btn1,4,2)
        formLayout.addWidget(btn2,4,3)


        baseWidget.setLayout(formLayout)
        self.setCentralWidget(baseWidget)

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