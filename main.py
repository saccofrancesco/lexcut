# Importing libraries
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

# Storing random window titles to use with random.choice()
window_titles: list[str] = [
    "My App",
    "Still My App",
    "What on earth",
    "This is surprising",
    "Something went wrong",
]


# Subclassing the default main windo class for better cutomization
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Saving the reference to a counter for the number of clicks
        self.n_times_clicked: int = 0

        self.setWindowTitle("My App")

        self.button: QPushButton = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        # Connect the SIGNAL from the change of title of the window to a new SLOT
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    # SLOT method for using the button clicked evet to trigger a new random choice
    # for the app window title
    def the_button_was_clicked(self) -> None:
        print("Clicked.")

        # Choosing randomly a new title
        new_window_title: str = choice(window_titles)

        # Outputting that the changed has been applied and what is the new title
        print(f"Setting title: {new_window_title}")
        self.setWindowTitle(new_window_title)

    # SLOT method to check if the title is equal to something and then changing the
    # state of the referenced button with self based on the result of the check
    def the_window_title_changed(self, window_title: str) -> None:
        print(f"Window title changed: {window_title}")

        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
