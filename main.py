from layout_colorwidget import Color
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Now implementing the tabwidget to reduce the code by 70% for managing tabs
        # compared to using the stacked layout
        tabs: QTabWidget = QTabWidget()

        # Customize the position using the cardinal points and if it can be moved
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        # Change the tab mode adapting it to a tab document type insted of a bubble
        # tabs.setDocumentMode(True)

        # Adding for each color in the list, the corresponding colored widget add
        # the desired tab
        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color.capitalize())

        self.setCentralWidget(tabs)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
