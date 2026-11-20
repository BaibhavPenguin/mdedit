"""
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
editor.py - Ui widget for writing markdown, uses CTkCode Edit Initially
"""

from ui.misc import Palette
from ui.assets import AppAssets
from ui.codebox import AppTextBox

class MarkdownEditor(AppTextBox):
    def __init__(self, master):
        super().__init__(
        master=master,
        font= AppAssets.JetBrains(16),
        corner_radius = 1,
        height=240,
        undo=True
        )
