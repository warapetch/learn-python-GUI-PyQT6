from PyQt6.QtWidgets import (QVBoxLayout, QWidget,  QLabel ,QPushButton)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('About')
        self.setWindowIcon(QIcon("./asset/icons/application-blue.png"))
        self.setFixedSize(300,250)
        self.setupUI()

    def setupUI(self):

        layout = QVBoxLayout()
        lbAbout = QLabel("เกี่ยวกับโปรแกรม\nพัฒนาโดย วรเพชร  เรืองพรวิสุทธิ์")

        btnOK = QPushButton('ตกลง')
        btnOK.setFixedWidth(150)
        btnOK.clicked.connect(self.btnOKClick)

        layout.addWidget(lbAbout)
        layout.addWidget(btnOK)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    
    def btnOKClick(self):
        self.close()