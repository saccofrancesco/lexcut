# Importing PyQt6 essential widgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Creating the MainWindow class, subclassing the default one
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        self.button: QPushButton = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    # SLOT method to connect to the cliecked SIGNAL by the class' button
    def the_button_was_clicked(self) -> None:

        # When triggering the SIGNAL, uses the saved button instance in self
        # to access it, chancking it's label and disabling it, state-wise
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Also changing the window title, always using a class setter method
        self.setWindowTitle("A new window title")


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
