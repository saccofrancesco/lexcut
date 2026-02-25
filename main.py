from layout_colorwidget import Color
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QStackedLayout,
    QPushButton,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Defining the general layout structures of the page
        page_layout: QVBoxLayout = QVBoxLayout()
        button_layout: QHBoxLayout = QHBoxLayout()
        self.stacked_layout: QStackedLayout = QStackedLayout()

        # Adding the two pages' layouts part to the main page layout
        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stacked_layout)

        # Now creating the three buttons to control the stacked layout
        # and the corresponding colored widget, in order
        btn: QPushButton = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacked_layout.addWidget(Color("red"))

        btn: QPushButton = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacked_layout.addWidget(Color("green"))

        btn: QPushButton = QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacked_layout.addWidget(Color("yellow"))

        # Creating the widget where to apply the general page layout
        widget: QWidget = QWidget()
        widget.setLayout(page_layout)

        self.setCentralWidget(widget)

    # Creating the SLOT methods to trigger by the button pressing SIGNAL
    # to then change the order in the stack, accordingly to the button label
    def activate_tab_1(self) -> None:
        self.stacked_layout.setCurrentIndex(0)

    def activate_tab_2(self) -> None:
        self.stacked_layout.setCurrentIndex(1)

    def activate_tab_3(self) -> None:
        self.stacked_layout.setCurrentIndex(2)


app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
