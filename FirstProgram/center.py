#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program centers a window
on the screen.

Original Author: Jan Bodnar

Author: Harshit Joshi
Website: harshitjoshi.in
"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()  # get a rectangle specifying the geometry of the main window
        cp = QDesktopWidget().availableGeometry().center()  # Figure out resolution of the window and get center point
        qr.moveCenter(cp)  # set center of the rectangle at center of the screen
        self.move(qr.topLeft())  # move top-left point of the application to top left of the rectangle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
