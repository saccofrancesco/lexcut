from layout_colorwidget import Color
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Instanciating a stack type layout
        layout: QStackedLayout = QStackedLayout()

        # Adding several widget to the stack (one by one)
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        # Option to change the current index at which the stack displays a
        # widget
        layout.setCurrentIndex(3) # In this case: yellow, the last one added

        # Creating the wrapper widget and applying the layout to it
        widget: QWidget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
