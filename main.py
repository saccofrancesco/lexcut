from layout_colorwidget import Color
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Instanciating a layout of grid type
        layout: QGridLayout = QGridLayout()

        # Putting elements inside the grid layout,, suing row and columns indexes
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("purple"), 2, 1)

        # Creating the widget where to apply the layout
        widget: QWidget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
