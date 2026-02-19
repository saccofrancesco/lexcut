# Importing sizing from Qt Core module
from PyQt6.QtCore import QSize

# Importing essentials
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass Qt Main Window to customize MY window
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        button: QPushButton = QPushButton("Press Me!")

        # Using the method, pass a QSize object with width and height in
        # order to set the size
        self.setFixedSize(QSize(400, 300))

        # Set the button as the central widget
        self.setCentralWidget(button)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
