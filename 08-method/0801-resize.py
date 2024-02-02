from PyQt6.QtWidgets import QApplication, QMainWindow, QSizePolicy, QLabel, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):  
    def __init__(self, parent=None):
        super().__init__(parent)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)        
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout(central_widget)
        
        self.label_1 = QLabel(self)
        self.label_1.setStyleSheet('background-color: green')
        self.label_1.setFixedHeight(100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.label_1.setSizePolicy(sizePolicy)
        self.layout.addWidget(self.label_1)
        
        self.label_2 = QLabel(self)
        self.label_2.setStyleSheet('background-color: red')
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.label_2.setSizePolicy(sizePolicy)
        self.layout.addWidget(self.label_2)
        self.show()
        # ~ print('label_1 Size Before Expanding: ', self.label_1.width(), self.label_1.height())
        # ~ print('label_2 Size Before Expanding: ', self.label_2.width(), self.label_2.height())
        self.showMaximized()
        # ~ print('label_1 Size After Expanding: ', self.label_1.width(), self.label_1.height())
        # ~ print('label_2 Size After Expanding: ', self.label_2.width(), self.label_2.height())
        
    def resizeEvent(self, event):
        print('self Size : ', self.width(), self.height())
        print('label_1 Size : ', self.label_1.width(), self.label_1.height())
        print('label_2 Size : ', self.label_2.width(), self.label_2.height())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setFixedSize(480,260)
    app.exec()