import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("D&D 5E Character Creator")
        self.setMinimumSize(900, 600)

        self.init_ui()

    def init_ui(self):

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # --- TOP BAR ---
        top_bar = QHBoxLayout()

        # Title
        title = QLabel("D&D 5E Character Creator")
        title.setFont(QFont("Times", 20, QFont.Bold))
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Settings button
        self.settings_button = QPushButton("⚙")
        self.settings_button.setFixedSize(40, 40)
        self.settings_button.clicked.connect(self.open_settings)

        # Add to top bar
        top_bar.addWidget(title)
        top_bar.addStretch()
        top_bar.addWidget(self.settings_button)

        # Add top bar to main layout
        main_layout.addLayout(top_bar)

        # --- MAIN CONTENT AREA ---
        self.content_area = QLabel("Main content will go here")
        self.content_area.setAlignment(Qt.AlignCenter)
        self.content_area.setStyleSheet("font-size: 18px;")

        main_layout.addWidget(self.content_area)

    def open_settings(self):
        print("Settings clicked!")
        # Later we’ll open a settings dialog here


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())