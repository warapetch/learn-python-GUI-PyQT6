"""
    # Qt-Designer
    D:\anaconda3\envs\envPyQT\Lib\site-packages\qt6_applications\Qt\bin

    # Doc ComboBox
    https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QComboBox.html#signals

    วรเพชร  เรืองพรวิสุทธิ์
    Alignment . QComboBox
    created: 27/01/2567 21:00
"""

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
        self.setWindowTitle("PyQT6 หัวข้อที่ 4")
        self.setFont(QFont("Bai Jamjuree",15))
        self.resize(680,480)
        self.setupUI()


    def setupUI(self):

        baseWidget = QWidget() # Background
        
        # set Layout VBox แนวตั้ง
        vGrid = QGridLayout()
        
        self.cbAlignment = QComboBox()
        self.myAlignment = [
            Qt.AlignmentFlag.AlignLeft,
            #Qt.AlignmentFlag.AlignLeading,
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom,
            
            Qt.AlignmentFlag.AlignHCenter,
            Qt.AlignmentFlag.AlignCenter,            
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom,            
            #Qt.AlignmentFlag.AlignTrailing,

            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop,
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom,

            Qt.AlignmentFlag.AlignJustify,
            Qt.AlignmentFlag.AlignAbsolute,
            #Qt.AlignmentFlag.AlignHorizontal_Mask,
            Qt.AlignmentFlag.AlignTop,
            Qt.AlignmentFlag.AlignBottom,
            Qt.AlignmentFlag.AlignVCenter,
            #Qt.AlignmentFlag.AlignVertical_Mask,
            Qt.AlignmentFlag.AlignBaseline,       
        ]

        for value in self.myAlignment: 
            self.cbAlignment.addItem(value.name)        
        
        # set signal --> slot
        # activated == Selected      
        self.cbAlignment.activated.connect(self.DoOnComboboxSelected)
        self.cbAlignment.currentTextChanged.connect(self.DoOnComboboxTextChange)        
        self.cbAlignment.currentIndexChanged.connect(self.DoOnComboboxIndexChange)


        # set UI        
        lbInfo = QLabel(self)
        lbInfo.setGeometry(20,5,620,30)
        lbInfo.setText("Alignment การกำหนดตำแหน่ง")
        lbInfo.setStyleSheet("background: #BCFFA9;")
        lbInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbLeft = QLabel("alignLeft")
        lbCenter = QLabel("alignCenter")
        lbRight = QLabel("alignRight")
        lbTop = QLabel("alignTop")
        lbBottom = QLabel("alignBottom")
        lbHCenter = QLabel("alignHCenter")
        lbVCenter = QLabel("alignVCenter")
        lbJust = QLabel("alignJustify")
        lbAbs = QLabel("alignAbsolute")
        lbBaseLine = QLabel("alignBaseline")
        
        self.lbActive = QLabel("--ทดสอบ--")
        self.lbActive.setStyleSheet("background: yellow;")

        #2 
        lbLeft.setFixedSize(QSize(170,65))
        lbCenter.setFixedSize(QSize(170,65))
        lbRight.setFixedSize(QSize(170,65))
        lbTop.setFixedSize(QSize(170,65))
        lbBottom.setFixedSize(QSize(170,65))
        lbHCenter.setFixedSize(QSize(170,65))
        lbVCenter.setFixedSize(QSize(170,65))
        lbJust.setFixedSize(QSize(170,65))
        lbAbs.setFixedSize(QSize(170,65))
        lbBaseLine.setFixedSize(QSize(170,65))

        self.lbActive.setFixedSize(QSize(170,65))

        lbLeft.setAlignment(Qt.AlignmentFlag.AlignLeft)
        lbCenter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbRight.setAlignment(Qt.AlignmentFlag.AlignRight)
        lbTop.setAlignment(Qt.AlignmentFlag.AlignTop)
        lbBottom.setAlignment(Qt.AlignmentFlag.AlignBottom)
        lbHCenter.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lbVCenter.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        lbJust.setAlignment(Qt.AlignmentFlag.AlignJustify)
        lbAbs.setAlignment(Qt.AlignmentFlag.AlignAbsolute)
        lbBaseLine.setAlignment(Qt.AlignmentFlag.AlignBaseline)
        self.lbActive.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        #3 
        #vGrid.addWidget(lbInfo)
        vGrid.addWidget(lbLeft,0,0)
        vGrid.addWidget(lbCenter,0,1)
        vGrid.addWidget(lbRight,0,2)
        vGrid.addWidget(lbTop,1,0)
        vGrid.addWidget(lbBottom,1,1)

        vGrid.addWidget(lbHCenter,2,0)
        vGrid.addWidget(lbVCenter,2,1)
        vGrid.addWidget(lbJust,1,2)
        vGrid.addWidget(lbAbs,2,2)
        vGrid.addWidget(lbBaseLine,3,0)
        vGrid.addWidget(self.lbActive,3,1)

        vGrid.addWidget(self.cbAlignment,3,2)

        baseWidget.setLayout(vGrid)

        self.setCentralWidget(baseWidget)


    #1
    def DoOnComboboxIndexChange(self,index):
        #Old Value
        #QComboBox(self).currentText()
        #QComboBox(self).currentIndex()
        print(f"Current Text:{self.cbAlignment.currentText()}")
        print(f"Current Index:{self.cbAlignment.currentIndex()}")


        #New Value
        _text = self.myAlignment[index].name
        print(f"Index Changed: {index}")
        print(f"set to: {_text}")
        
        self.cbAlignment.setCurrentText(_text)
        self.cbAlignment.setCurrentIndex(index)

        self.lbActive.setAlignment(self.myAlignment[index])

    #2
    def DoOnComboboxTextChange(self, text):
        print(f"Text Changed: '{text}'")


    #3
    def DoOnComboboxSelected(Self, index):
        print(f"Selected index: {index}")


def main():
    app = QApplication([])

    app.setStyleSheet("""
        QLabel{
        color: black;
        background-color: white;
        }

""")
    app.setFont(QFont('Bai Jamjuree',15))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()