"""
CTkCodeBox
Author: Akash Bora
License: MIT

Has been significantly modified and integrated with the ui package of MDEdit by Baibhav Bhattacharya
Dropped Syntax Highlighting
"""

import customtkinter
import tkinter
from tklinenums import TkLineNumbers
from ui.misc import Palette


class TextMenu(tkinter.Menu):
    """
    Popup Text Menu for CTkTextbox and CTkEntry
    Author: Akash Bora
    """

    def __init__(self,
                 widget,
                 fg_color=None,
                 text_color=None,
                 hover_color=None,
                 **kwargs):

        super().__init__(tearoff=False, title="menu", borderwidth=0, bd=0, relief="flat", **kwargs)

        self.fg_color = customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"] if fg_color is None else fg_color
        self.text_color = customtkinter.ThemeManager.theme["CTkLabel"][
            "text_color"] if text_color is None else text_color
        self.hover_color = customtkinter.ThemeManager.theme["CTkButton"][
            "hover_color"] if hover_color is None else hover_color

        self.widget = widget

        self.add_command(label="Cut", command=self.cut_text)
        self.add_command(label="Copy", command=self.copy_text)
        self.add_command(label="Paste", command=self.paste_text)
        self.add_command(label="Delete", command=self.clear_text)
        self.add_command(label="Clear All", command=self.clear_all_text)
        self.add_command(label="Select All", command=self.select_all_text)

        self.add_command(label="Undo", command=self.undo_text)

        self.widget.bind("<Button-3>", lambda event: self.do_popup(event))
        self.widget.bind("<Button-2>", lambda event: self.do_popup(event))

    def do_popup(self, event):
        """ open the popup menu """

        super().config(bg=self.widget._apply_appearance_mode(self.fg_color),
                       fg=self.widget._apply_appearance_mode(self.text_color),
                       activebackground=self.widget._apply_appearance_mode(self.hover_color))
        self.tk_popup(event.x_root, event.y_root)

    def cut_text(self):
        """ cut text operation """
        self.copy_text()
        try:
            self.widget.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        except:
            pass

    def copy_text(self):
        """ copy text operation """
        try:
            self.clipboard_clear()
            self.clipboard_append(self.widget.get(tkinter.SEL_FIRST, tkinter.SEL_LAST))
        except:
            pass

    def paste_text(self):
        """ paste text operation """
        try:
            self.widget.insert(self.widget.index('insert'), self.clipboard_get())
        except:
            pass

    def clear_all_text(self):
        """ clears sll the text """
        try:
            self.widget.delete(0.0, "end")
        except:
            pass

    def select_all_text(self):
        """ clears sll the text """
        try:
            self.widget.tag_add("sel", "0.0", "end")
        except:
            pass

    def clear_text(self):
        """ clears sll the text """
        try:
            self.widget.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        except:
            pass

    def undo_text(self):
        try:
            self.widget.edit_undo()
            self.widget.event_generate("<<ContentChanged>>")
        except:
            pass


