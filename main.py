from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        # Passing the orientation to the constructur overrides the
        # default vertical orientation
        widget: QSlider = QSlider(Qt.Orientation.Horizontal)

        # Same as QSpin
        widget.setRange(-10, 3)
        widget.setSingleStep(3)

        # Some different SIGNALS from the QSpin or QDoubleSpin
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    # SLOT methods to access slider value and position in time
    def value_changed(self, value: int) -> None:
        print(value)
    
    def slider_position(self, position: int) -> None:
        print("Position:", position)

    # SLOT methods reacting and accessing if the slider is either
    # pressed or released
    def slider_pressed(self) -> None:
        print("Pressed!")

    def slider_released(self) -> None:
        print("Released!")

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
