# 07 - Style หน้าตา ธีมของวินโดว์
# available styles
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication,QMainWindow,
                             QGridLayout,QWidget,
                             QLabel,QPushButton,QCheckBox, QLineEdit)
from PyQt6.QtGui import QFont,QIcon
import sys

# create(key)
# keys()

# print(QStyleFactory.keys())
# >> ['windowsvista', 'Windows', 'Fusion']


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("PyQT6 :: หัวข้อที่ 7-8-9")
        self.setWindowIcon(QIcon("./asset/windows.ico"))
        self.setupUI()


    def setupUI(self):

        bLayout = QWidget() #background
        vGrid = QGridLayout()

        lb1 = QLabel("Sign in ลงชื่อเข้าใช้งาน")
        lb1.setFixedWidth(480-20)
        lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lb1.setStyleSheet("background-color: #63EBF7;")

        lb2 = QLabel(f"UserID ไอดี:")
        lb3 = QLabel(f"Password รหัสผ่าน:")

        edt1 = QLineEdit()
        edt1.setPlaceholderText("ระบุไอดีผู้ใช้งาน")
        edt1.setFixedSize(200,40)

        edt2 = QLineEdit()
        edt2.setPlaceholderText("ระบุรหัสผ่าน")
        edt2.setFixedSize(200,40)

        btn1 = QPushButton("OK")
        btn1.setFixedSize(200,40)
        btn1.setObjectName("ok")

        btn2 = QPushButton("Cancel")
        btn2.setFixedSize(200,40)
        btn2.setObjectName("cancel")

        cbb1 = QCheckBox("จดจำข้อมูล ?")

        vGrid.addWidget(lb1,0,0)
        vGrid.addWidget(lb2,1,0)
        vGrid.addWidget(lb3,2,0)
        vGrid.addWidget(edt1,1,1)
        vGrid.addWidget(edt2,2,1)
        vGrid.addWidget(btn1,3,0)
        vGrid.addWidget(btn2,3,1)
        vGrid.addWidget(cbb1,4,0)

        bLayout.setLayout(vGrid)
        self.setCentralWidget(bLayout)

### --- End Class --- ###


def Main():
# >> ['windowsvista', 'Windows', 'Fusion']    
    app = QApplication([])
    # set Style
    _style = "Windows"
    app.setStyle(_style)
    
    # set Font
    # QFont(const QString &family, int pointSize = -1, int weight = -1, bool italic = false)
    _font = QFont("Bai Jamjuree",12)
    app.setFont(_font)

    # set StyleSheet QSS
    # https://doc.qt.io/qt-6/stylesheet-reference.html
    # รูปแบบ property: value; 
    # qss = "QMainWindow { background-color: #fff; }"
    qss = """
            QMainWindow { 
                background-color: #fff; 
                }
            QLabel {
                color: black;
                background-color: #CFA8F8;
                font-size: 18px;
                margin-bottom: 10px;
                }            
            QPushButton:hover {
                background-color: #8EECF0;
                border: 3px solid #8EB9F0;
                }
            QPushButton {
                background-color: #C8CACD;
                color: black;
                }         
            QPushButton#ok {
                background-color: green;
                color: black;
                }         
            QPushButton#cancel {
                background-color: red;
                color: black;
                }         
            QCheckBox {
                color: black;
                font-size: 18px;
                margin-bottom: 10px;
                }            
        """
    app.setStyleSheet(qss)



    window = MainWindow()
    window.setFixedSize(480,250)
    window.show()

    sys.exit(app.exec())

#--End Main--

if __name__ == '__main__':
    Main()