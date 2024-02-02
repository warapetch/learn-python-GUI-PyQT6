```python
from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

# Note ::
# QApplication = QGuiApplication()

# run in GUI
# app = QApplication(argv=[]) # Parameters พารามิเตอร์ / Arguments อาร์กิวเมนท์
app = QApplication([])

app.exec() # สั่งให้ Application ทำงาน

"""
    exec() เป็นการสั่งงานแบบ Loop While 
    ทำงานจนกว่า โปรแกรมจะถูกปิด
    While App-Run == True:
        wait signal
    #
"""
```
