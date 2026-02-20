from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget: QListWidget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        # Using the widget custom SIGNALS
        # Trigger when the item in the list (<class 'QListWidgetItem'>)
        widget.currentItemChanged.connect(self.item_changed)

        # Trigger when the text changed
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    # SLOT method that reacts when an item changes and get access to 
    # the QListWidgetItem object
    def item_changed(self, item: QListWidgetItem) -> None:
        print(item.text())

    # SLOT method that reacts when the text changes and get access to 
    # the changes
    def text_changed(self, text: str) -> None:
        print(text)

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
