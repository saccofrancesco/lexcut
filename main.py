# Importing the custom widget from the file
from layout_colorwidget import Color
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Create a vertical layout where to put new widgets
        layout: QVBoxLayout = QVBoxLayout()

        # Add widget to the layout
        layout.addWidget(Color("red"))

        # Creating a main widget where to apply the layout
        widget: QWidget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
