"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
"""

from PySide6.QtWidgets import QMainWindow
from ui.misc import  AppAsset
from ui.menubar import Menubar

class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # Widgets
            self.menubar =Menubar(self)

            # Initializers
            self._initialize_window()
            self._initialize_widget_groups()


        def _initialize_window(self):
            self.setWindowTitle(AppAsset.Title())
            self.setWindowIcon(AppAsset.Icon())
            self.setGeometry(*AppAsset.BaseGeometry())

        def _initialize_widget_groups(self):
            self.setMenuBar(self.menubar)

