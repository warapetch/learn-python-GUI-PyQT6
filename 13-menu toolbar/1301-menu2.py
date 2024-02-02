"""
    Menu and Toolbar
    GridLayout
    30/01/2567
"""

from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel ,QMenu,QMenuBar,QToolBar
from PyQt6.QtGui import QIcon,QAction,QFont
import sys

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("PyQT6 :: Menu Toolbar")
        self.setWindowIcon(QIcon("./asset/windows.ico"))
        self.statusBar().showMessage("Loaded ..")
        self.setFixedSize(680,480)

        self.setupUI()

    def setupUI(self):
        
        actNew = QAction(QIcon("./asset/icons/document.png"),'สร้างใหม่',self)  
        actNew.setShortcut('Ctrl+N')
        actNew.setStatusTip("New Document สร้างไฟล์ใหม่")
        actNew.triggered.connect(self.actNewClick)

        actEdit = QAction(QIcon("./asset/icons/blue-document-text-image.png"),'แก้ไข',self)  
        actEdit.setShortcut('Ctrl+E')
        actEdit.setStatusTip("Edit Document แก้ไขไฟล์")
        actEdit.triggered.connect(self.actEditClick)

        actExit = QAction(QIcon("./asset/icons/cross-circle.png"),'ปิดโปรแกรม',self)  
        actExit.setShortcut('Ctrl+X')
        actExit.setStatusTip("ปิดโปรแกรม")
        actExit.triggered.connect(self.actExitClick)


        tmpMenu = QMenu('เมนูลับ',self)        
        tmpMenu.addAction('ลับ 1')
        tmpMenu.addAction('ลับ 2')


        # Mainmenu
        mainMenu = self.menuBar() # QMenuBar
        #mainMenu = QMenuBar(self)
        menuFile = mainMenu.addMenu('File') # QMenu - item
        menuFile.addAction(actNew) # sub Menu == Menu item
        menuFile.addAction(actEdit)
        menuFile.addMenu(tmpMenu)

        menuFile.addSeparator()
        menuFile.addAction(actExit)

        menuView = mainMenu.addMenu('View')
        
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16, 16)) # 16x16 24x24 32x32
        self.addToolBar(toolbar)
        

        toolbar.addWidget(QLabel("Toolbar"))
        toolbar.addSeparator()

        btnActNew = QAction(QIcon("./asset/icons/document.png"), "สร้างเอกสาร", self) # Hint / Tip
        btnActNew.setStatusTip("New Document สร้างไฟล์ใหม่")
        btnActNew.triggered.connect(self.actNewClick)
        toolbar.addAction(btnActNew)

        toolbar.addSeparator()

        btnActEdit = QAction(QIcon("./asset/icons/blue-document-text-image.png"), "แก้ไขเอกสาร", self)
        btnActEdit.setStatusTip("Edit Document แก้ไขไฟล์")
        btnActEdit.triggered.connect(self.actEditClick)
        toolbar.addAction(btnActEdit)

        btnActExit = QAction(QIcon("./asset/icons/cross-circle.png"), "ปิดโปรแกรม", self)
        btnActExit.setStatusTip("ปิดโปรแกรม")
        btnActExit.triggered.connect(self.actExitClick)
        toolbar.addAction(btnActExit)




    def actNewClick(self):
        print('Click New')

    def actEditClick(self):
        print('Click Edit')

    def actExitClick(self):
        QApplication.quit()
        #QApplication.instance.quit()


def main():
    app = QApplication([])
    app.setFont(QFont('Bai Jamjuree',12))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())



if __name__ == '__main__':
    main()
