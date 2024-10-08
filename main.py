import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt
import os

class FileUploadWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Underwriting Automator')
        self.setGeometry(300, 200, 500, 400)

        # Apply background image using a local file path or a valid URL
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('Re_logo.png');  /* Local file */
                background-repeat: no-repeat;
                background-position: top;
            }
        """)

        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # Labels and customized upload buttons for 4 PDF files
        self.file_paths = ["", "", "", ""]

        self.upload_labels = [
            "Upload rating_guide",
            "Upload financial statement 1",
            "Upload financial statement 2",
            "Upload proposal form"
        ]

        for i in range(4):
            label = QLabel(f"No file {i+1} selected", self)
            label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label)

            upload_btn = QPushButton(self.upload_labels[i], self)  # Custom label for each button
            upload_btn.clicked.connect(lambda _, index=i: self.upload_file(index))
            self.layout.addWidget(upload_btn)

            setattr(self, f'file_label_{i}', label)

        # Process button
        self.process_btn = QPushButton('Generate quotation', self)
        self.process_btn.clicked.connect(self.process_files)
        self.process_btn.setEnabled(False)  # Disable until all files are uploaded
        self.layout.addWidget(self.process_btn)

        # Download button
        self.download_btn = QPushButton('Download Report', self)
        self.download_btn.clicked.connect(self.download_report)
        self.download_btn.setEnabled(False)  # Disable until a report is generated
        self.layout.addWidget(self.download_btn)

        self.report_generated = False

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileUploadWindow()
    window.show()
    sys.exit(app.exec_())
