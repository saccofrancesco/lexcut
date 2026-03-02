from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Creating a placeholder label to use for exploring the toolbar properties and
        # capabilities
        label: QLabel = QLabel("Hello")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.setCentralWidget(label)

        # Instanciating the toolbar
        toolbar: QToolBar = QToolBar("My main toolbar")

        # Optional: to prevent this toolbar being removed.
        toolbar.toggleViewAction().setEnabled(False)
        self.addToolBar(toolbar)

    def onMyToolBarButtonClick(self, checked: bool) -> None:
        print("Click", checked)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
