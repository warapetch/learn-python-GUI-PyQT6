# 10 - Dialog
# QDialog
from PyQt6.QtCore import Qt ,QUrl
from PyQt6.QtWidgets import (QApplication,QMainWindow,QDialog,
                            QGridLayout,QWidget,QDialogButtonBox,
                            QLabel,QPushButton,QVBoxLayout,QMessageBox,
                            QInputDialog,QFileDialog,QProgressDialog,QColorDialog
                            )
from PyQt6.QtGui import QFont,QIcon,QColor
import sys ,time

sys.path.append('./')
from lib.mydialog import *



class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQT6 :: หัวข้อที่ 10-11")
        self.setWindowIcon(QIcon("./asset/windows.ico"))

        self.setupUI()


    def setupUI(self):

        bLayout = QWidget()
        vGrid = QGridLayout()

        lbHeader = QLabel("แนะนำ Dialog ไดอะลอก")
        lbHeader.setStyleSheet("background-color: #75FAA8;")
        lbHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btnShowQDlg = QPushButton("QDialog")
        btnShowQDlg.setFixedSize(200,40)
        btnShowQDlg.clicked.connect(self.btnShowQDlgClick)

        btnShowMsgBox = QPushButton("QMessageBox")
        btnShowMsgBox.setFixedSize(200,40)
        btnShowMsgBox.clicked.connect(self.btnShowMsgBoxClick)

        # QDialog,QMessageBox
        # QInputDialog QFileDialog
        # QProgressDialog ,QColorDialog

        # QFontDialog
        # QErrorMessage, QPrintPreviewDialog, 
        # QPageSetupDialog, QAbstractPrintDialog, QPrintDialog, 

        btnInputDlg = QPushButton("QInputDialog")
        btnInputDlg.setFixedSize(200,40)
        btnInputDlg.clicked.connect(self.btnInputDlgClick)

        btnOpenFileDlg = QPushButton("QFileDialog")
        btnOpenFileDlg.setFixedSize(200,40)
        btnOpenFileDlg.clicked.connect(self.btnOpenFileDlgClick)
                
        btnProgressDlg = QPushButton("QProgressDialog")
        btnProgressDlg.setFixedSize(200,40)
        btnProgressDlg.clicked.connect(self.btnProgressDlgClick)

        self.btnShowColorDlg = QPushButton("QColorDialog")
        self.btnShowColorDlg.setFixedSize(200,40)
        self.btnShowColorDlg.clicked.connect(self.btnShowColorDlgClick)

        btnMyCustomDlg = QPushButton("CustomDialog")
        btnMyCustomDlg.setFixedSize(200,40)
        btnMyCustomDlg.clicked.connect(self.btnMyCustomDlgClick)

        vGrid.addWidget(lbHeader,0,0,1,0)
        vGrid.addWidget(btnShowQDlg,1,0)
        vGrid.addWidget(btnShowMsgBox,2,0)
        vGrid.addWidget(btnInputDlg,3,0)
        vGrid.addWidget(btnOpenFileDlg,4,0)
        vGrid.addWidget(btnProgressDlg,5,0)
        vGrid.addWidget(self.btnShowColorDlg,6,0)
        vGrid.addWidget(btnMyCustomDlg,7,0)


        bLayout.setLayout(vGrid)
        self.setCentralWidget(bLayout)


    def btnShowQDlgClick(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("QDialog ครับ")

        vLayout = QVBoxLayout()
        lbMessage = QLabel("สวัสดีชาวโลก") #QPlainTextEdit 
        lbMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        
        buttons.button(QDialogButtonBox.StandardButton.Ok).setText("ตกลง")
        buttons.button(QDialogButtonBox.StandardButton.Cancel).setText("ยกเลิก")        
        
        buttons.accepted.connect(dlg.accept)
        buttons.rejected.connect(dlg.reject)

        vLayout.addWidget(lbMessage)
        vLayout.addWidget(buttons)
        dlg.setLayout(vLayout)
        dlg.setFixedSize(350,250)
        dlg.exec()

    def btnShowMsgBoxClick(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Message Box")
        dlg.setText("สวัสดีชาวโลก")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dlg.button(QMessageBox.StandardButton.Ok).setText("ตกลง")
        dlg.button(QMessageBox.StandardButton.Cancel).setText("ยกเลิก")
        dlg.exec()

    def btnInputDlgClick(self):
        dlg = QInputDialog(self)
        #value,resultOK = dlg.getDouble(self,"ระบุเลขทศนิยม","จำนวน")
        #value,resultOK = dlg.getInt(self,"ระบุเลข","จำนวน")
        # _list = ['ชาย','หญิง','ไม่ระบุ']
        # value,resultOK = dlg.getItem(self,"เลือก 1 รายการ","เลือก",_list)
        # value,resultOK = dlg.getText(self,"กรุณากรอกชื่อ","ชื่อ")
        dlg.setOkButtonText("ตกลง")
        dlg.setCancelButtonText("ยกเลิก")
        value,resultOK = dlg.getMultiLineText(self,"กรุณากรอกรายละเอียด","ประวัติ")
        
        if resultOK == True:
            print(f"value = {value} >> {resultOK}")


    def btnOpenFileDlgClick(self):
        _filter = "Python file (*.py);;All files (*.*)"
        # dlg = QFileDialog(caption="เลือกไฟล์",directory=".",filter=_filter)
        # dlg.exec()
        # _files = dlg.selectedFiles()
        # if _files != []:
        #     print(_files)

        #value = QFileDialog.getExistingDirectory(caption="เลือกโฟลเดอร์",directory=".",)
        #value1,value2 = QFileDialog.getOpenFileName(caption="เลือกไฟล์",directory=".",filter=_filter)
        # filenames,selectedfilter = QFileDialog.getOpenFileNames(caption="เลือกไฟล์",directory=".",filter=_filter,initialFilter="All files (*.*)")
        # filenames,selectedfilter = QFileDialog.getSaveFileName(caption="บันทึกเป็น",directory=".",filter=_filter,initialFilter="Python file (*.py)")
        url = QUrl()
        url.fromLocalFile("*.py")
        filenames,selectedfilter = QFileDialog.getSaveFileUrl(caption="เลือกไฟล์",directory=url,filter=_filter,initialFilter="All files (*.*)")

        if not filenames.isEmpty():
            print(f"file={filenames} ,type={selectedfilter}")


    def btnProgressDlgClick(self):
        dlg = QProgressDialog()        
        dlg.setRange(0,100) # dlg.minimum = 0 , dlg.maximum = 100
        value = 1
        dlg.show() #dlg.exec()
        for value in range(100):
            dlg.setValue(value)
            if dlg.wasCanceled() :
                break
            time.sleep(0.100) 
            QApplication.processEvents()

    def btnShowColorDlgClick(self):
        dlg = QColorDialog()
        dfColor = QColor() 
        value = dlg.getColor(initial=dfColor,title="เลือกสี")
        print(f"Selected Color= {value.name()}")
        colorName = value.name()
        _style = f"background-color: {colorName};"
        self.btnShowColorDlg.setStyleSheet(_style)


    def doOnDlgClose(self,clickedOK):
        print(clickedOK)

    def btnMyCustomDlgClick(self):
        # dlg = MyDialog(title="ยืนยันการทำงาน",message="ยืนยันการทำงานต่อไปนี้",
        #                 dialogStyle= DialogType.CONFIRM,
        #                 buttonTitles=["ยืนยัน","ยกเลิก"])

        dlg = MyDialog(title="แจ้งข้อความ",message="การทำงานเสร็จแล้ว",
                        dialogStyle= DialogType.INFO,
                        buttonTitles=["ตกลง"],
                        backgroundHeader= "#F3C289")

        dlg.closedDialog.connect(self.doOnDlgClose)
        dlg.exec()




### --- End Class --- ###


def Main():

    app = QApplication([])
    app.setFont(QFont("Bai Jamjuree",12))

    window = MainWindow()
    window.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
    window.show()

    sys.exit(app.exec())

#--End Main--

if __name__ == '__main__':
    Main()






























"""
    def doOnBtnCancelClick(self):
        myDialog = MyDialog("ยืนยันการทำงาน","ยืนยันการทำงานต่อไปนี้",dialogStyle=DialogType.CONFIRM,buttonTitles=["ยืนยัน","ยกเลิก"])
        myDialog.closedDialog.connect(self.doOnDlgClose)
        myDialog.exec()


        """