from PySide6.QtWidgets import QPushButton

def create_button(text, action):
    button = QPushButton(text)
    button.clicked.connect(action)
    return button

def apply_styles(window):
    window.setStyleSheet("""
        QMainWindow {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        QLabel {
            font-size: 16px;
            margin: 10px;
            color: #333;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 14px;
            margin: 5px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:pressed {
            background-color: #388e3c;
        }
        /* Combine button specific styling */
        QPushButton#combine_button {
            background-color: #4A90E2; /* Blue */
        }
        QPushButton#combine_button:hover {
            background-color: #357ABD; /* Darker blue for hover */
        }
        QPushButton#combine_button:pressed {
            background-color: #2C6BA3; /* Even darker blue for press */
        }
    """)