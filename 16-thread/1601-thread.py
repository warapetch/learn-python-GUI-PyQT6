"""
    https://www.pythontutorial.net/pyqt/pyqt-qthread/

"""

import sys
import time
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, 
                            QVBoxLayout, QProgressBar)
from PyQt6.QtCore import (QThread, QObject, 
                        pyqtSignal as Signal, pyqtSlot as Slot)
from PyQt6.QtGui import QFont



class Worker(QObject):
    
    # Assign New Event/Signal
    progressed = Signal(int)
    completed = Signal(int)

    # def __init__(self):
    #     super().__init__()
    #     pass

    @Slot(int)
    def runProcess(self, maxLoop):
        # process
        for i in range(1, maxLoop+1):
            time.sleep(0.5) # 500 ms
            print(f"i={i} , maxLoop={maxLoop}")

            # update progressed Status
            self.progressed.emit(i)

        # end >> process completed
        self.completed.emit(maxLoop)

# end class Worker ------------------------------


class MainWindow(QMainWindow):
    # Assign New Event/Signal
    processRequest = Signal(int)

    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 100)
        self.setWindowTitle('ตัวอย่าง QThread')
        self.setupUI()


    def setupUI(self):
        
        # setup widget
        self.widget = QWidget()

        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)       

        self.progressbar = QProgressBar(self)
        self.progressbar.setValue(0)

        self.btnStart = QPushButton('เริ่ม Process', clicked = self.btnStartClick)
        #self.btnStart.clicked.connect(self.btnStartClick)

        layout.addWidget(self.progressbar)
        layout.addWidget(self.btnStart)

        # Thread
        self.mainThread = QThread()

        self.worker = Worker()
        self.worker.progressed.connect(self.progressbarUpdate)
        self.worker.completed.connect(self.progressComplete)
        
        # move worker to the worker thread
        self.worker.moveToThread(self.mainThread)

        # Binding processRequest To worker.runProcess 
        self.processRequest.connect(self.worker.runProcess)

        # start the thread
        self.mainThread.start()


    def btnStartClick(self):
        self.btnStart.setEnabled(False)
        loop = 5
        self.progressbar.setMaximum(loop)
        self.processRequest.emit(loop)


    def progressbarUpdate(self, value):
        self.progressbar.setValue(value)


    def progressComplete(self, value):
        self.progressbar.setValue(value)
        self.btnStart.setEnabled(True)


    def closeEvent(self, event):
        print('window close')
        self.mainThread.quit()
        self.mainThread.wait()

# end class MainWindow ------------------------------


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Bai Jamjuree",12))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()