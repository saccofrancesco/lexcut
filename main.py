# Importing Qt essentials
from PyQt6.QtWidgets import QApplication, QWidget

# Creating ONLY ONE instance of the Application widget
app: QApplication = QApplication([])

# Create a Qt widget, which will create a window
window: QWidget = QWidget()
window.show() # IMPORTANT!!! Windows are ALWAYS hidden by deafault

# Start the event loop
app.exec()

# Will reach this section ONLY when the MAIN window is closed
