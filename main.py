import sys
import time
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel,
    QFileDialog, QMessageBox, QSplashScreen, QSpacerItem, QSizePolicy, QProgressBar
)
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QPixmap, QPalette, QColor
import os


class FileUploadWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Automated Underwriter')
        self.setGeometry(300, 200, 800, 600)  # Increased size for better layout

        # Set light background color using stylesheet
        self.setStyleSheet("background-color: #B0E0E6;")

        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)

        # Top section for background image
        self.image_label = QLabel(self)

        # Get the script's directory and construct the full path to the image
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, 'Re_logo.png')

        logo_pixmap = QPixmap(image_path)
        if logo_pixmap.isNull():
            print(f"Error: '{image_path}' not found or is invalid.")
        self.image_label.setPixmap(logo_pixmap.scaledToWidth(200, Qt.SmoothTransformation))  # Adjust logo size
        self.image_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.image_label)  # Add image at the top

        # Add a vertical spacer to push the upload section down to the last 40%
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_layout.addItem(spacer)

        # Bottom section for file uploads and buttons (occupying the last 40% of the window)
        self.upload_widget = QWidget(self)
        self.upload_layout = QVBoxLayout(self.upload_widget)
        self.upload_layout.setContentsMargins(50, 20, 50, 20)
        self.upload_layout.setSpacing(15)

        # Labels and customized upload buttons for 4 PDF files
        self.file_paths = ["", "", "", ""]
        self.upload_labels = [
            "Upload Rating Guide",
            "Upload Financial Statement 1",
            "Upload Financial Statement 2",
            "Upload Proposal Form"
        ]

        self.upload_buttons = []
        self.upload_labels_widgets = []

        for i in range(4):
            label = QLabel("No file selected", self)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("color: #333;")  # Dark text for readability
            self.upload_layout.addWidget(label)

            # Customizing button size to be 40% of window width
            upload_btn = QPushButton(self.upload_labels[i], self)
            upload_btn.setFixedWidth(200)  # Fixed width for consistency
            upload_btn.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px;
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """)
            upload_btn.clicked.connect(lambda _, index=i: self.upload_file(index))
            self.upload_layout.addWidget(upload_btn, alignment=Qt.AlignCenter)

            # Store references for later use
            self.upload_buttons.append(upload_btn)
            self.upload_labels_widgets.append(label)
            setattr(self, f'file_label_{i}', label)

        # Process button
        self.process_btn = QPushButton('Generate Quotation', self)
        self.process_btn.setFixedWidth(200)
        self.process_btn.setStyleSheet("""
            QPushButton {
                background-color: #008CBA;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #007bb5;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        """)
        self.process_btn.clicked.connect(self.process_files)
        self.process_btn.setEnabled(False)  # Disable until all files are uploaded
        self.upload_layout.addWidget(self.process_btn, alignment=Qt.AlignCenter)

        # Download button
        self.download_btn = QPushButton('Download Report', self)
        self.download_btn.setFixedWidth(200)
        self.download_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        """)
        self.download_btn.clicked.connect(self.download_report)
        self.download_btn.setEnabled(False)  # Disable until a report is generated
        self.upload_layout.addWidget(self.download_btn, alignment=Qt.AlignCenter)

        self.report_generated = False

        # Add the upload section below the image
        self.main_layout.addWidget(self.upload_widget)

    def upload_file(self, index):
        # Open file dialog to select a file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, f"Select {self.upload_labels[index]}", "",
            "PDF Files (*.pdf);;All Files (*)", options=options
        )
        if file_name:
            self.file_paths[index] = file_name
            file_label = getattr(self, f'file_label_{index}')
            file_label.setText(f"Selected: {os.path.basename(file_name)}")

            # Enable process button only if all 4 files are selected
            if all(self.file_paths):
                self.process_btn.setEnabled(True)

    def process_files(self):
        if not all(self.file_paths):
            QMessageBox.warning(self, "Error", "Please upload all 4 documents!")
            return

        # Display a message box to show the uploaded files
        QMessageBox.information(
            self, "Processing",
            f"Processing files...\n"
            f"Files: {', '.join([os.path.basename(path) for path in self.file_paths])}"
        )

        # After processing, enable the download button
        self.report_generated = True
        self.download_btn.setEnabled(True)

    def download_report(self):
        if not self.report_generated:
            QMessageBox.warning(self, "Error", "No report generated yet!")
            return

        # Open save file dialog to download the report
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Report", "",
            "PDF Files (*.pdf);;All Files (*)", options=options
        )
        if file_name:
            # Simulate saving the report (replace with actual report saving logic)
            QMessageBox.information(self, "Download", f"Report saved at {file_name}")


def check_internet_connection():
    try:
        requests.get('https://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False


class SplashScreen(QSplashScreen):
    def __init__(self, pixmap, parent=None):
        super().__init__(pixmap)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, pixmap.height() - 30, pixmap.width() - 20, 20)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #000;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #3add36;
                width: 20px;
            }
        """)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and display the splash screen
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, 'Re_logo.png')

    splash_pix = QPixmap(image_path)
    if splash_pix.isNull():
        print(f"Error: '{image_path}' not found or is invalid. Using default pixmap.")
        splash_pix = QPixmap(600, 300)
        splash_pix.fill(QColor('white'))  # Fill with white if image not found

    splash = SplashScreen(splash_pix.scaled(600, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    screen_geometry = app.primaryScreen().availableGeometry()
    splash_width = screen_geometry.width() // 2
    splash_height = screen_geometry.height() // 2
    splash.setFixedSize(splash_width, splash_height)
    splash.show()

    # Simulate loading and updating the progress bar
    for i in range(1, 101):
        time.sleep(0.03)  # Simulate loading process
        splash.progress_bar.setValue(i)
        app.processEvents()

    # Check for internet connection after splash screen
    has_internet = check_internet_connection()
    if not has_internet:
        QMessageBox.warning(None, "No Internet", "No internet connection detected.")

    # Launch the main application window
    window = FileUploadWindow()
    window.show()
    splash.finish(window)

    sys.exit(app.exec())

