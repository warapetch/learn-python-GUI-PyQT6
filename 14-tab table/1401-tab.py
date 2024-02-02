import sys
from PyQt6.QtWidgets import (QApplication, QWidget,  QFormLayout, 
                        QGridLayout, QTabWidget, QLineEdit, 
                        QDateEdit, QPushButton,QTableWidget,QTableWidgetItem,
                        QAbstractItemView,QMessageBox
                        )
from PyQt6.QtGui import QFont,QIcon
from PyQt6.QtCore import Qt,QDate

# แก้ไขปัญหา module not found แม้จะสร้างไฟล์ `__init__.py` แล้ว
sys.path.append('./')
""" 
PYQT6
  |-- lib
       - mydialog.py
"""
from lib.mydialog import *

# แก้ไขปัญหา module not found แม้จะสร้างไฟล์ `__init__.py` แล้ว
# Folder "15-multi form"
# File "1501-about.py"
""" 
PYQT6
  |-- 15-multi form
       - 1501-about.py
"""
about = __import__("15-multi form.1501-about",fromlist="AboutWindow")

# QMainWindow >> Error
# QWidget::setLayout: Attempting to set QLayout "" on MainWindow "", which already has a layout

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('ลงทะเบียน')
        self.setWindowIcon(QIcon("./asset/icons/card-address"))
        self.setFixedSize(800,250)
        self.setupUI()



    def setupUI(self):

        # background Layer-1
        gridLayout = QGridLayout()

        self.dataset = []

        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ชื่อ","วันเกิด","อีเมล","โทรศัพท์"])
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        # create a tab widget
        tab = QTabWidget(self)

        # personal info page
        personalPage = QWidget()

        # contact info page
        contactPage = QWidget()

        self.leName = QLineEdit()
        self.lePassword = QLineEdit()
        self.lePassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.lePassword2 = QLineEdit()
        self.lePassword2.setEchoMode(QLineEdit.EchoMode.Password)

        self.leBirth = QDateEdit() ## ,calendarPopup=True,date=QDate.currentDate())
        self.leBirth.setCalendarPopup(True)
        self.leBirth.setDate(QDate.currentDate())

        self.leEmail = QLineEdit()
        self.lePhone = QLineEdit()

        # personLayout สำหรับแสดงใน Tab person info
        personLayout = QFormLayout()
        personLayout.addRow('ชื่อ:',self.leName)
        personLayout.addRow('รหัสผ่าน:', self.lePassword)
        personLayout.addRow('ยืนยัน รหัสผ่าน:', self.lePassword2)
        personLayout.addRow('วันเกิด:',self.leBirth)

        personalPage.setLayout(personLayout)


        # contactLayout สำหรับแสดงใน Tab contact info
        contactLayout = QFormLayout()
        contactLayout.addRow('อีเมล:', self.leEmail)
        contactLayout.addRow('โทรศัพท์:', self.lePhone)
        
        contactPage.setLayout(contactLayout)


        # add page to tab
        tab.addTab(personalPage, 'ข้อมูลบุคคล')
        tab.addTab(contactPage, 'การติดต่อ')

        # buttons
        btnOK = QPushButton('บันทึก')
        btnOK.setFixedWidth(150)
        btnOK.clicked.connect(self.btnOKClick)

        btnCancel = QPushButton('ยกเลิก')
        btnCancel.setFixedWidth(150)
        btnCancel.clicked.connect(self.btnCancelClick)

        btnAbout = QPushButton('เกี่ยวกับ')
        btnAbout.setFixedWidth(150)
        btnAbout.clicked.connect(self.btnAboutClick)

        btnCustom = QPushButton('Custom')
        btnCustom.setFixedWidth(150)
        btnCustom.clicked.connect(self.btnCustomClick)


        # add all to GridLayout
        gridLayout.addWidget(tab, 0, 0, 1, 2)
        gridLayout.addWidget(btnOK,2,0)
        gridLayout.addWidget(btnCancel,2,1)

        gridLayout.addWidget(btnCustom,2,2,alignment=Qt.AlignmentFlag.AlignLeft)
        gridLayout.addWidget(btnAbout,2,2,alignment=Qt.AlignmentFlag.AlignRight)

        gridLayout.addWidget(self.table,0,2)
        self.setLayout(gridLayout)



    def btnOKClick(self):
        #print("OK-Click")
        pswOK = self.lePassword.text() == self.lePassword2.text()

        if  pswOK and len(self.leName.text()) > 0:
            data = {'name': self.leName.text() ,
                    'birth': self.leBirth.text(),
                    'email': self.leEmail.text(),
                    'phone': self.lePhone.text()
                    }

            self.dataset.append(data)

            recordCount = len(self.dataset)
            self.table.setItem(recordCount-1,0, QTableWidgetItem(data['name']))
            self.table.setItem(recordCount-1,1, QTableWidgetItem(data['birth']))
            self.table.setItem(recordCount-1,2 , QTableWidgetItem(data['email']))
            self.table.setItem(recordCount-1,3 , QTableWidgetItem(data['phone']))

            self.leName.clear()
            self.leBirth.clear()
            self.leEmail.clear()
            self.lePhone.clear()
            self.lePassword.clear()
            self.lePassword2.clear()
            self.leBirth.setDate(QDate.currentDate())

        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("โปรดตรวจสอบ")
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.setText(f"กำหนดข้อมูลไม่ถูกต้อง รหัสผ่าน OK ={pswOK} !!")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.button(QMessageBox.StandardButton.Ok).setText("ตกลง")
            dlg.exec()            


    def btnCancelClick(self):
        print("Cancel-Click")
        self.close()


    def btnAboutClick(self):
        print("About-Click")
        self.dlg = about.AboutWindow()
        self.dlg.show()


    def btnCustomClick(self):
        print("Custom-Click")

        dlg = MyDialog(title="ยืนยันการทำงาน ?",message="ยืนยันการทำงาน",dialogStyle=DialogType.CONFIRM)
        dlg.exec()



def main():

    app = QApplication(sys.argv)
    app.setFont(QFont("Bai Jamjuree",12))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()