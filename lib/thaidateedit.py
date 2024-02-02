import sys 
from PyQt6.QtWidgets import QLineEdit,QToolButton,QStyle
from PyQt6.QtCore import Qt ,pyqtSignal
from PyQt6.QtGui import QIcon


class QThaiDateEdit(QLineEdit):

    buttonClicked = pyqtSignal(list)

    def __init__(self,iconFile : str = ""):
        super().__init__()
        self.calendarPopup = True
        self.iconFile = iconFile
        self.setupUI()

    def setupUI(self):
        self.button = QToolButton(self)
        self.button.setIcon(QIcon(self.iconFile))
        self.button.setStyleSheet('border: 0px; padding: 0px;')
        self.button.setCursor(Qt.CursorShape.ArrowCursor)
        self.button.clicked.connect(self.buttonClicked.emit)

        frameWidth = self.style().pixelMetric(QStyle.PixelMetric.PM_DefaultFrameWidth)
        buttonSize = self.button.sizeHint()

        self.setStyleSheet('QLineEdit {padding-right: %dpx; }' % (buttonSize.width() + frameWidth + 1))
        self.setMinimumSize(max(self.minimumSizeHint().width(), buttonSize.width() + frameWidth*2 + 2),
                            max(self.minimumSizeHint().height(), buttonSize.height() + frameWidth*2 + 2))        


    def resizeEvent(self, event):
        buttonSize = self.button.sizeHint()
        frameWidth = self.style().pixelMetric(QStyle.PixelMetric.PM_DefaultFrameWidth)
        _rightX = int(self.rect().right() - frameWidth - buttonSize.width())
        _rightY = int((self.rect().bottom() - buttonSize.height() + 1)/2)
        self.button.move(_rightX,_rightY)
        super(QThaiDateEdit,self).resizeEvent(event)

    def doOnDateChange(self,newdate):
        print(newdate)
        self.validate = newdate



    def doOnDateTimeChange(self,newdate):
        print(newdate)
