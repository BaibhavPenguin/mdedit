"""
CTkCodeBox
Author: Akash Bora
License: MIT

Has been significantly modified and integrated with the ui package of MDEdit by Baibhav Bhattacharya
"""

import customtkinter as ctk
import tkinter
from tklinenums import TkLineNumbers
from ui.misc import Palette


class TextMenu(tkinter.Menu):
    """
    Popup Text Menu for CTkTextbox and CTkEntry
    Author: Akash Bora
    """

    def __init__(
        self,
        widget,
        fg_color=None,
        text_color=None,
        hover_color=None,
        **kwargs
    ):
        super().__init__(tearoff=False, title="menu", borderwidth=0, bd=0, relief="flat", **kwargs)

        self.widget = widget
        self._custom_fg_color = fg_color
        self._custom_text_color = text_color
        self._custom_hover_color = hover_color

        self.add_command(label="Cut", command=self.cut_text)
        self.add_command(label="Copy", command=self.copy_text)
        self.add_command(label="Paste", command=self.paste_text)
        self.add_command(label="Delete", command=self.clear_text)
        self.add_command(label="Clear All", command=self.clear_all_text)
        self.add_command(label="Select All", command=self.select_all_text)
        self.add_command(label="Undo", command=self.undo_text)

        self.widget.bind("<Button-3>", self.do_popup, add=True)
        self.widget.bind("<Button-2>", self.do_popup, add=True)

    def _resolve_colors(self):
        """Dynamically resolve colors from ThemeManager at popup time so theme changes work."""
        fg = (
            ctk.ThemeManager.theme["CTkFrame"]["top_fg_color"]
            if self._custom_fg_color is None else self._custom_fg_color
        )
        txt = (
            ctk.ThemeManager.theme["CTkLabel"]["text_color"]
            if self._custom_text_color is None else self._custom_text_color
        )
        hover = (
            ctk.ThemeManager.theme["CTkButton"]["hover_color"]
            if self._custom_hover_color is None else self._custom_hover_color
        )
        return (
            self.widget._apply_appearance_mode(fg),
            self.widget._apply_appearance_mode(txt),
            self.widget._apply_appearance_mode(hover),
        )

    def do_popup(self, event):
        """Open the popup menu with current theme colors."""
        bg_col, fg_col, active_col = self._resolve_colors()
        super().config(
            bg=bg_col,
            fg=fg_col,
            activebackground=active_col,
            activeforeground=fg_col
        )
        self.tk_popup(event.x_root, event.y_root)

    def cut_text(self):
        self.copy_text()
        try:
            self.widget.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        except Exception:
            pass

    def copy_text(self):
        try:
            self.widget.clipboard_clear()
            self.widget.clipboard_append(self.widget.get(tkinter.SEL_FIRST, tkinter.SEL_LAST))
        except Exception:
            pass

    def paste_text(self):
        try:
            self.widget.insert(self.widget.index("insert"), self.widget.clipboard_get())
        except Exception:
            pass

    def clear_all_text(self):
        try:
            self.widget.delete("0.0", "end")
        except Exception:
            pass

    def select_all_text(self):
        try:
            self.widget.tag_add("sel", "0.0", "end")
        except Exception:
            pass

    def clear_text(self):
        try:
            self.widget.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        except Exception:
            pass

    def undo_text(self):
        try:
            self.widget.edit_undo()
            self.widget.event_generate("<<ContentChanged>>")
        except Exception:
            pass


