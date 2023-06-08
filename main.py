# -*- coding: utf-8 -*-
__author__ = 'Jinbiao Tan'
# @Author  : Jinbiao Tan
# @Time    : 2023/01/28 12:00
# @phone   : 15616114695
# @QQ      : 1780126040
# @Function: App ui main start function.

from cut_images_tool import ui_window, ui_function
import sys
import cv2 as cv
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    qmain = QMainWindow()

    # win = ui_window.Ui_MainWindow().setupUi(qmain)
    d = ui_function.System(qmain)
    qmain.show()
    qmain.setWindowTitle('Quick crop picture tool')

    sys.exit(app.exec_())

    pass
