
# 07 - Style หน้าตา ธีมของวินโดว์

# available styles
from PyQt6.QtWidgets import (QApplication,QMainWindow,
                            QLabel,QPushButton,QCheckBox)
from PyQt6.QtGui import QIcon
import sys

class MainWindow(QMainWindow):

    def __init__(self,useStyle : str) -> None:
        super().__init__()
        self.useStyle = useStyle
        self.setWindowTitle("PyQT6 :: หัวข้อที่ 7-8-9")
        self.setWindowIcon(QIcon("./asset/windows.ico"))

        self.setupUI()


    def setupUI(self):
        lb1 = QLabel(f"Style: {self.useStyle}")
        lb1.setGeometry(5,5,200,40)
        lb1.setParent(self)

        btn1 = QPushButton(f"Style: {self.useStyle}")
        btn1.setGeometry(5,50,200,40)
        btn1.setParent(self)

        cbb1 = QCheckBox(f"Style: {self.useStyle}")
        cbb1.setGeometry(5,100,200,40)
        cbb1.setParent(self)

### --- End Class --- ###


def Main():
# >> ['windowsvista', 'Windows', 'Fusion']    
    app = QApplication([])
    _style = "Windows"
    app.setStyle(_style)

    window = MainWindow(useStyle=_style)
    window.setFixedSize(480,250)
    window.show()

    sys.exit(app.exec())

#--End Main--

if __name__ == '__main__':
    Main()