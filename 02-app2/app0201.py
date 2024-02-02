from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


# Note ::
# QApplication สืบทอดคลาสมาจาก QGuiApplication()

# run in GUI
# app = QApplication(argv=[]) # Parameters พารามิเตอร์ / Arguments อาร์กิวเมนท์
app = QApplication([])

window = QMainWindow()
#window.show()
window.setFixedSize(680,480)
label1 = QLabel(window)
label1.setText("สวัสดีครับ")
#label1.setParent(window)
window.show()

app.exec() # สั่งให้ Application ทำงาน