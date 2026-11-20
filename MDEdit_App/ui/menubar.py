"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
menubarmenubar.py - Ui Widget menubar/toolbar and its elements
"""

import customtkinter as ctk
from ui.misc import Palette
from ui.assets import AppAssets
from ui.app_handler import AppHandler



"""
    Subclassing CTkOptionMenu to make the arrows disappear and make it act as a menubar.
"""
class MenubarItem(ctk.CTkOptionMenu):

    def __init__(self, master, **kwargs):
        if "fg_color" in kwargs:
            kwargs.setdefault("button_color", kwargs["fg_color"])
            kwargs.setdefault("button_hover_color", kwargs["fg_color"])

        super().__init__(master, **kwargs)


        super().configure(button_color=self._fg_color)
        super().configure(button_hover_color=self._fg_color)

        self._text_label.configure(anchor="center")
        self._text_label.grid(row=0, column=0, padx=(5,5), pady=4, sticky="nsew",columnspan=2)

    def _draw(self, no_color_updates=False):
        super()._draw(no_color_updates)
        self._canvas.delete("dropdown_arrow")

    def configure(self, require_redraw=False, **kwargs):
        if "fg_color" in kwargs:
            kwargs.setdefault("button_color", kwargs["fg_color"])
            kwargs.setdefault("button_hover_color", kwargs["fg_color"])

        super().configure(require_redraw=require_redraw, **kwargs)



class AppMenubar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master=master,
            fg_color=Palette.frame_colors,
            corner_radius=0,
            height=50,
        )


        self.file_options = MenubarItem(self,command=self._file_options_command)
        self.theme_options = MenubarItem(self,command=self._theme_options_command)
        self.download_options = MenubarItem(self,command=self._download_options_command)
        self.appearance = MenubarItem(self,command=self._appearance_options_command)
        self.theme_display = ctk.CTkEntry(self)

        self._configure_gridlayout()
        self._configure_widgets()
        self._place_widgets()


    def _configure_gridlayout(self):
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=1)

    def _configure_widgets(self):
        self.file_options.set("File")
        self.theme_options.set("Themes")
        self.download_options.set("Export")
        self.appearance.set("Appearance")

        self.file_options.configure(
            values=("New","Open","Save","Save As"),
            fg_color=Palette.menubar_item_colors,
            text_color=Palette.menubar_label_colors,
            font=AppAssets.Trebuchet(12),
            width=50
        )


        self.download_options.configure(
            values=("Markdown" , "PDF" , "HTML"),
            fg_color=Palette.frame_colors,
            text_color=Palette.menubar_label_colors,
            font=AppAssets.Trebuchet(12),
            width=50
        )

        self.theme_options.configure(
            values=("Default","MDEdit Modern","MDEdit Classic"),
            fg_color=Palette.menubar_item_colors,
            text_color=Palette.menubar_label_colors,
            font=AppAssets.Trebuchet(12),
            width =60
        )

        self.theme_display.configure(
            placeholder_text="Default",
            placeholder_text_color=Palette.placeholder_text,
            corner_radius = 5,
            width = 400,
            font=AppAssets.JetBrains(12),
            border_color=Palette.menubar_item_colors,
            state="disabled"
        )

        self.appearance.configure(
            values=("Dark","Light"),
            fg_color=Palette.menubar_item_colors,
            text_color=Palette.menubar_label_colors,
            font=AppAssets.Trebuchet(12),
            width=70,
        )



    def _place_widgets(self):
        self.file_options.grid(column=0, row=0, sticky="nsew" , padx=(0,5))
        self.appearance.grid(column=1, row=0, sticky="nsew", padx=5)
        self.theme_options.grid(column=2, row=0, sticky="nsew" , padx=5)
        self.download_options.grid(column=3, row=0, sticky="nsw", padx=5,pady=2)
        self.theme_display.grid(column=3, row=0, sticky="nse", padx=28,pady=2)



    def _file_options_command(self,choice):
        self.file_options.set("File")

    def _theme_options_command(self,choice):
        self.theme_options.set("Themes")
        self.theme_display.configure(state="normal")
        self.theme_display.delete(0,"end")
        self.theme_display.insert(0,choice)
        self.theme_display.configure(state="disabled")

    def _download_options_command(self,choice):
        self.download_options.set("Export")

    def _appearance_options_command(self,choice):
        self.appearance.set("Appearance")
        AppHandler.update_style(choice.lower())