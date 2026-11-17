"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
appui.py - Main App Ui
"""

import customtkinter as ctk
from ui.assets import AppAssets
from ui.app_handler import AppHandler

class AppUi(ctk.CTk):
    def __init__(self):
        # Initialize Base Class
        super().__init__()

        # Asset manager
        self.assets = AppAssets()

        # Widgets

        # Handler
        handler = AppHandler(app=self, assets=self.assets)

        # Window Setup
        handler.initialize_window()







