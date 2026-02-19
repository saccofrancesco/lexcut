# Importing common Qt widgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass the QMainWindow  to customize it's aspect
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Set the title on the subclassed MainWindow
        self.setWindowTitle("My App")

        button: QPushButton = QPushButton("Press Me!")

        # Set the central widget of the window instance
        self.setCentralWidget(button)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
