# 07 - Style หน้าตา ธีมของวินโดว์
# available styles
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QStyleFactory,QApplication,QMainWindow,QStyle,
                             QGridLayout,QWidget,QMessageBox,
                             QLabel,QPushButton,QCheckBox, QLineEdit)
from PyQt6.QtGui import QFont,QIcon
import sys

# create(key)
# keys()

print(QStyleFactory.keys())
# >> ['windowsvista', 'Windows', 'Fusion']


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQT6 :: หัวข้อที่ 7-8-9")
        self.setWindowIcon(QIcon("./asset/windows.ico"))
        self.setupUI()


    def setupUI(self):

        bLayout = QWidget()
        vGrid = QGridLayout()

        lb1 = QLabel("Sign in ลงชื่อเข้าใช้งาน")
        #lb1.setFixedWidth(self.width()-20)
        lb1.setFixedWidth(480-20)
        lb1.setStyleSheet("background-color: #63EBF7;")
        
        lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lb2 = QLabel(f"UserID ไอดี:")
        lb3 = QLabel(f"Password รหัสผ่าน:")

        self.edt1 = QLineEdit("somchai")
        self.edt1.setPlaceholderText("ระบุไอดีผู้ใช้งาน")
        self.edt1.setFixedSize(200,40)

        self.edt2 = QLineEdit("12345")
        self.edt2.setPlaceholderText("ระบุรหัสผ่าน")
        self.edt2.setFixedSize(200,40)

        # https://doc.qt.io/qt-6/qpushbutton.html
        btn1 = QPushButton("OK")
        btn1.setFixedSize(200,40)
        btn1.setObjectName("ok")
        # clicked , pressed 
        btn1.clicked.connect(self.doOnBtnOKClick)


        btn2 = QPushButton("Cancel")
        btn2.setFixedSize(200,40)
        btn2.setObjectName("cancel")      
        btn2.clicked.connect(self.doOnBtnCancelClick)  

        cbb1 = QCheckBox("จดจำข้อมูล ?")

        vGrid.addWidget(lb1,0,0)
        vGrid.addWidget(lb2,1,0)
        vGrid.addWidget(lb3,2,0)
        vGrid.addWidget(self.edt1,1,1)
        vGrid.addWidget(self.edt2,2,1)
        vGrid.addWidget(btn1,3,0)
        vGrid.addWidget(btn2,3,1)
        vGrid.addWidget(cbb1,4,0)

        bLayout.setLayout(vGrid)
        self.setCentralWidget(bLayout)


    def doOnBtnOKClick(self):
        # print(self.edt1.text())
        # print(self.edt2.text())
        _text1 = f"User={self.edt1.text()}"
        _text2 = f"Password={self.edt2.text()}"
        
        #print("OK Click")
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Submit ลงชื่อเข้าโดย")
        dlg.setText(_text1+'\n'+_text2)
        dlg.exec()


    def doOnBtnCancelClick(self):
        QApplication.quit()
        

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

    # # set StyleSheet QSS
    # # https://doc.qt.io/qt-6/stylesheet-reference.html
    # # รูปแบบ property: value; 
    # # qss = "QMainWindow { background-color: #fff; }"
    # qss = """
    #         QMainWindow { 
    #             background-color: #fff; 
    #             }
    #         QLabel {
    #             color: black;
    #             background-color: #CFA8F8;
    #             font-size: 18px;
    #             margin-bottom: 10px;
    #             }            
    #         QPushButton:hover {
    #             background-color: #0b5ed7;
    #             border: 3px solid #9ac3fe;
    #             }
    #         QPushButton {
    #             background-color: #C8CACD;
    #             color: black;
    #             }         
    #         QPushButton#ok {
    #             background-color: green;
    #             color: black;
    #             }         
    #         QPushButton#cancel {
    #             background-color: red;
    #             color: black;
    #             }         
    #         QCheckBox {
    #             color: black;
    #             font-size: 18px;
    #             margin-bottom: 10px;
    #             }            
    #     """

    with open('main.css', 'r') as file:
        qss = file.read()
        app.setStyleSheet(qss)

    window = MainWindow()
    window.setFixedSize(480,250)
    window.show()

    sys.exit(app.exec())

#--End Main--

if __name__ == '__main__':
    Main()