from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


# Note ::
# QApplication = QGuiApplication()

# run in GUI
# app = QApplication(argv=[]) # Parameters พารามิเตอร์ / Arguments อาร์กิวเมนท์
app = QApplication([])

window = QMainWindow()
window.setWindowTitle("PyQT6 บทเรียน 02")
window.setFont(QFont("Bai Jamjuree",15))
#2 
window.resize(680,480)
#3
#window.setFixedSize(680,480)

#4
lb1 = QLabel("ชื่อ")
btn = QPushButton("คลิกหน่อย")

#5 
lb1.setParent(window)
#6
btn.setParent(window)
"""
    Widget insert to parent Maximize
"""
window.show()

app.exec() # สั่งให้ Application ทำงาน