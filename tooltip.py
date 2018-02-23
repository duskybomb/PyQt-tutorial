#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a tooltip on
a window and a button.

Author: Harshit Joshi
Website: harshitjoshi.in
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Static method sets font used to render tooltip
        QToolTip.setFont(QFont('SansSerif', 10))

        # calling tooltip
        self.setToolTip('This is a <b>Qwidget</b> widget')

        # create tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b> QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
