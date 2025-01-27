import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QFileDialog, QWidget
from combine import combine_files
from ui_components import create_button, apply_styles

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Combiner")

        # Set window icon
        icon_path = os.path.join(os.path.dirname(__file__), "assets", "combine.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.input_folder = None
        self.output_file = None

        self.resize(300, 200)  # Set width to 600px and height to 400px

        # Set up UI layout and components
        self.setup_ui()

        # Apply styling
        apply_styles(self)

    def setup_ui(self):
        layout = QVBoxLayout()

        # Labels for displaying the input folder and output file
        self.input_label = QLabel("<font color='black'>Input Folder: </font><font color='red'>Not selected</font>")
        self.output_label = QLabel("<font color='black'>Output Folder: </font><font color='red'>Not selected</font>")

        # Buttons to select input folder, output file, and combine files
        input_button = create_button("Select input folder", self.select_input_folder)
        output_button = create_button("Select output file", self.select_output_file)
        
        # Create combine button and set its object name to apply custom style
        combine_button = create_button("Combine files", self.combine_files)
        combine_button.setObjectName("combine_button")  # Set object name for styling

        layout.addWidget(self.input_label)
        layout.addWidget(input_button)
        layout.addWidget(self.output_label)
        layout.addWidget(output_button)
        layout.addWidget(combine_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_input_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Input Folder")
        if folder:
            self.input_folder = folder
            self.input_label.setText(f"<font color='black'>Input Folder: </font><font color='green'>{folder}</font>")
        else:
            self.input_label.setText("<font color='black'>Input Folder: </font><font color='red'>Not selected</font>")

    def select_output_file(self):
        file, _ = QFileDialog.getSaveFileName(
            self, "Select Output File", filter="Text Files (*.txt);;All Files (*)"
        )
        if file:
            self.output_file = file
            self.output_label.setText(f"<font color='black'>Output Folder: </font><font color='green'>{file}</font>")
        else:
            self.output_label.setText("<font color='black'>Output Folder: </font><font color='red'>Not selected</font>")

    def combine_files(self):
        try:
            if not self.input_folder or not self.output_file:
                raise ValueError("Input folder or output file not set.")

            # Combine files and show success
            combine_files(self.input_folder, self.output_file)
            self.output_label.setText(f"Success: Combined files into {self.output_file}")
        except Exception as e:
            self.output_label.setText(f"Error: {e}")
