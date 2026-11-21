# MDEdit Changelog
All Notabe chaanges to MDEdit are listed here.

---
### 16/11/26 &mdash; Baibhav Bhattacharya

- Initial project structure
- Dependency installation
- Version Control integration

---
### 17/11/26 &mdash; Baibhav Bhattacharya

- Added Asset Structure
- Added MVC-like structure
- Removed `CTkMenuBar` Dependency

---
### 20/11/26 &mdash; Baibhav Bhattacharya

- Added Custom `Menubar` and `MenubarItem` class
- Added Other widgets
- Added Appearance/Mode switch
- Added Code Editor

---
### 21/11/2026 &mdash; Baibhav Bhattacharya
**Migration to PySide6 in the migrate branch**  
The code available on the main branch is a broken Ui prototype for sake
of preservation, it will be merged with the main branch once it has the same amount of capability.

-  Dropped `pygments` and `CTkToolTip`
-  Dropped `tkinterweb` because it was unusable with `customtkinter` and `custom2kinter`
-  Dropped `customTkinter`
-  Dropped `CTkCodeBox` 
-  Dropped `CTkMessageBox`
-  Dropped `CTkListBox`
-  Dropped `Markdown`
-  Dropped `tklinenums`
-  Dropped `tkwebview2`
-  Dropped `Pillow` 

- Migrating to `PySide6`