#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a submenu.

Original Author: Jan Bodnar

Author: Harshit Joshi
Website: harshitjoshi.in
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)  # submenu Import > Import mail
        impMenu.addAction(impAct)  # shows Import mail submenu

        newAct = QAction('New', self)  # simple menu

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())