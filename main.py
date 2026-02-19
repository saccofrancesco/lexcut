# Importing the QPixMap for displaying an Image via it's pixxel array
from PyQt6.QtGui import QPixmap

# Importing then essential libraries
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget: QLabel = QLabel("Hello")

        # using the SLOT method to set a pixmap for the referenced label
        widget.setPixmap(QPixmap("otje.jpg"))

        self.setCentralWidget(widget)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
