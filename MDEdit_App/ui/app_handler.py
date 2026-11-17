"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
app_handler.py - Handler functions for all ui elements
"""


import pywinstyles as pys

class AppHandler():
    def __init__(self,
                 app,
                 assets):

        self.app = app
        self.assets = assets


    def _set_appicon(self):
        self.app.after(200, lambda: self.app.iconphoto(self.assets.appicon))

    def initialize_window(self):
        # Window Titles
        self.app.title("MDEdit")

        # 16:9 Window Size
        self.app.geometry("1280x720")

        # Window Style
        pys.apply_style(self.app, "acrylic")

        # Apply Window Icon
        self.app.after(200, lambda: self.app.iconphoto(False,self.assets.appicon))

