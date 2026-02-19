import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QDialog,
    QScrollArea,
    QComboBox,
    QLineEdit
)

from PySide6.QtCore import (
    Qt, 
    QSettings, 
    QPropertyAnimation, 
    QTimer,
    QSize, 
    QUrl,
)
from PySide6.QtGui import (
    QFont, 
    QPixmap
)

from PySide6.QtMultimedia import QSoundEffect

import random



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("D&D 5E Character Creator")
        self.setMinimumSize(1100, 700)
        
        # ensure settings is kept in between launches
        self.settings_store = QSettings("DNDApp", "CharacterCreator")

        self.dark_mode = self.settings_store.value("dark_mode", True, type=bool)
        self.accent_color = self.settings_store.value("accent_color", "#3498db")

        # Character storage (temporary in-memory list)
        self.characters = []

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.main_page = self.build_main_page()
        self.settings_page = self.build_settings_page()
        self.character_page = self.build_character_page()

        self.stack.addWidget(self.main_page)
        self.stack.addWidget(self.settings_page)
        self.stack.addWidget(self.character_page)


        self.dice_sound = QSoundEffect()
        self.dice_sound.setSource(QUrl.fromLocalFile("assets/sounds/dice_roll.wav"))
        self.dice_sound.setVolume(0.7)  # range 0.0 to 1.0
        self.sound_enabled = self.settings_store.value("sound_enabled", True, type=bool)
        if not self.sound_enabled:
            self.sound_button.setText("Sound: OFF")

        self.roll_page = QWidget()
        self.stack.addWidget(self.roll_page)
        self.active_animations = []
        self.dice_base_geometries = []
        self.is_animating = False
        self.build_roll_page()


        self.apply_theme()

    # ==================================
    # MAIN PAGE
    # ==================================
    def build_main_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        top_bar = self.build_top_bar("D&D 5E Character Creator", show_home=True)
        layout.addLayout(top_bar)

        content = QHBoxLayout()

        image_placeholder = QLabel("Character Art\n(Placeholder)")
        image_placeholder.setAlignment(Qt.AlignCenter)
        image_placeholder.setMinimumWidth(550)
        image_placeholder.setStyleSheet("border: 2px dashed gray; font-size: 20px;")

        button_layout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)

        characters_button = QPushButton("Characters")
        characters_button.setMinimumSize(300, 140)
        characters_button.clicked.connect(self.go_to_character_page)

        roll_button = QPushButton("Roll")
        roll_button.setMinimumSize(300, 140)
        roll_button.clicked.connect(self.go_to_roll_page)

        button_layout.addWidget(characters_button)
        button_layout.addSpacing(50)
        button_layout.addWidget(roll_button)

        content.addWidget(image_placeholder)
        content.addLayout(button_layout)

        layout.addLayout(content)
        return page

    # ==================================
    # CHARACTER PAGE
    # ==================================
    def build_character_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        top_bar = self.build_top_bar("Character Selection", show_home=True)
        layout.addLayout(top_bar)

        content = QHBoxLayout()

        # LEFT SIDE
        left_layout = QVBoxLayout()

        self.filter_dropdown = QComboBox()
        self.filter_dropdown.addItems(["Name", "Class", "Race"])
        self.filter_dropdown.setFixedHeight(40)

        self.character_preview = QLabel("Let's make a Character!  →")
        self.character_preview.setAlignment(Qt.AlignCenter)
        self.character_preview.setMinimumSize(400, 400)
        self.character_preview.setStyleSheet(
            "border: 2px dashed gray; font-size: 20px;"
        )

        left_layout.addWidget(self.filter_dropdown)
        left_layout.addSpacing(20)
        left_layout.addWidget(self.character_preview)

        # RIGHT SIDE
        right_layout = QVBoxLayout()

        new_char_button = QPushButton("New Character")
        new_char_button.setFixedHeight(70)
        new_char_button.clicked.connect(self.create_dummy_character)

        right_layout.addWidget(new_char_button)
        right_layout.addSpacing(20)

        # Scroll Area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.character_list_widget = QWidget()
        self.character_list_layout = QVBoxLayout(self.character_list_widget)
        self.character_list_layout.setAlignment(Qt.AlignTop)

        self.scroll_area.setWidget(self.character_list_widget)

        right_layout.addWidget(self.scroll_area)

        content.addLayout(left_layout)
        content.addLayout(right_layout)

        layout.addLayout(content)
        return page

    # ==================================
    # SETTINGS PAGE 
    # ==================================
    def build_settings_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        top_bar = self.build_top_bar("Settings", show_home=True)
        layout.addLayout(top_bar)

        layout.addSpacing(40)

        dark_button = QPushButton("Toggle Dark Mode")
        dark_button.setFixedHeight(60)
        dark_button.clicked.connect(self.toggle_dark_mode)

        theme_button = QPushButton("Theme Color")
        theme_button.setFixedHeight(60)
        theme_button.clicked.connect(self.open_theme_dialog)

        layout.addWidget(dark_button)
        layout.addSpacing(20)
        layout.addWidget(theme_button)

        self.sound_button = QPushButton("Sound: ON")
        self.sound_button.setFixedHeight(60)
        self.sound_button.clicked.connect(self.toggle_sound)

        layout.addSpacing(20)
        layout.addWidget(self.sound_button)

        layout.addStretch()    

        return page

    # ==================================
    # TOP BAR BUILDER
    # ==================================
    def build_top_bar(self, title_text, show_home=False):
        top_bar = QHBoxLayout()

        if show_home:
            home_button = QPushButton("Home")
            home_button.setFixedSize(80, 45)
            home_button.clicked.connect(self.go_to_main)
            top_bar.addWidget(home_button)

        title = QLabel(title_text)
        title.setFont(QFont("Times", 24, QFont.Bold))

        settings_button = QPushButton("⚙")
        settings_button.setFixedSize(45, 45)
        settings_button.clicked.connect(self.go_to_settings)

        top_bar.addWidget(title)
        top_bar.addStretch()
        top_bar.addWidget(settings_button)

        return top_bar


    # ==================================
    # CHARACTER LIST LOGIC
    # ==================================
    def create_dummy_character(self):
        # Temporary example character
        name = f"Character {len(self.characters) + 1}"
        self.characters.append({
            "name": name,
            "class": "Fighter",
            "race": "Human"
        })
        self.refresh_character_list()

    def refresh_character_list(self):
        # Clear layout
        for i in reversed(range(self.character_list_layout.count())):
            widget = self.character_list_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        for char in self.characters:
            btn = QPushButton(f"{char['name']} - {char['class']} - {char['race']}")
            btn.setFixedHeight(50)
            btn.clicked.connect(lambda checked, c=char: self.show_character_preview(c))
            self.character_list_layout.addWidget(btn)

    def show_character_preview(self, character):
        self.character_preview.setText(
            f"{character['name']}\n\nClass: {character['class']}\nRace: {character['race']}"
        )

    # ==================================
    # Dice Roller Page Logic
    # ==================================
    def build_roll_page(self):
        layout = QVBoxLayout(self.roll_page)

        # Top Bar
        top_bar = self.build_top_bar("Time to Roll some Dice", show_home=True)
        layout.addLayout(top_bar)

        # Main Content
        content_layout = QHBoxLayout()

        # LEFT SIDE - Dice Inputs
        left_layout = QVBoxLayout()

        self.dice_sides = [4, 6, 8, 10, 12, 20]
        self.dice_inputs = []
        self.dice_icons = []

        for sides in self.dice_sides:
            row = QHBoxLayout()

            label = QLabel(f"d{sides}:")
            label.setFixedWidth(50)

            input_field = QLineEdit("0")
            input_field.setFixedWidth(60)

            image_label = QLabel()
            pixmap = QPixmap(f"assets/images/dice/d{sides}.png")
            image_label.setPixmap(pixmap)
            image_label.setScaledContents(True)
            image_label.setFixedSize(60, 60)

            self.dice_inputs.append(input_field)
            self.dice_icons.append(image_label)

            row.addWidget(label)
            row.addWidget(input_field)
            row.addWidget(image_label)

            left_layout.addLayout(row)

        content_layout.addLayout(left_layout)

        # RIGHT SIDE
        right_layout = QVBoxLayout()

        self.advantage_box = QComboBox()
        self.advantage_box.addItems([
            "Normal", 
            "Advantage (roll twice and take the higher number)", 
            "Disadvantage (roll twice and take the lowest number)"
            ])
        self.advantage_box.setFixedHeight(40)

        right_layout.addWidget(self.advantage_box)

        self.modifier_input = QLineEdit("")
        self.modifier_input.setPlaceholderText("Modifier (+/-)")
        self.modifier_input.setFixedHeight(40)

        right_layout.addWidget(self.modifier_input)

        self.roll_button = QPushButton("ROLL")
        self.roll_button.setFixedHeight(60)
        self.roll_button.clicked.connect(self.roll_dice)

        self.total_label = QLabel("Total:")
        self.total_label.setStyleSheet("font-size: 20px;")

        # Dice Tray Container
        dice_tray_container = QWidget()
        dice_tray_container.setFixedHeight(100)  # room for bounce
        dice_tray_layout = QHBoxLayout(dice_tray_container)
        dice_tray_layout.setSpacing(20)
        dice_tray_layout.setContentsMargins(20, 10, 20, 10)

        # Add 6 dice labels
        self.dice_tray_images = []
        self.dice_base_geometries = []

        for _ in range(6):
            label = QLabel()
            label.setFixedSize(70, 70)
            label.setScaledContents(True)
            label.setVisible(False)  # only show when dice > 0
            self.dice_tray_images.append(label)
            dice_tray_layout.addWidget(label)

        # Add container to layout
        right_layout.addWidget(dice_tray_container)

        self.history_area = QScrollArea()
        self.history_area.setWidgetResizable(True)

        self.history_widget = QWidget()
        self.history_layout = QVBoxLayout(self.history_widget)
        self.history_layout.setAlignment(Qt.AlignTop)

        self.history_area.setWidget(self.history_widget)

        right_layout.addWidget(self.history_area)

        self.reset_button = QPushButton("Reset")
        self.reset_button.setFixedHeight(50)
        self.reset_button.setEnabled(False)
        self.reset_button.setStyleSheet("color: transparent; background: transparent; border: none;")
        self.reset_button.clicked.connect(self.reset_dice)

        self.clear_history_button = QPushButton("Clear History")
        self.clear_history_button.setFixedHeight(50)
        self.clear_history_button.setEnabled(False)
        self.clear_history_button.setStyleSheet("color: transparent; background: transparent; border: none;")
        self.clear_history_button.clicked.connect(self.clear_history)

        right_layout.addWidget(self.roll_button)
        right_layout.addWidget(self.total_label)
        right_layout.addWidget(self.reset_button)
        right_layout.addWidget(self.clear_history_button)
        right_layout.addStretch()

        content_layout.addLayout(right_layout)
        layout.addLayout(content_layout)

        QTimer.singleShot(0, self.store_dice_positions)

    def store_dice_positions(self):
        self.dice_base_geometries = [
            label.geometry() for label in self.dice_tray_images
        ]

    def roll_dice(self):
        total = 0
        roll_summary = []
        dice_flags = []

        # Autofill empty fields
        for field in self.dice_inputs:
            if field.text().strip() == "":
                field.setText("0")

        total_dice = sum(int(field.text() or 0) for field in self.dice_inputs)

        if total_dice == 0:
            return # Nothing to roll

        if total_dice > 0 and self.sound_enabled:
            self.dice_sound.play()

        modifier_text = self.modifier_input.text().strip()
        modifier = int(modifier_text) if modifier_text else 0

        for index, input_field in enumerate(self.dice_inputs):
            count = int(input_field.text())
            sides = self.dice_sides[index]

            if count > 0:
                dice_flags.append(True)
                rolls = []

                for _ in range(count):

                    if self.advantage_box.currentText() == "Normal":
                        roll = random.randint(1, sides)

                    else:
                        roll1 = random.randint(1, sides)
                        roll2 = random.randint(1, sides)

                        if "Advantage" in self.advantage_box.currentText():
                            roll = max(roll1, roll2)
                        else:
                            roll = min(roll1, roll2)

                        rolls.append(f"{roll1},{roll2}→{roll}")
                        total += roll
                        continue  # skip normal append below

                    rolls.append(roll)
                    total += roll

                roll_summary.append(f"{count}d{sides}: {rolls}")

            else:
                dice_flags.append(False)


        total += modifier

        if total != 0:
            self.total_label.setText(f"Total: {total}")
            self.reset_button.setEnabled(True)
            self.reset_button.setStyleSheet("")
            self.animate_dice(dice_flags)
            self.add_to_history(roll_summary, modifier, total)


    def add_to_history(self, summary, modifier, total):
        entry_text = " | ".join(summary)

        if modifier != 0:
            entry_text += f" + {modifier}"

        entry_text += f" = {total}"

        label = QLabel(entry_text)
        label.setWordWrap(True)
        label.setStyleSheet("font-size: 14px;")

        self.history_layout.insertWidget(0, label)
        self.clear_history_button.setEnabled(True)
        self.clear_history_button.setStyleSheet("")

    def animate_dice(self, dice_flags):
        if self.is_animating:
            return

        self.is_animating = True
        self.active_animations = []

        last_animation = None

        for index, label in enumerate(self.dice_tray_images):

            if dice_flags[index]:

                sides = self.dice_sides[index]
                pixmap = QPixmap(f"assets/images/dice/d{sides}.png")
                label.setPixmap(pixmap)
                label.setVisible(True)

                grow = QPropertyAnimation(label, b"maximumSize")
                grow.setDuration(200)
                grow.setStartValue(label.size())
                grow.setEndValue(label.size() * 1.4)

                shrink = QPropertyAnimation(label, b"maximumSize")
                shrink.setDuration(200)
                shrink.setStartValue(label.size() * 1.4)
                shrink.setEndValue(QSize(70, 70))

                grow.finished.connect(shrink.start)

                self.active_animations.append(grow)
                self.active_animations.append(shrink)

                grow.start()
                
                last_animation = shrink

            else:
                label.setVisible(False)

        if last_animation:
            last_animation.finished.connect(self.animation_finished)
        else:
            self.is_animating = False

    def animation_finished(self):
        self.is_animating = False        

    def reset_dice(self):
        for input_field in self.dice_inputs:
            input_field.setText("0")

        self.modifier_input.clear()

        for image in self.dice_tray_images:
            image.setVisible(False) 

        self.total_label.setText("Total:")
        self.reset_button.setEnabled(False)
        self.reset_button.setStyleSheet("color: transparent; background: transparent; border: none;")

    def clear_history(self):
        for i in reversed(range(self.history_layout.count())):
            widget = self.history_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        #self.clear_history_button.setVisible(False)
        self.clear_history_button.setEnabled(False)
        self.clear_history_button.setStyleSheet("opacity: 0;")
        self.clear_history_button.setStyleSheet("color: transparent; background: transparent; border: none;")


    # ==================================
    # THEME SYSTEM
    # ==================================
    def apply_theme(self):
        background = "#1e1e1e" if self.dark_mode else "#f4f4f4"
        text = "#ffffff" if self.dark_mode else "#000000"

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {background};
                color: {text};
            }}

            QPushButton {{
                background-color: {self.accent_color};
                border-radius: 12px;
                padding: 12px;
                font-size: 18px;
                font-weight: bold;
            }}
        """)

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.settings_store.setValue("dark_mode", self.dark_mode)
        self.apply_theme()

    def toggle_sound(self):
        self.sound_enabled = not self.sound_enabled
        self.settings_store.setValue("sound_enabled", self.sound_enabled)

        if self.sound_enabled:
            self.sound_button.setText("Sound: ON")
        else:
            self.sound_button.setText("Sound: OFF")

    def open_theme_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Theme Color")
        layout = QVBoxLayout(dialog)

        colors = {
            "Red": "#e74c3c",
            "Orange": "#e67e22",
            "Yellow": "#f1c40f",
            "Green": "#2ecc71",
            "Blue": "#3498db",
            "Purple": "#9b59b6"
        }

        for name, code in colors.items():
            btn = QPushButton(name)
            btn.setStyleSheet(f"background-color: {code}; color: white;")
            btn.clicked.connect(lambda checked, c=code: self.set_accent(c, dialog))
            layout.addWidget(btn)

        dialog.exec()

    def set_accent(self, color, dialog):
        self.accent_color = color
        self.settings_store.setValue("accent_color", self.accent_color)
        self.apply_theme()
        dialog.accept()

    # ==================================
    # NAVIGATION
    # ==================================
    def go_to_settings(self):
        self.stack.setCurrentWidget(self.settings_page)

    def go_to_main(self):
        self.stack.setCurrentWidget(self.main_page)

    def go_to_character_page(self):
        self.stack.setCurrentWidget(self.character_page)

    def go_to_roll_page(self):
        self.stack.setCurrentWidget(self.roll_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
