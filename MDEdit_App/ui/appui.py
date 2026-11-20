"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
appui.py - Main App Ui
"""


import customtkinter as ctk
from ui.assets import AppAssets
from ui.app_handler import AppHandler
from ui.menubar import AppMenubar
from ui.misc import AppVerticalDivider, AppSidebar, AppNavbar
from ui.editor import MarkdownEditor


class AppUi(ctk.CTk):
    def __init__(self):
        # Initialize Base Class
        super().__init__()

        # Asset manager
        AppAssets.load_assets()

        # Widgets
        self.menubar = AppMenubar(self)
        self.vdiv1 = AppVerticalDivider(self)
        self.left_sidebar = AppSidebar(self)
        self.right_sidebar = AppSidebar(self)
        self.navbar = AppNavbar(self)
        self.mdedit = MarkdownEditor(self)



        # Handler
        self.handler = AppHandler()

        # Initialization
        self._initialize_window()
        self._set_appicon()
        self._set_styles()
        self._configure_gridlayout()
        self._set_widget_grids()




    def _set_appicon(self):
        self.after(200, lambda: self.iconphoto(False,AppAssets.appicon))

    def _configure_gridlayout(self):
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=0)


    def _set_widget_grids(self):
        self.menubar.grid(column=0, row=0, columnspan=5, sticky="new")

        self.vdiv1.grid(column=2, row=1, rowspan=2, sticky="ns", pady=5, padx=5)
        self.mdedit.grid(column=1, row=1, sticky="nsew",padx=5,pady=5)

        self.left_sidebar.grid(column=0, row=1, sticky="nsw",rowspan=3)
        self.right_sidebar.grid(column=4, row=1, sticky="nse",rowspan=3)
        self.navbar.grid(column=0, row=3, sticky="nsew",columnspan=5)


    def _initialize_window(self):
        # Window Titles
        self.title("MDEdit")
        # 16:9 Window Size
        self.geometry("1280x720")

    def _set_styles(self):
       ctk.set_appearance_mode("system")



