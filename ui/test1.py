
from PyQt6.QtWidgets import QApplication,QWidget
import sys


#app = QApplication(sys.argv) # arguments / parameter พารามิเตอร์ที่ส่งเข้าไป
app = QApplication([])
window = QWidget()
window.show()

app.exec()