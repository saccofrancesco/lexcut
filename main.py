from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget: QComboBox = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # Changing what it's conceded in the widget
        # Editable list
        widget.setEditable(True)

        # Max number of option included the addition made by the edits
        widget.setMaxCount(10)

        # Choose and modify the way the elements are inserted in the widget's
        # internal list
        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, index) -> None:
        print(index)

    def text_changed(self, text: str) -> None:
        print(text)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
