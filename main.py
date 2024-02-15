from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit
import sys
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from buttons import Button, ButtonsGrid

if __name__ == "__main__":
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.v_layout.addLayout(buttonsGrid)

    # Ajusta Size
    window.adjustFixedSize()

    window.show()
    app.exec()