class AddLineNums(TkLineNumbers):
    """
    Adds dynamically sized line numbers to a CTkTextbox
    using TkLineNumbers with full custom2kinter appearance/theme support.
    """

    def __init__(
        self,
        master,
        text_color=None,
        justify="left",
        padx=12,
        **kwargs
    ):
        self.master = master
        self._custom_text_color = text_color
        self._base_padx = padx
        self._digit_padding = 12
        self._digit_width = 10

        # Strip font from kwargs because TkLineNumbers forwards kwargs to tk.Canvas
        kwargs.pop("font", None)

        fg_hex, bg_hex = self._get_resolved_colors()

        super().__init__(
            self.master,
            self.master._text,
            justify=justify,
            colors=(fg_hex, bg_hex),
            relief="flat",
            highlightthickness=0,
            height=self.master.winfo_reqheight(),
            **kwargs
        )

        padding = (
            self.master.cget("border_width")
            + self.master.cget("corner_radius")
        )

        # Match the exact vertical grid padding of _text so top edges align
        tb_grid = self.master._text.grid_info()
        tb_pady = tb_grid.get("pady", padding)

        super().grid(
            row=0,
            column=0,
            sticky="nsw",
            padx=(padding, 0),
            pady=tb_pady
        )

        self.master._text.lift()

        # Bind vertical scroll properly without breaking master's vertical scrollbar
        self.master._text.configure(yscrollcommand=self.set_scrollbar)

        self.master._text.bind("<<ContentChanged>>", self._on_content_changed, add=True)
        self.master.bind("<Key>", lambda e: self.after(10, self._on_content_changed), add=True)
        self.master.bind("<Configure>", lambda e: self.after(10, self._on_configure), add=True)

        self.sync_font()

    def _get_resolved_colors(self):
        """Resolve foreground (number) and background (gutter) colors for the current theme."""
        raw_text_color = (
            self.master.cget("border_color")
            if self._custom_text_color is None else self._custom_text_color
        )
        raw_fg_color = self.master.cget("fg_color")

        if raw_fg_color == "transparent":
            raw_fg_color = ctk.ThemeManager.theme["CTkTextbox"]["fg_color"]

        return (
            self.master._apply_appearance_mode(raw_text_color),
            self.master._apply_appearance_mode(raw_fg_color),
        )

    def update_theme_colors(self):
        """Re-apply colors when either appearance mode (Light/Dark) or color theme changes."""
        fg_hex, bg_hex = self._get_resolved_colors()
        self.colors = (fg_hex, bg_hex)
        try:
            self.configure(bg=bg_hex)
            self.set_colors()
            self.redraw()
        except Exception:
            pass

    def _on_configure(self):
        self.update_line_number_width()
        self.redraw()

    def sync_font(self):
        """Sync TkLineNumbers font with the master textbox font."""
        try:
            tb_font = self.master._text.cget("font")
            self.font = tb_font
            self.itemconfigure("all", font=tb_font)
            self.update_line_number_width()
            self.redraw()
        except Exception:
            pass

    def redraw(self, *args):
        super().redraw(*args)
        try:
            tb = self.master._text
            tb_font = tb.cget("font")
            self.itemconfigure("all", font=tb_font)

            # Align vertical position dynamically using dlineinfo of the first visible line
            first_visible = tb.index("@0,0")
            dline = tb.dlineinfo(first_visible)
            items = self.find_all()
            if dline is not None and items:
                canvas_y_offset = self.winfo_y() - tb.winfo_y()
                target_y = dline[1] - canvas_y_offset
                first_bbox = self.bbox(items[0])
                if first_bbox is not None:
                    dy = target_y - first_bbox[1]
                    if dy != 0:
                        self.move("all", 0, dy)
        except Exception:
            pass

    def update_line_number_width(self):
        try:
            total_lines = int(self.master._text.index("end-1c").split(".")[0])
            digits = len(str(max(1, total_lines)))
            font = self.master._text.cget("font")

            try:
                actual_digit_width = max(
                    self.master._text.tk.call("font", "measure", font, "0"),
                    self.master._text.tk.call("font", "measure", font, "9")
                )
            except Exception:
                actual_digit_width = self._digit_width

            new_width = digits * actual_digit_width + self._digit_padding
            self.configure(width=new_width)

            self.master._text.grid_configure(
                padx=(new_width + self._base_padx, 0)
            )
        except Exception:
            pass

    def _on_content_changed(self, event=None):
        self.update_line_number_width()
        self.redraw()

    def set_scrollbar(self, x, y):
        self.redraw(x, y)
        if hasattr(self.master, "_y_scrollbar") and self.master._y_scrollbar is not None:
            self.master._y_scrollbar.set(x, y)

    def _set_appearance_mode(self, mode_string):
        self.update_theme_colors()
        self.update_line_number_width()


class AppTextBox(ctk.CTkTextbox):
    def __init__(self, master, undo=True, height=200, **kwargs):
        super().__init__(master, undo=undo, height=height, **kwargs)

        self.cursor_color = "#F97316"
        self.select_color = "#C2410C"
        self.select_width = 2

        self.configure(wrap="word")

        self.line_nums = AddLineNums(self, text_color=Palette.code)
        self.text_menu = TextMenu(
            self,
            fg_color=Palette.frame_colors,
            text_color=Palette.menubar_label_colors,
            hover_color=Palette.menu_hover
        )

        self._apply_text_selection_colors()

        self.bind("<KeyRelease>", self.update_code, add=True)
        self.bind("<<ContentChanged>>", self.update_code, add=True)
        self.bind("<Control-a>", lambda e: self.after(50, self._select_all), add=True)
        self.bind("<Control-n>", lambda e: self.clear_code(), add=True)
        self.bind("<Control-s>", self.on_save, add=True)
        self.edited = False

    def _apply_text_selection_colors(self):
        self._text.config(
            selectbackground=self._apply_appearance_mode(self.select_color),
            selectforeground="#FFFFFF",
            insertbackground=self._apply_appearance_mode(self.cursor_color),
            insertwidth=self.select_width,
        )

    def update_code(self, event=None, edited=True):
        self.edited = edited

    def on_save(self, event=None):
        self.edited = False

    def clear_code(self):
        for tag in self.tag_names():
            self.tag_remove(tag, "0.0", "end")

    def _select_all(self):
        self.tag_add("sel", "0.0", "end")

    def insert(self, index, text, tags=None):
        super().insert(index, text, tags)
        self.edit_reset()
        self.edited = False
        if hasattr(self, "line_nums"):
            self.line_nums._on_content_changed()

    def configure(self, require_redraw=False, **kwargs):
        if "select_color" in kwargs:
            self.select_color = kwargs.pop("select_color")
            self._apply_text_selection_colors()
        if "cursor_color" in kwargs:
            self.cursor_color = kwargs.pop("cursor_color")
            self._apply_text_selection_colors()

        font_changed = "font" in kwargs
        color_changed = any(k in kwargs for k in ("fg_color", "border_color", "text_color"))

        super().configure(require_redraw=require_redraw, **kwargs)

        if hasattr(self, "line_nums"):
            if font_changed:
                self.line_nums.sync_font()
            if color_changed:
                self.line_nums.update_theme_colors()

    def cget(self, attribute_name):
        if attribute_name == "select_color":
            return self.select_color
        if attribute_name == "cursor_color":
            return self.cursor_color
        return super().cget(attribute_name)

    def _set_appearance_mode(self, mode_string):
        super()._set_appearance_mode(mode_string)
        self._apply_text_selection_colors()
        if hasattr(self, "line_nums"):
            self.line_nums._set_appearance_mode(mode_string)