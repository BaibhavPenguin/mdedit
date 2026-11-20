"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
app_handler.py - Handler functions for all ui elements
"""



import customtkinter as ctk
class AppHandler:

    def __init__(self):
       pass

    @staticmethod
    def update_style(style):
        if style == "dark":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
