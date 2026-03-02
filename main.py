from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QComboBox,
    QLabel,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Initializing a layout of type form
        layout: QFormLayout = QFormLayout()

        # Creating a dictionary where to store the widgets' data, with default
        # data
        self.data: dict[str, str | int] = {
            "name": "Johnina Smith",
            "age": 10,
            "favourite_icecream": "Vanilla",
        }

        # Creating widgets to then display in the form
        self.name: QLineEdit = QLineEdit()
        self.name.setText(self.data["name"])
        self.name.textChanged.connect(self.handle_name_changed)
        self.age: QSpinBox = QSpinBox()
        self.age.setValue(self.data["age"])
        self.age.valueChanged.connect(self.handle_age_changed)
        self.age.setRange(0, 200)
        self.icecream: QComboBox = QComboBox()
        self.icecream.setCurrentText(self.data["favourite_icecream"])
        self.icecream.addItems(["Vanilla", "Strawberry", "Chocolate"])
        self.icecream.currentTextChanged.connect(self.handle_icecream_changed)

        # Creating an empty label for showing the validation results
        self.error: QLabel = QLabel()

        # Adding the created widget to the layout
        layout.addRow("Name", self.name)  # or layout.addRow(QLabel("Name"), self.name)
        layout.addRow("Age", self.age)
        layout.addRow("Favourite Ice cream", self.icecream)
        layout.addRow(self.error)

        # Creating and placing the widget where the layout's applied
        widget: QWidget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # Method to process all the data in the widgets and validate it (deciding if it'good
    # and if not, what widgets are wrong)
    def validate(self) -> None:
        if self.data["age"] > 10 and self.data["favourite_icecream"] == "Chocolate":
            self.error.setText("People over 10 aren't allowed chocolate ice cream")
            return  # Used to return only one message at a time (even if more than one error)
        if self.data["age"] > 100:
            self.error.setText("Did you send a telegram?")
            return

        # In case nothing is triggered, set the text always to be blank
        self.error.setText("")

    # SLOT methods for handling the changes in the widgets and update the
    # values in th data component variable
    def handle_name_changed(self, name: str) -> None:
        self.data["name"] = name
        self.validate()

    def handle_age_changed(self, age: int) -> None:
        self.data["age"] = age
        self.validate()

    def handle_icecream_changed(self, icecream: str) -> None:
        self.data["favourite_icecream"] = icecream
        self.validate()


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
