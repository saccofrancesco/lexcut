# Importing necessaries libraries
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget: QCheckBox = QCheckBox("This is a checkbox")
        widget.setCheckState(Qt.CheckState.Checked)

        # Using this enables the box to have 3 states instead of two 
        # (this is why False 0, True 2 and in the middle 1)
        # widget.setTristate(True)

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    # SLOT fanction which react to the changing of state made by the checkbox
    def show_state(self, state) -> None:

        # Check if the state it's equal to the value of a Trye checked checkbox
        print(state == Qt.CheckState.Checked.value)

        print(state)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
