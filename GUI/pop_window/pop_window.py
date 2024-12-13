from PyQt6.QtWidgets import QMessageBox
from GUI.style.style import CONST_POPUP_WINDOW

def pop_window(title, text):
    window = QMessageBox()
    window.setWindowTitle(title)
    window.setStyleSheet(CONST_POPUP_WINDOW)
    window.setText(text)
    window.exec()