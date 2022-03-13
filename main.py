from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QCheckBox,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt, QSize
from generator import PasswordGenerator

class MainWindow(QMainWindow):
    checked = 2
    
    def __init__(self):
        super().__init__()
        self.generator = PasswordGenerator()

        self.setWindowTitle("Password generator")

        container = self.create_layout()
        self.setCentralWidget(container)
        self.setMinimumSize(QSize(400, 300))

    def create_layout(self):
        layout = QVBoxLayout()

        self.label = self.create_label()
        self.button = self.create_button()
        self.valid_checkbox = self.create_valid_words_checkbox()
        self.numbers_checkbox = self.create_use_numbers_checkbox()
        self.uppercase_checkbox = self.create_use_uppercase_checkbox()
        self.symbols_checkbox = self.create_use_symbols_checkbox()

        layout.addWidget(self.valid_checkbox)
        layout.addWidget(self.numbers_checkbox)
        layout.addWidget(self.uppercase_checkbox)
        layout.addWidget(self.symbols_checkbox)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.layout = layout

        container = QWidget()
        container.setLayout(layout)
        return container

    def create_label(self):
        widget = QLabel('Генерация пароля')
        widget.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return widget

    def create_button(self):
        widget = QPushButton('Сгенерировать')
        widget.clicked.connect(self.button_clicked)
        return widget

    def button_clicked(self):
        text = self.generator.generate()
        self.label.setText(text)
        QApplication.clipboard().setText(text)

    def create_valid_words_checkbox(self):
        widget = QCheckBox('Использовать настоящие слова')
        widget.stateChanged.connect(self.set_valid_words_checked)
        return widget
    
    def set_valid_words_checked(self, state):
        self.generator.set_use_valid_words(state == self.checked)

    def create_use_numbers_checkbox(self):
        widget = QCheckBox('Использовать цифры')
        widget.stateChanged.connect(self.set_use_numbers_checked)
        return widget
    
    def set_use_numbers_checked(self, state):
        self.generator.set_use_numbers(state == self.checked)
    
    def create_use_uppercase_checkbox(self):
        widget = QCheckBox('Использовать заглавные буквы')
        widget.stateChanged.connect(self.set_use_uppercase_checked)
        return widget
    
    def set_use_uppercase_checked(self, state):
        self.generator.set_use_uppercase(state == self.checked)

    def create_use_symbols_checkbox(self):
        widget = QCheckBox('Использовать спец. символы')
        widget.stateChanged.connect(self.set_use_symbols_checked)
        return widget
    
    def set_use_symbols_checked(self, state):
        self.generator.set_use_symbols(state == self.checked)
