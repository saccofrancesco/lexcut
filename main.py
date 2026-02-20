from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget: QLineEdit = QLineEdit()

        # Customize the properties of the line editor
        widget.setMaxLength(10) # 10 Characters

        # Text displayed bevore the user enters something
        widget.setPlaceholderText("Enter your text")

        # It can also be setted not editable
        # widget.setReadOnly(True)

        # It can be possible to sanitize the input using a mask
        # widget.setMask("000.000.000.000;_") # Allow input of 3 digits separated by '.' (IP)

        # Connect differente SIGNALS methods used by the QLineEdit widget 
        # to notify some changes
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    # SLOT method triggered when the widget is pressed
    def return_pressed(self) -> None:
        print("Return pressed!")

        # Access the central widget setted in the constructor, using the reference 
        # to the main window
        self.centralWidget().setText("BOOM!")
    
    # SLOT method triggered when a selection of text changes
    def selection_changed(self) -> None:
        print("Selection changed!")

        # Access the selected text passed by the SIGNAL using the central widget
        print(self.centralWidget().selectedText())

    # SLOT method triggered by the changed of the text from -> to (only if 100% different)
    def text_changed(self, text: str) -> None:
        print("Text changed...")
        print(text) # The full text now in the widget
    
    # SLOT method triggered by the EDITS of the text from -> to (even by a single letter)
    def text_edited(self, edit: str) -> None:
        print("Text edited...")
        print(edit)

app: QApplication = QApplication([])

window: MainWindow = MainWindow()
window.show()

app.exec()
