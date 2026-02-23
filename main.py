# Importing the custom widget from the file
from layout_colorwidget import Color
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # create an instance of the custom widget and pass it a color
        widget: Color = Color("red")

        self.setCentralWidget(widget)

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
