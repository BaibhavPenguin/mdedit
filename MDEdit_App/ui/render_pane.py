"""
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
render_pane.py - Ui Widget for rendering markdown as html
"""

import  customtkinter as ctk
import tkinterweb as tkweb
from ui.assets import AppAssets
from ui.test_html import html
from ui.misc import Palette

class WebPreviewButtonBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master=master,
            fg_color=Palette.highlighted_frames,
            corner_radius=0,
            height=40
        )

class WebPreviewLabel(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master=master,
            fg_color=Palette.highlighted_frames,
            corner_radius=0,
            height=40
        )
        self.label = ctk.CTkLabel(self,text="Preview",justify="left",font=AppAssets.Trebuchet(12))
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.label.grid(row=0, column=0, sticky="nsw", pady=3, padx=10)


class TkWebRender(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master,fg_color=Palette.highlighted_frames)
        self.grid_propagate(False)
        self.handler = self.winfo_toplevel().handler

        self.preview_label = WebPreviewLabel(self)
        self.buttonbar = WebPreviewButtonBar(self)
        self.render = tkweb.HtmlFrame(self,javascript_enabled=True,javascript_backend="python")

        # Test Code
        self.render.load_html(html)

        self._configure_gridlayout()
        self._place_widgets()



    def _configure_gridlayout(self):
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)

    def _place_widgets(self):
        self.preview_label.grid(row=0, column=0, sticky="new", pady=0, padx=0)
        self.buttonbar.grid(column=0, row=2, sticky="sew", padx=0, pady=0)
        self.render.grid(column=0, row=1, sticky="nsew", pady=0, padx=0)


    def _on_mousewheel(self,event):
        pass