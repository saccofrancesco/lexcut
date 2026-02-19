# Importing the OS library to work with relative paths and files
import os

# Importing then necessaries libraries
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

# Computing the base directory where the script it's at
basedir: str = os.path.dirname(__file__)
print("Current working directory:", os.getcwd())
print("Paths are relative to:", basedir)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget: QLabel = QLabel("Hello")

        # Joins the based dir calculated safely, and then adding the path realtive to
        # the computed path
        widget.setPixmap(QPixmap(os.path.join(basedir, "otje.jpg")))

        # Activate the scaling to ALWAYS fit the window size 
        # (aspect ratio when enlarging not maintained)
        widget.setScaledContents(True)

        self.setCentralWidget(widget)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
