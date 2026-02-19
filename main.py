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

        button: QPushButton = QPushButton("Press Me!")

        # Set the possibility for the button to be 'checked'
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        # Set the button as the central widget
        self.setCentralWidget(button)

    def the_button_was_toggled(self, is_checked: bool) -> None:
        
        # Chancge the value of the STATE based on the data passed to the 
        # SLOT by the button SIGNAL
        self.button_is_checked = is_checked

        print(self.button_is_checked)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
