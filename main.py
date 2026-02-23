# Importing the custom widget from the file
from layout_colorwidget import Color
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Creting different layouts to nest
        layout1: QHBoxLayout = QHBoxLayout()
        layout2: QVBoxLayout = QVBoxLayout()
        layout3: QVBoxLayout = QVBoxLayout()

        # Customize the different type of spaces for containers / widgets in general
        # Remove all the margins between the container and the screen
        layout1.setContentsMargins(0, 0, 0, 0)
        
        # Set the spacing between the elements inside the layout
        layout1.setSpacing(20)

        # Adding some placeholder widgets to the layout to see the final result
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))

        # Nesting one layout into another (the layout respsct all the rules setted in its
        # parent as if it was one entire object itself)
        layout1.addLayout(layout2)

        # Adding widget also to the master layout
        layout1.addWidget(Color("green"))

        # Adding elements also to the last created layout to complete the visualization
        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))

        # Nesting another layout in the master horizontal widget
        layout1.addLayout(layout3)

        # Applying the layout to a widget to display it in the main window, placing it in
        # the center
        widget: QWidget = QWidget()
        widget.setLayout(layout1)

        self.setCentralWidget(widget)
        
        self.setCentralWidget(widget)

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
