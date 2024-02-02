เล่นกับ app

```python
from PyQt6 import QtCore ,QtGui,QtWidgets
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QPoint

app = QApplication([])

#window = QWidget()

# window = QPushButton()
# window.setFont(QFont("Bai Jamjuree",15))
# window.setText("สวัสดีครับ")

window = QMainWindow()
window.setGeometry(0,0,680,480)

gt = window.frameGeometry()
ctp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
gt.moveCenter(ctp)
window.move(gt.left(),gt.top())

window.show()

app.exec()
# from PyQt6 import QtCore ,QtGui,QtWidgets
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QPoint

app = QApplication([])

#window = QWidget()

# window = QPushButton()
# window.setFont(QFont("Bai Jamjuree",15))
# window.setText("สวัสดีครับ")

window = QMainWindow()
window.setGeometry(0,0,680,480)

gt = window.frameGeometry()
ctp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
gt.moveCenter(ctp)
window.move(gt.left(),gt.top())

window.show()

app.exec()