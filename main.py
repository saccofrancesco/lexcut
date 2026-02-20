from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget: QSpinBox = QSpinBox()
        # Or: widget: QDoubleSpinBox = QDoubleSpinBox()

        # Can individually set min and max
        # widget.setMinimum(-10)
        # widget.setMaximum(3)

        # Use range for faster lower and upper bound settings
        widget.setRange(-10, 3)

        # Can define prefix and suffix (thoes doesn't change between input 
        # edits: they are fixed)
        widget.setPrefix("$")
        widget.setSuffix("c")

        # You can vary the amout increased or decreased by the arrow customizing
        # the step value
        widget.setSingleStep(3) # Or e.g. 0.5 for <class 'QDoubleSpinBox'>

        # Two SIGNAL method carrying with them the int version and the string version
        # of the widget current content (value)
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    # Both SLOTS methods reacts to changes SIGNAL; they differ by the chars included
    # Includes only the value of the number / counter
    def value_changed(self, value: int) -> None:
        print(value)
    
    # Includes all the string, included the prefix and suffix (if setted)
    def value_changed_str(self, value: str) -> None:
        print(value)

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
