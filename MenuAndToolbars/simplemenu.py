#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a menubar. The
menubar has one menu with an exit action.

Original Author: Jan Bodnar

Author: Harshit Joshi
Website: harshitjoshi.in
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)  # Add icon to exit menu, add Exit label
        exitAct.setShortcut('Ctrl+Q')  # set shortcut for exit menu
        exitAct.setStatusTip('Exit Application')  # status bar shows 'Exit Application'
        exitAct.triggered.connect(qApp.quit)  # action upon trigger

        self.statusBar()

        menubar = self.menuBar()  # creates menu bar
        fileMenu = menubar.addMenu('&File')  # create a File menu
        fileMenu.addAction(exitAct)  # add action to File menu

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
