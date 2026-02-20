from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        self.lwidget: QListWidget = QListWidget()
        self.lwidget.addItems(["One", "Two", "Three"])

        # Using the widget custom SIGNALS
        # Trigger when the item in the list (<class 'QListWidgetItem'>)
        self.lwidget.currentItemChanged.connect(self.item_changed)

        # Configuring the selection mode by using various Qt Flags
        self.lwidget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)

        # Trigger when the text changed
        self.lwidget.currentTextChanged.connect(self.text_changed)

        # Based on the type of selection, we can connect a SIGNAL to trigger when the
        # selection change (e. g. changing one item deselecting it it's a valid trigger)
        self.lwidget.selectionModel().selectionChanged.connect(self.selection_changed)

        self.setCentralWidget(self.lwidget)

    # SLOT method that reacts when an item changes and get access to 
    # the QListWidgetItem object
    def item_changed(self, item: QListWidgetItem) -> None:
        print(item.text())

    # SLOT method that reacts when the text changes and get access to 
    # the changes
    def text_changed(self, text: str) -> None:
        print(text)

    # SLOT method to print the Items selected, when the number of item seleceted changes
    def selection_changed(self) -> None:

        # Gets the currently selected items via the widget class reference
        print("Selected items:", self.lwidget.selectedItems())

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
