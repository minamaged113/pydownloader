"""
This file will hold the first application
Tutorial: https://www.youtube.com/watch?v=nAyi62r4SDk&list=PLbW_am_GRTo3D2HNO3PICb-n8Fi8k6VCR

"""
# Libraries include
# ----------------------------------------------------
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import urllib.request

# Global variables
# ----------------------------------------------------

# Classes definitions
# ----------------------------------------------------
class pydownloader (QDialog):
    def __init__(self):
        QDialog.__init__(self)
        
        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.url.setPlaceholderText("Enter download URL")

        self.save_location = QLineEdit()
        self.save_location.setPlaceholderText("Save location")

        self.progress = QProgressBar()
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        download_btn = QPushButton("Download")
        download_btn.clicked.connect(self.download)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(download_btn)

        self.setLayout(layout)
        self.setWindowTitle("MINA Downloader")
        self.setFocus()

    def download(self):
        # next lines will extract text entered in QLineEdit()
        url = self.url.text()
        save_location = self.save_location.text()
        urllib.request.urlretrieve(url, save_location, self.report)


    def report(self, blocknum, blocksize, totalsize):
        pass

# Function definitions
# ----------------------------------------------------

# Main Program
# ----------------------------------------------------
app = QApplication(sys.argv)
dialog = pydownloader()
dialog.show()
app.exec_()