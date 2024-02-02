from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


# Note ::
# QApplication = QGuiApplication()

# run in GUI
# app = QApplication(argv=[]) # Parameters พารามิเตอร์ / Arguments อาร์กิวเมนท์
app = QApplication([])

window = QWidget()
window.show()


app.exec() # สั่งให้ Application ทำงาน