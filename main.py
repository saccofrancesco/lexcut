# Importing libraries (new QLineEdit, QLabel, QBoxLayout)
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Creating the two new widgets
        self.label: QLabel = QLabel()
        self.input: QLineEdit = QLineEdit()

        # Connecting th SIGNAL method of the text changes of the QLineEdit,
        # to the SLOT method of the QLabel, which receives the text's changes
        # and update the text with setText on the connected label
        self.input.textChanged.connect(self.label.setText)

        # Created the widget first, then composing the layout of them and then,
        # apply the layout to the final widget so the widgets are finally
        # visible
        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container: QWidget = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
