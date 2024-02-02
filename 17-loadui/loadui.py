"""
    by: วรเพชร  เรืองพรวิสุทธิ์
    create: 1/2/2567
"""

import sys ,os

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6.QtCore import QCoreApplication,QDate
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        pass


    def loadUI(self,uiFileName: str):

        try:
            uic.loadUi(uiFileName, self)
            print('loadUI = [OK]')
            
            self.setupUI()           
            return True
        
        except Exception as err:
            print(err)


    def setupUI(self):
        print('setupUI [Enter]')

        self.btnOK.clicked.connect(self.btnOKClick)
        self.btnCancel.clicked.connect(self.btnCancelClick)
        self.deBirth.setDate(QDate.currentDate())

        pass


    def btnOKClick(self):
        print('btnOKClick Click')

        print(self.leName.text())
        print(self.leLastName.text())
        print(self.deBirth.text())


    def btnCancelClick(self):
        print('btnCancelClick Click')

def main():

    # รับค่า instance ถ้าเคยมีการสั่งรันไว้ก่อนหน้านี้
    app = QCoreApplication.instance()
    # ถ้าไม่มีการรัน ค่าที่ได้คือ None
    # PyQT API อาจแจ้ง Error ถ้า app != None !! Freeze !!
    # 1 app ต้องมี 1 instance เท่านั้น
    
    if app is None:
        app = QApplication([])

    # set app
    app.setFont(QFont('Bai Jamjuree',12))
    
    # check file UI
    pathFileName = 'ui/ui01.ui'
    if os.path.exists(pathFileName) :
        print('Path+FileName = OK')        
    else:
        print('Path+FileName = NOT_FOUND')
    
    # load UI
    window = MainWindow()
    if window.loadUI(pathFileName) == True:
        window.show()
        sys.exit(app.exec())
    else:
        print('loadUI Error !!')



if __name__ == '__main__':
    main()
