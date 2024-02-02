from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

app = QApplication([])
window = QMainWindow()
window.show()
window.setFixedSize(680,480)

app.exec()