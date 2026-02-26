from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QComboBox,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Initializing a layout of type form
        layout: QFormLayout = QFormLayout()

        # Creating widgets to then display in the form
        self.name: QLineEdit = QLineEdit()
        self.age: QSpinBox = QSpinBox()
        self.age.setRange(0, 200)
        self.icecream: QComboBox = QComboBox()
        self.icecream.addItems(["Vanilla", "Strawberry", "Chocolate"])

        # Adding the created widget to the layout
        layout.addRow("Name", self.name)  # or layout.addRow(QLabel("Name"), self.name)
        layout.addRow("Age", self.age)
        layout.addRow("Favourite Ice cream", self.icecream)

        # Creating and placing the widget where the layout's applied
        widget: QWidget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
