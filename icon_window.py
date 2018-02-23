#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows an icon
in the titlebar of the window.

Author: Harhsit Joshi
Website: harshitjoshi.in
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()  # constructor of super class
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)  # combines resize() and move()
        self.setWindowTitle('Icon')  # title bar of window
        self.setWindowIcon(QIcon('icon.png'))  # adds icon to the title bar
        self.show()  # starts the window


if __name__ == '__main__':
    app = QApplication(sys.argv)  # application object
    ex = Example()
    sys.exit(app.exec_())  # ensures clean closing
