# Importing the custom widget from the file
from layout_colorwidget import Color
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Create a vertical layout where to put new widgets
        layout: QVBoxLayout = QVBoxLayout()

        # Add widgets to visualize the layout structure
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))

        # Creating a main widget where to apply the layout
        widget: QWidget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
