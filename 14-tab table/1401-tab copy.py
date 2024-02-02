# import sys
# from PyQt6.QtWidgets import (QApplication, QWidget,  QFormLayout, 
#                         QGridLayout, QTabWidget, QLineEdit, 
#                         QDateEdit, QPushButton
#                         )
# from PyQt6.QtCore import Qt,QDate,QDateTime

# sys.path.append('./')
# from lib.thaidateedit import QThaiDateEdit


# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('ลงทะเบียน')
#         self.setupUI()

#     def setupUI(self):

#         # background Layer-1
#         baseWidget = QWidget()

#         # create a tab widget
#         tab = QTabWidget(self)

#         # personal info page
#         personalPage = QWidget(self)

#         # contact info page
#         contactPage = QWidget(self)

#         # 
#         personLayout = QFormLayout()
#         personalPage.setLayout(personLayout)


#         personLayout.addRow('ชื่อ:', QLineEdit(self))
#         personLayout.addRow('อีเมล:', QLineEdit(self))
#         personLayout.addRow('รหัสผ่าน:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
#         personLayout.addRow('ยืนยัน รหัสผ่าน:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
#         personLayout.addRow('วันเกิด:',QDateEdit(self))

#         layout.addRow('โทรศัพท์:', QLineEdit(self))
        

#         btnOK = QPushButton('บันทึก')
#         btnOK.setFixedWidth(150)
#         btnOK.clicked.connect(self.btnOKClick)

#         btnCancel = QPushButton('ยกเลิก')
#         btnCancel.setFixedWidth(150)
#         btnCancel.clicked.connect(self.btnCancelClick)

#         baseWidget
#         layout.addRow(btnOK,btnCancel)


#     def btnOKClick(self):
#         print("OK-Click")


#     def btnCancelClick(self):
#         print("Cancel-Click")
#         self.close()


#         # # create a tab widget
#         # tab = QTabWidget(self)

#         # # personal page
#         # personal_page = QWidget(self)
#         # layout = QFormLayout()
#         # personal_page.setLayout(layout)
#         # layout.addRow('First Name:', QLineEdit(self))
#         # layout.addRow('Last Name:', QLineEdit(self))
#         # layout.addRow('DOB:', QThaiDateEdit())
        
#         now = QDateTime().currentDateTime()
#         print('Local datetime: ', now.toString(Qt.DateFormat.ISODate))

#         # contact pane
#         contact_page = QWidget(self)
#         layout = QFormLayout()
#         contact_page.setLayout(layout)
#         layout.addRow('Phone Number:', QLineEdit(self))
#         layout.addRow('Email Address:', QLineEdit(self))

#         # add pane to the tab widget
#         tab.addTab(personal_page, 'Personal Info')
#         tab.addTab(contact_page, 'Contact Info')

#         main_layout.addWidget(tab, 0, 0, 2, 1)
#         main_layout.addWidget(QPushButton('Save'), 2, 0,
#                             alignment=Qt.AlignmentFlag.AlignLeft)
#         main_layout.addWidget(QPushButton('Cancel'), 2, 0,
#                             alignment=Qt.AlignmentFlag.AlignRight)




# def main():
#     app = QApplication(sys.argv)
#     app.setFont(QFont("Bai Jamjuree",12))

#     window = MainWindow()
#     window.show()

#     sys.exit(app.exec())


# if __name__ == '__main__':
#     main()