class AddLineNums(TkLineNumbers):
    """
    Adds dynamically sized line numbers to a CTkTextbox
    using TkLineNumbers.
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

        self.text_color = (
            self.master.cget("border_color")
            if text_color is None else text_color
        )

        self.fg_color = self.master.cget("fg_color")

        self._base_padx = padx
        self._digit_padding = 12
        self._digit_width = 10

        customtkinter.windows.widgets.appearance_mode.CTkAppearanceModeBaseClass.__init__(
            self
        )

        # Strip font from kwargs because TkLineNumbers forwards kwargs to tk.Canvas
        kwargs.pop("font", None)

        super().__init__(
            self.master,
            self.master,
            justify=justify,
            colors=(
                self.master._apply_appearance_mode(self.text_color),
                self.master._apply_appearance_mode(self.fg_color)
            ),
            relief="flat",
            height=self.master.winfo_reqheight(),
            **kwargs
        )

        padding = (
            self.master.cget("border_width")
            + self.master.cget("corner_radius")
        )

        # Match the exact vertical grid padding of _textbox so top edges align
        tb_grid = self.master._textbox.grid_info()
        tb_pady = tb_grid.get("pady", padding)

        super().grid(
            row=0,
            column=0,
            sticky="nsw",
            padx=(padding, 0),
            pady=tb_pady
        )

        self.master._textbox.lift()

        self.master._textbox.configure(
            yscrollcommand=self.set_scrollbar
        )

        self.master._textbox.bind(
            "<<ContentChanged>>",
            self._on_content_changed,
            add=True
        )

        self.master.bind(
            "<Key>",
            lambda e: self.after(10, self._on_content_changed),
            add=True
        )

        self.master.bind(
            "<Configure>",
            lambda e: self.after(10, self._on_configure),
            add=True
        )

        self.sync_font()

    def _on_configure(self):
        self.update_line_number_width()
        self.redraw()

    def sync_font(self):
        """Sync TkLineNumbers font with the master textbox font."""
        try:
            tb_font = self.master._textbox.cget("font")
            self.font = tb_font
            self.itemconfigure("all", font=tb_font)
            self.update_line_number_width()
            self.redraw()
        except Exception:
            pass

    def redraw(self, *args):
        super().redraw(*args)
        try:
            tb = self.master._textbox
            tb_font = tb.cget("font")
            self.itemconfigure("all", font=tb_font)

            # Align vertical position dynamically using dlineinfo of the first visible line
            first_visible = tb.index("@0,0")
            dline = tb.dlineinfo(first_visible)
            items = self.find_all()
            if dline is not None and items:
                # Compare the top of the first line number bbox to the text widget's y-offset
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
            total_lines = int(
                self.master._textbox.index("end-1c").split(".")[0]
            )

            digits = len(str(max(1, total_lines)))

            font = self.master._textbox.cget("font")

            try:
                actual_digit_width = max(
                    self.master._textbox.tk.call(
                        "font", "measure", font, "0"
                    ),
                    self.master._textbox.tk.call(
                        "font", "measure", font, "9"
                    )
                )
            except Exception:
                actual_digit_width = self._digit_width

            new_width = (
                digits * actual_digit_width
                + self._digit_padding
            )

            self.configure(width=new_width)

            self.master._textbox.grid_configure(
                padx=(new_width + self._base_padx, 0)
            )

        except Exception:
            pass

    def _on_content_changed(self, event=None):

        self.update_line_number_width()
        self.redraw()

    def set_scrollbar(self, x, y):

        self.redraw(x, y)

        self.master._y_scrollbar.set(x, y)

    def _set_appearance_mode(self, mode_string):

        self.colors = (
            self.master._apply_appearance_mode(self.text_color),
            self.master._apply_appearance_mode(self.fg_color)
        )

        self.set_colors()

        self.update_line_number_width()


class AppTextBox(customtkinter.CTkTextbox):
    def __init__(self, master, undo, height, **kwargs):

        super().__init__(master, undo=undo, height=height, **kwargs)

        self.cursor_color = "#F97316"
        self.select_color = "#C2410C"
        self.select_width = 2

        self.configure(wrap="word")
        self.line_nums = AddLineNums(self, text_color=Palette.code)
        TextMenu(self, fg_color=Palette.frame_colors, text_color=Palette.menubar_label_colors, hover_color=Palette.menu_hover)

        self._textbox.config(selectbackground=self.select_color, selectforeground="#FFFFFF")
        self._textbox.config(insertbackground=self.cursor_color, insertwidth=2)

        self.bind('<KeyRelease>', self.update_code)  # When a key is released, update the code
        self.bind('<<ContentChanged>>', self.update_code)
        self.bind("<Control-a>", lambda e: self.after(200, self._select_all), add=True)
        self.bind("<Control-n>", lambda e: self.clear_code(), add=True)
        self.bind("<Control-s>", self.on_save, add=True)
        self.edited = False

    def update_code(self, event=None):
        self.edited = True

    def on_save(self, event=None):
        self.edited = False

    def clear_code(self):
        for tag in self.tag_names():
            self.tag_remove(tag, '0.0', 'end')

    def _select_all(self):
        self.tag_add("sel", "0.0", "end")

    def insert(self, start, end):
        super().insert(start, end)
        self.update_code(edited=False)
        self.edit_reset()
        self.edited = False

    def configure(self, param=None, **kwargs):
        if "select_color" in kwargs:
            self.select_color = kwargs.pop("select_color")
            self._textbox.config(selectbackground=self.select_color)
        if "cursor_color" in kwargs:
            self.cursor_color = kwargs.pop("cursor_color")
            self._textbox.config(insertbackground=self.cursor_color)
        font_changed = "font" in kwargs
        super().configure(**kwargs)
        if font_changed and hasattr(self, "line_nums"):
            self.line_nums.sync_font()

    def cget(self, param):
        if param == "select_color":
            return self.select_color
        if param == "cursor_color":
            return self.cursor_color
        return super().cget(param)

    def _set_appearance_mode(self, mode_string):
        super()._set_appearance_mode(mode_string)
        self._textbox.config(
            insertbackground=self.cursor_color,
            selectbackground=self.select_color,
            selectforeground="#FFFFFF",
        )