# Importing essentials
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass Qt Main Window to customize MY window
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Create a variable where we store the current STATE of a widget, 
        # the button in this case
        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button: QPushButton = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    # SLOT method to connect to with the RELEASED signal to then retrieve 
    # manually the state
    def the_button_was_released(self) -> None:
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
