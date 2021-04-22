from qt_biz_process import biz_process
import sys
import time
from PyQt5.QtWidgets import QWidget, QProgressBar, QApplication

class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 200, 25)
        self.progressBar.setMaximum(100)
        self.progressBar.setWindowTitle("In Progress...")

    def set_progressbar(self, i):
        self.progressBar.setValue(i)

if __name__=='__main__':
    app = QApplication(sys.argv)

    _ProgressBar = ProgressBar()
    _ProgressBar.show()

    # Get the process_status
    for process_status in biz_process():
        _ProgressBar.set_progressbar(process_status)
        QApplication.processEvents()

    print("<-- Completed -->")
    _ProgressBar.close()

    # sys.exit(app.exec_())



