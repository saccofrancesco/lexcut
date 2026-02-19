# Importing base libraries
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget: QComboBox = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    # SLOT mathod which reacts at the option change SIGNAL by the combo-box
    def index_changed(self, index: int) -> None:
        print(index)

    # SLOT method which instead connect to the other type fo SIGNAL by the combo-box
    def text_changed(self, text: str) -> None:
        print(text)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
