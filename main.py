from PyQt6.QtWidgets import QApplication, QPushButton

app: QApplication = QApplication([])

window: QPushButton = QPushButton("Push Me")
window.show()

app.exec()
