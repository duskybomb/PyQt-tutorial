#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

Author: Harhsit Joshi
Website: harshitjoshi.in
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    # application object
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)  # window size
    w.move(300, 300)  # window placement
    w.setWindowTitle('Simple')  # window title
    w.show()  # shows window

    sys.exit(app.exec_())  # ensures clean exit
