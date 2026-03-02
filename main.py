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

        # Creating a dictionary where to store the widgets' data
        self.data: dict[str, str | int] = dict()

        # Creating widgets to then display in the form
        self.name: QLineEdit = QLineEdit()
        self.name.textChanged.connect(self.handle_name_changed)
        self.age: QSpinBox = QSpinBox()
        self.age.valueChanged.connect(self.handle_age_changed)
        self.age.setRange(0, 200)
        self.icecream: QComboBox = QComboBox()
        self.icecream.addItems(["Vanilla", "Strawberry", "Chocolate"])
        self.icecream.currentTextChanged.connect(self.handle_icecream_changed)

        # Adding the created widget to the layout
        layout.addRow("Name", self.name)  # or layout.addRow(QLabel("Name"), self.name)
        layout.addRow("Age", self.age)
        layout.addRow("Favourite Ice cream", self.icecream)

        # Creating and placing the widget where the layout's applied
        widget: QWidget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # SLOT methods for handling the changes in the widgets and update the
    # values in th data component variable
    def handle_name_changed(self, name: str) -> None:
        self.data["name"] = name
        print(self.data)

    def handle_age_changed(self, age: int) -> None:
        self.data["age"] = age
        print(self.data)

    def handle_icecream_changed(self, icecream: str) -> None:
        self.data["favourite_icecream"] = icecream
        print(self.data)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
