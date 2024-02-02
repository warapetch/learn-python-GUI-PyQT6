from PyQt6 import QtCore , QtGui , QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

app = QApplication([]) # Parameter  List of String
window = QMainWindow() # Main , Dialog ,Widget
window.setWindowTitle("PyQT6-บทที่ 1")
window.setFixedSize(680,480) # Overload 
#window.resize(QSize(400,400)) # QSize(W,H)
#window.setGeometry(200, 200, 400, 400) # Left , Top , Width , Height
window.setFont(QFont("Bai Jamjuree",15))

label = QLabel(window)
label.setText("สวัสดีครับ")

btn1 = QPushButton(window)
btn1.setText("กดฉันหน่อย")
btn1.setGeometry(0,40,150,30)

window.show()

app.exec()
"""
    while app == run:
        event handler (ดักรอรับ Event)

"""


