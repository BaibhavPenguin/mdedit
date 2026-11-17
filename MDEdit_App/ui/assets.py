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
    def __init__(self):
        _ctk.FontManager.load_font("assets/fonts/oswald.ttf")
        _ctk.FontManager.load_font("assets/fonts/trebuc.ttf")
        _ctk.FontManager.load_font("assets/fonts/jetbrains-mono.ttf")
        _ctk.FontManager.load_font("assets/fonts/adlam-display.ttf")

        # Fonts
        self.font_oswald = _ctk.CTkFont("Oswald",22,"bold")


        # Icons
        self.appicon = _ImageTk.PhotoImage(_Image.open("assets/icons/appicon.png"))

