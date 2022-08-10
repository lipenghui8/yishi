import argparse
import parser
import sys

import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow

import FaceMaskDetection

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = FaceMaskDetection.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
