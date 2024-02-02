"""
    ไดอะลอก
    วรเพชร  เรืองพรวิสุทธิ์
    29/01/2567
"""

from PyQt6.QtCore import Qt ,pyqtSignal,QEventLoop
from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import (QDialog,QStyle,
                            QGridLayout,QWidget,QPlainTextEdit,
                            QLabel,QPushButton,)
from lib.layer import *

class DialogType():
    INFO = QStyle.StandardPixmap.SP_MessageBoxInformation
    WARN = QStyle.StandardPixmap.SP_MessageBoxWarning
    ERROR = QStyle.StandardPixmap.SP_MessageBoxCritical
    CONFIRM = QStyle.StandardPixmap.SP_MessageBoxQuestion

class MessageType():
    TEXT = 1
    HTML = 2


class MyDialog(QDialog):
    
    # New Event / Signal
    closedDialog = pyqtSignal(bool)

    def __init__(self,
                title:str,
                message:str,
                messageType: MessageType = MessageType.TEXT,
                dialogStyle: DialogType = DialogType.INFO,
                responses: list = [True,False],
                buttonTitles: list[str] = ["ตกลง"] ,
                backgroundHeader: str = "#A5E0FA"            
                ):

        # Display Type Dialog
        super().__init__(flags=Qt.WindowType.WindowTitleHint)

        self.setWindowTitle(title)
        
        # get standardIcon from QStyle.StandardPixmap
        icon = self.style().standardIcon(dialogStyle)
        self.setWindowIcon(icon)

        self.title = title
        self.message = message
        self.dialogStyle = dialogStyle
        self.dialogResponse = responses
        self.messageType = messageType
        self.buttonTitles = buttonTitles        
        if dialogStyle == DialogType.CONFIRM:
            if len(self.buttonTitles) == 1:
                self.buttonTitles.append("ยกเลิก")
        else:
            self.buttonTitles = buttonTitles
        self.backgroundHeader = backgroundHeader

        # fixed window (can not resize)
        self.setFixedSize(420,290)

        self.setupUI()


    def setupUI(self):

        baseLayout = QWidget()
        vGrid = QGridLayout()

        # get standardIcon from QStyle.StandardPixmap
        dynIcon = self.style().standardIcon(self.dialogStyle)
        lbImage = QLabel()
        lbImage.setPixmap(dynIcon.pixmap(40,40))
        lbImage.setGeometry(20,4,40,40)
        lbImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbHead = QLabel(self.title)
        lbHead.setFixedSize(400,30)
        lbHead.setStyleSheet(f"background-color: {self.backgroundHeader};")
        lbHead.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # make Layer
        layer1 = Layer(baseLayout,lbHead)
        layer2 = Layer(baseLayout,lbImage)

        pteMessage = QPlainTextEdit()
        if self.messageType == MessageType.TEXT:
            pteMessage.setPlainText(self.message)
        else:
            pteMessage.appendHtml(self.message)
        pteMessage.setReadOnly(True)

        
        btnOK = QPushButton(self.buttonTitles[0])
        btnOK.setFixedSize(150,40)
        btnOK.clicked.connect(self.doOnBtnOKClick)
        btnOK.setObjectName('ok')

        if self.dialogStyle == DialogType.CONFIRM: 
            btnCancel = QPushButton(self.buttonTitles[1])
            btnCancel.setFixedSize(150,40)
            btnCancel.clicked.connect(self.doOnBtnCancelClick)  
            btnCancel.setObjectName('cancel')
            vGrid.addWidget(btnOK,2,0,alignment=Qt.AlignmentFlag.AlignCenter)
            vGrid.addWidget(btnCancel,2,1,alignment=Qt.AlignmentFlag.AlignCenter)
        else:
            vGrid.addWidget(btnOK,2,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)        


        vGrid.addWidget(lbHead,0,0,1,0)
        vGrid.addWidget(pteMessage,1,0,1,0)
        baseLayout.setLayout(vGrid)
        baseLayout.setParent(self)


    def doOnBtnOKClick(self):
        self.closeDialog(self.dialogResponse[0])


    def doOnBtnCancelClick(self):
        self.closeDialog(self.dialogResponse[1])


    def closeDialog(self,response):
        self.closedDialog.emit(response)
        self.close()

    # Override
    def closeEvent(self, a0: QCloseEvent):
        #a0.ignore()
        return super().closeEvent(a0)


    def show(self,wait: bool = False):

        if wait == True:
            self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
            super().show()

            loop = QEventLoop()
            self.destroyed.connect(loop.quit)
            loop.exec() # wait ...
        else:
            super().show()



    # Override
    def exec(self):
        super().exec()
        return self.dialogResponse[0]
    

## End --

