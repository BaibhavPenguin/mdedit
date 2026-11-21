"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
assets.py - Asset Loader for MDEdit
"""

from PIL import Image as _Image
from PIL import ImageTk as _ImageTk
import customtkinter as _ctk


class AppAssets:
    __slots__ = ()

    font_trebuchet = "assets/fonts/trebuc.ttf"
    font_adlam = "assets/fonts/adlam-display.ttf"
    font_jetbrains = "assets/fonts/jetbrains-mono.ttf"
    font_oswald = "assets/fonts/oswald.ttf"

    webview2_path = "bin/"
    appicon = None


    @classmethod
    def load_assets(cls):
        _ctk.FontManager.load_font(cls.font_trebuchet)
        _ctk.FontManager.load_font(cls.font_adlam)
        _ctk.FontManager.load_font(cls.font_jetbrains)
        _ctk.FontManager.load_font(cls.font_oswald)

        cls.appicon = _ImageTk.PhotoImage(_Image.open("assets/icons/appicon.png"))


    @staticmethod
    def Oswald(size=16,weight="normal"):

        return _ctk.CTkFont(family="Oswald",size=size,weight=weight)

    @staticmethod
    def Trebuchet(size=16,weight="normal"):
        return _ctk.CTkFont(family="trebuchet",size=size,weight=weight)

    @staticmethod
    def JetBrains(size=16,weight="normal"):
        return _ctk.CTkFont(family="JetBrains Mono",size=size,weight=weight)

    @staticmethod
    def Adlam(size=16,weight="normal"):
        return _ctk.CTkFont(family="ADLaM Display",size=size,weight=weight)



