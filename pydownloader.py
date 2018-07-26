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

        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.browse_file)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse_btn)
        layout.addWidget(self.progress)
        layout.addWidget(download_btn)

        self.setLayout(layout)
        self.setWindowTitle("MINA Downloader")
        self.setFocus()

    def download(self):
        """
        extract text entered in QLineEdit(), get the 
        URL, location to save on disk and then start
        downloading.
        this function will call report function which 
        calculates the percentage of the downloaded part
        of the file and display it on the progress bar.
        """
        url = self.url.text()
        save_location = self.save_location.text()
        # arg[0] = URL of the file to download
        # arg[1] = location to save on disk
        # arg[2] = report hook, which is the report() function
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed!")
            return

        # when the download finishes successfully, next functions
        # are called to notify the user and reset the program
        QMessageBox.information(self, "Information", "The download is complete!")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")


    def report(self, blocknum, blocksize, totalsize):
        """what percentage of the file has been downloaded
        
        Arguments:
            blocknum {[type]} -- [description]
            blocksize {[type]} -- [description]
            totalsize {[type]} -- [description]
        """
        # first of all calculate size of downloaded parts
        readSoFar = blocknum * blocksize
        if totalsize > 0:
            percent = readSoFar * 100 / totalsize
            self.progress.setValue(int(percent))

    def browse_file(self):
        """Open file save windows dialog, ask the user where
        they want to save their files. then set the QLineEdit
        of the save_location to the chosen destination
        """

        save_file = QFileDialog.getSaveFileName(self,
                                                caption = "Save File As",
                                                directory = ".",
                                                filter = "All Files (*.*)")
        self.save_location.setText(str(save_file[0]))



# Function definitions
# ----------------------------------------------------

# Main Program
# ----------------------------------------------------
app = QApplication(sys.argv)
dialog = pydownloader()
dialog.show()
app.exec_()