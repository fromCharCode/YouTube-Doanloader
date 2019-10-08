from __future__ import unicode_literals
from downloader import Downloader
from cmd_interface import CmdInterface
from file_iterator import FileIterator
import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from url_validator import url_is_valid
from shell_controller import duration_information, output_format_information, quick_mp3_download, quick_mp4_download, update_ydl
import logging
from PyQt5.QtGui import QIcon


# eva
# ask for task
# get input
# path -> iterator read
# else just write what is currently saved
# therefore: getName, getDuration, author, link
# this is supposed to become the big logical centre of this program, or the frame around it.
# we need communication between downloader, iterator, etc in here but in a way, that the
# interface could be changed, but uses the same commands in here


logger = logging.getLogger(__name__)  # now we use logger.debug, etc.
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(style="{", fmt="{asctime} [{levelname}] {message}", datefmt="%d.%m.%Y %H:%M:%S")

file_handler = logging.FileHandler('run.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


interface = CmdInterface
fIter = FileIterator
title = ""
link = ""
author = ""
duration = 0

linkList = fIter.link_generator(fIter, "_done.txt")


# begin with qt implementation
app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):


    def read_format(self):
        return self.ui.comboBox.currentText()


    def download(self):
        link = self.ui.lineEdit.text()
        f = self.read_format()

        logger.debug("beginning download..." + f)

        if (f == "mp3"):
            quick_mp3_download(link)
        elif (f == "mp4"):
            quick_mp4_download(link)

        # todo: will be led to a new class: a communicator with the console. (?)

    def get_information(self):
        information = self.sc.output_format_information(self.ui.lineEdit.text())
        for item in information:
            self.ui.comboBox_2.addItem(item)
        #self.title =

    def on_url_change(self):
        # log print("url changed")
        url = self.ui.lineEdit.text()
        if(url_is_valid(url)):
            self.ui.downloadButton.setEnabled(True)
        else:
            self.ui.downloadButton.setDisabled(True)
            self.ui.lineEdit.setText("Your link was not a valid YouTube link...")
            # this string will cause a graying of each element. yeah

    def __init__(self, parent=None):
        super().__init__(parent)

        update_ydl()
        logger.info("updater finished")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dl = Downloader
        self.setWindowIcon(QIcon("icons/Ydl_V2.png"))
        self.ui.downloadButton.clicked.connect(self.download)
        self.ui.lineEdit.textChanged.connect(self.on_url_change)
        self.setWindowTitle("Youtube Downloader Version Alpha 0.4.2")


window = MainWindow()
window.show()


def set_label_updating(self):
    window.ui.label.setText("Updating... Please wait")


def set_label_downloading(self):
    window.ui.label.setText("Downloading...")


def set_label_success(self):
    window.ui.label.setText("Download succeeded")


# for future cases
def set_label_failed(self):
    window.ui.label.setText("Download failed")


# should be called from extern, like downloader
def write_saved(self, link):
    with open("_done.txt", "w") as file:
        file.writelines(link)


sys.exit(app.exec_())
