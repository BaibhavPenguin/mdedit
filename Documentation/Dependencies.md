# MDEdit Dependency List
Dependencies as of 16th November 2026.  
- `Python 3.14.0`
- `Pyinstaller`
- `Pillow` 
- `WeasyPrint`
- `customTkinter`
- `CTkCodeBox` &mdash; *Significantly Modified*
- `CTkMessageBox`
- `CTkListBox`
- `Markdown`
- `tklinenums`
- `tkinterweb`


---
## Notes

- InnoSetup is required to build the setup file.
- Project must be bundled using <kbd>--onedir</kbd> flag on pyinstaller.  
- Themes and MDEdit Themes will be built separately.
- `CTkMenuBar` removed from dependency tree, implemented a custom menubar widget.
- `pywinstyles` removed from dependency tree, it was unused anyways.

- Dropped `pygments` and `CTkToolTip`
