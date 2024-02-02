import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,  QFormLayout 
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ลงทะเบียน')
        self.setupUI()

    def setupUI(self):
        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow('ชื่อ:', QLineEdit(self))
        layout.addRow('อีเมล:', QLineEdit(self))
        layout.addRow('รหัสผ่าน:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow('ยืนยัน รหัสผ่าน:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow('โทรศัพท์:', QLineEdit(self))
        
        btnOK = QPushButton('บันทึก')
        btnOK.setFixedWidth(150)
        btnOK.clicked.connect(self.btnOKClick)

        btnCancel = QPushButton('ยกเลิก')
        btnCancel.setFixedWidth(150)
        btnCancel.clicked.connect(self.btnCancelClick)

        layout.addRow(btnOK,btnCancel)


    def btnOKClick(self):
        print("OK-Click")


    def btnCancelClick(self):
        print("Cancel-Click")
        self.close()


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Bai Jamjuree",12))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()