# Importing essentials
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass Qt Main Window to customize MY window
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        button: QPushButton = QPushButton("Press Me!")

        # Set the possibility for the button to be 'checked'
        button.setCheckable(True)

        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        # Set the button as the central widget
        self.setCentralWidget(button)

    def the_button_was_clicked(self) -> None:
        print("Clicked!")

    def the_button_was_toggled(self, is_checked: bool) -> None:
        print("Checked?", is_checked)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
