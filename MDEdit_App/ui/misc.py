from ui.assets import AppAssets
import customtkinter as ctk



class Palette:
    frame_colors = ("gray86", "gray17")
    menubar_item_colors = ("gray86", "gray17")
    menubar_label_colors = ("#1A1A1A", "#D6D6D6")
    placeholder_text = ("gray35","gray92")
    title_text = ("#1A1A1A", "#EBEBEB")
    code = "#6E7781"
    menu_hover = ("#2E2E2E", "#C4C4C4")
    highlighted_frames = ("#cfcfcf","#1f1f1f")



class AppHorizontalDivider(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master,
            bg_color="transparent",
            fg_color=Palette.frame_colors,
            height=5,
            corner_radius = 10
        )




class AppVerticalDivider(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master,
            bg_color="transparent",
            fg_color=Palette.frame_colors,
            width=5,
            corner_radius = 10
        )



class AppSidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master=master,
            fg_color=Palette.frame_colors,
            corner_radius=0,
            width=30
        )


class AppNavbar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master=master,
            fg_color=Palette.frame_colors,
            corner_radius=0,
            height=30
        )


SYMBOLS = (
    "—  Em Dash",
    "–  En Dash",
    "…  Ellipsis",
    "•  Bullet",
    "©  Copyright",
    "™  Trademark",
    "®  Registered",
    "°  Degree",
    "±  Plus-Minus",
    "→  Right Arrow",
    "←  Left Arrow",
    "↑  Up Arrow",
    "↓  Down Arrow",
    "View more..."
)