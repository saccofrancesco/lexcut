# Importing libraries
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget: QLabel = QLabel("Hello")

        # Using the label methods to customize it's
        # Extracting and modifying the font
        font = widget.font()
        font.setPointSize(30)

        # Appliying the font to the QLable widget
        widget.setFont(font)

        # Customizing the positioning of the QLable using Qt constants attributes
        widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(widget)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
