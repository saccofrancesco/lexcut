# Importing libraries responsible for style and overall widget and UI appearance
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget

# Sublcassing the QWidget class, to create a custom widget to use for layout tests
class Color(QWidget):
    def __init__(self, color: str) -> None:
        super().__init__()

        # Telling the widget to autofill the bg with the setted window color
        self.setAutoFillBackground(True)

        # Retrieving the widget's palette to modify and reapply it
        palette: QPalette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
