import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])

    # Set application icon
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "combine.ico")
    app.setWindowIcon(QIcon(icon_path))

    # Create and show the main window
    window = MainWindow()
    window.show()

    app.exec()
