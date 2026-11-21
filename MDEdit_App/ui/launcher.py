"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
"""

from ui.mainwindow import MainWindow
from PySide6.QtWidgets import QApplication
import sys

class AppLauncher(QApplication):

    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.window.show()

    def launch(self):
        sys.exit(self.exec_())