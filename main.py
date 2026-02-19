# Importing essentials
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass Qt Main Window to customize MY window
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Creating and connecting the button clicked SIGNAL to the class 
        # custom method SLOT
        button: QPushButton = QPushButton("Press Me!")
        button.clicked.connect(self.the_button_was_clicked)

        # Set the button as the central widget
        self.setCentralWidget(button)
    
    # Defining the class cutom SLOT method
    def the_button_was_clicked(self) -> None:
        print("Clicked!")


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
