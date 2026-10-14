from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QStackedWidget, QLabel,
    QLineEdit, QComboBox, QMessageBox
)
from PySide6.QtCore import Qt
from character import Character
from race import Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, HalfElf, HalfOrc, Tiefling
from background import Acolyte, Charlatan, Criminal, Entertainer, Folk_Hero, Guild_Artisan, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin
from char_class import Artificer, Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard
from stats_gui import StatGenerator
from languages import LANGUAGES  


class CharacterCreationWizard(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.character_data = {
            "name": "",
            "race": None,
            "subrace": None,
            "class": "",
           "subclass": "",
            "background": "",
            "stats": [],
            "race_skills": set(),
            "class_skills": set(),
            "background_skills": set(),
            "skills": [],
            "equipment": [],
            "alignment": ""
        }

        self.setWindowTitle("Character Creation")

        self.main_layout = QVBoxLayout(self)

        # ---- STACK ----
        self.stack = QStackedWidget()
        self.main_layout.addWidget(self.stack)


        # ---- STEPS ----
        self.stack.addWidget(self.name_step())
        self.stack.addWidget(self.race_step())
        self.stack.addWidget(self.class_step())
        self.stack.addWidget(self.background_step())
        self.stack.addWidget(self.stats_step())
        self.update_subrace_options(self.race_dropdown.currentText())
        

        # ---- NAVIGATION ----
        nav_layout = QHBoxLayout()

        self.back_button = QPushButton("Back")
        self.next_button = QPushButton("Next")

        self.back_button.clicked.connect(self.go_back)
        self.next_button.clicked.connect(self.go_next)

        nav_layout.addWidget(self.back_button)
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_button)

        self.main_layout.addLayout(nav_layout)

        self.update_buttons()

    # =====================================================
    # STEP 1 — NAME
    # =====================================================
    def name_step(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        layout.addWidget(QLabel("Enter Character Name:"))

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Type Name Here")
        layout.addWidget(self.name_input)
        self.name_input.setClearButtonEnabled(True)

        layout.addStretch()

        return page

    # =====================================================
    # STEP 2 — RACE
    # =====================================================
    def race_step(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        layout.addWidget(QLabel("Choose Race:"))

        self.race_dropdown = QComboBox()
        self.available_races = {
            "Dwarf": Dwarf,
            "Halfling": Halfling,
            "Elf": Elf,
            "Human": Human,
            "Dragonborn": Dragonborn,
            "Gnome": Gnome,
            "Half-Elf": HalfElf,
            "Half-Orc": HalfOrc,
            "Tiefling": Tiefling
        }
        self.race_dropdown.addItems(self.available_races.keys())
        layout.addWidget(self.race_dropdown)

        self.subrace_dropdown = QComboBox()
        self.subrace_dropdown.setVisible(False)
        layout.addWidget(self.subrace_dropdown)
        self.race_dropdown.currentTextChanged.connect(self.update_subrace_options)
        self.subrace_dropdown.currentTextChanged.connect(self.on_subrace_changed)

        self.dynamic_choice_widgets = {}
        self.dynamic_choice_layout = QVBoxLayout()
        layout.addLayout(self.dynamic_choice_layout)

        layout.addStretch()
        return page
    
    def update_subrace_options(self, race_name):
        self.subrace_dropdown.clear()

        race_class = self.available_races[race_name]
        subraces = getattr(race_class, "SUBRACES", {})

        if subraces:
            self.subrace_dropdown.addItems(subraces.keys())
            self.subrace_dropdown.setVisible(True)
        else:
            self.subrace_dropdown.setVisible(False)

        subrace = self.subrace_dropdown.currentText() if self.subrace_dropdown.isVisible() else None
        race_instance = race_class(subrace)

        self.character_data["race"] = race_instance
        self.character_data["subrace"] = subrace

        self.render_race_choices(race_instance)

    def on_subrace_changed(self, subrace_name):
        race_name = self.race_dropdown.currentText()
        race_class = self.available_races[race_name]

        race_instance = race_class(subrace_name)

        self.character_data["race"] = race_instance
        self.character_data["subrace"] = subrace_name

        self.render_race_choices(race_instance)

        self.update_stat_labels()

    def clear_dynamic_choices(self):
        while self.dynamic_choice_layout.count():
            item = self.dynamic_choice_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.dynamic_choice_widgets.clear()


    def render_race_choices(self, race_instance):
        self.clear_dynamic_choices()

        choice_defs = race_instance.get_choice_definitions()

        for key, info in choice_defs.items():
            # for language filter out known languages
            choice_type = info.get("type")
            choose_count = info.get("choose", 1)
            options = info.get("options", [])

            if choice_type == "language":
                known_languages = {lang.name for lang in race_instance.languages}
                options = [lang for lang in options if lang not in known_languages]

                if not options: # hide if nothing to choose
                    continue
            
            if choose_count == 1: 
                label = QLabel(f"Choose a {choice_type}:")
            else: 
                label = QLabel(f"Choose {choose_count} different {choice_type}s:")

            self.dynamic_choice_layout.addWidget(label)

            dropdowns = []

            for i in range(choose_count):
                combo = QComboBox()
                combo.addItems(options)
                self.dynamic_choice_layout.addWidget(combo)
                dropdowns.append(combo)

            # Prevent duplicate ability selection
            if choice_type in {"ability score", "skill"} and choose_count > 1:
                for d in dropdowns:
                    d.currentTextChanged.connect(
                    lambda _, dd=dropdowns, opts=options: self.update_duplicate_dropdowns(dd, opts)
                )
                
            self.dynamic_choice_widgets[key] = dropdowns

    def update_ability_dropdowns(self, dropdowns, options):
        selected = [d.currentText() for d in dropdowns]

        for i, dropdown in enumerate(dropdowns):
            current = dropdown.currentText()
            dropdown.blockSignals(True)
            dropdown.clear()

            available = [opt for opt in options if opt not in selected or opt == current]
            dropdown.addItems(available)
            dropdown.setCurrentText(current)

            dropdown.blockSignals(False)

    def update_duplicate_dropdowns(self, dropdowns, options):
        selected = [d.currentText() for d in dropdowns]
        for d in dropdowns:
            current = d.currentText()
            d.blockSignals(True)
            d.clear()
            available = [opt for opt in options if opt not in selected or opt == current]
            d.addItems(available)
            d.setCurrentText(current)
            d.blockSignals(False)

    def finalize_race_step(self):
        race = self.character_data["race"]
        race.apply_choices()

        # debugging prints
        #print("Choices made:", race.choices_made)
        #print("Choice skills:", race.choice_skills)

        self.character_data["race_skills"] = race.get_skill_proficiencies()

        total_skills = (
            self.character_data.get("race_skills", set())
            | self.character_data.get("class_skills", set())
            | self.character_data.get("background_skills", set())
        )

        self.character_data["skills"] = sorted(total_skills)


    # =====================================================
    # STEP 3 — CLASS
    # =====================================================
    def class_step(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        layout.addWidget(QLabel("Choose Class:"))

        self.class_dropdown = QComboBox()
        self.class_dropdown.addItems([
            "Fighter",
            "Wizard",
            "Rogue",
            "Cleric",
            "Druid"
        ])
        layout.addWidget(self.class_dropdown)

        layout.addStretch()
        return page

    # =====================================================
    # STEP 4 — BACKGROUND
    # =====================================================
    def background_step(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        layout.addWidget(QLabel("Choose Background:"))

        self.background_dropdown = QComboBox()
        self.background_dropdown.addItems([
            "Acolyte",
            "Soldier",
            "Criminal",
            "Sage"
        ])
        layout.addWidget(self.background_dropdown)

        layout.addStretch()
        return page
    
    # =====================================================
    # STEP 5 — STAT GENERATION
    # =====================================================
    def stats_step(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        layout.addWidget(QLabel("Ability Scores (Standard Array)"))

        # -----------------------------------
        # STANDARD ARRAY DISPLAY (OBJECT)
        # -----------------------------------
        self.standard_array = [15, 14, 13, 12, 10, 8]
        base_stats = self.standard_array.copy()
        race = self.character_data.get("race")
        if race:
            base_stats = race.apply_racial_bonuses(base_stats)

        self.array_labels = []

        array_layout = QHBoxLayout()
        for value in base_stats:
            label = QLabel(str(value))
            label.setStyleSheet("font-size: 18px; font-weight: bold;")
            label.setAlignment(Qt.AlignCenter)

            self.array_labels.append(label)
            array_layout.addWidget(label)

        layout.addLayout(array_layout)


        # -----------------------------------
        # STAT DISPLAY
        # -----------------------------------
        self.stat_labels = {}
        self.modifier_labels = {}

        stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

        for stat, value in zip(stat_names, base_stats):
            row = QHBoxLayout()

            name_label = QLabel(stat)

            value_label = QLabel(str(value))
            value_label.setStyleSheet("font-size: 16px; font-weight: bold;")

            modifier = self.calculate_modifier(value)
            modifier_label = QLabel(f"({modifier:+})")

            self.stat_labels[stat] = value_label    
            self.modifier_labels[stat] = modifier_label

            row.addWidget(name_label)
            row.addStretch()
            row.addWidget(value_label)
            row.addWidget(modifier_label)

            layout.addLayout(row)

        layout.addStretch()

        self.character_data["stats"] = base_stats.copy()

        return page
    
    # Helper method for determining a stats modifier 
    def calculate_modifier(self, score):
        return (score - 10) // 2

    
    # =====================================================
    # NAVIGATION
    # =====================================================
    def go_next(self):
        current = self.stack.currentIndex()

        if not self.validate_step(current):
            return

        if current < self.stack.count() - 1:
            self.stack.setCurrentIndex(current + 1)

            if self.stack.currentIndex() == 2:
                self.finalize_race_step() # before proceeding to class

            if self.stack.currentIndex() == 4: 
                self.update_stat_labels()

        else:
            self.finish_character()

        self.update_buttons()

    def go_back(self):
        current = self.stack.currentIndex()

        # If on first page → Cancel behavior
        if current == 0:
            self.cancel_creation()
            return

        # Otherwise behave normally
        self.stack.setCurrentIndex(current - 1)
        self.update_buttons()

    def update_buttons(self):
        current = self.stack.currentIndex()

          # ---- FIRST PAGE (NAME) ----
        if current == 0:
            self.back_button.setText("Cancel")
            self.back_button.setVisible(True)
        else:
            self.back_button.setText("Back")
            self.back_button.setVisible(True)

        # ---- LAST PAGE ----
        if current == self.stack.count() - 1:
            self.next_button.setText("Finish")
        else:
            self.next_button.setText("Next")
    
    
    # =====================================================
    # VALIDATION
    # =====================================================
    def validate_step(self, step_index):
        
        # ---------------------------
        # STEP 0 — NAME
        # ---------------------------
        if step_index == 0:
            name = self.name_input.text().strip()
            if not name:
                return False
            self.character_data["name"] = name

        # ---------------------------
        # STEP 1 — RACE
        # ---------------------------
        elif step_index == 1:
            race_name = self.race_dropdown.currentText()    
            race_class = self.available_races[race_name]

            subrace = None
            if self.subrace_dropdown.isVisible():
                subrace = self.subrace_dropdown.currentText()

            race_instance = race_class(subrace)

            for key, dropdowns in self.dynamic_choice_widgets.items():
                selections = [d.currentText() for d in dropdowns]
                success = race_instance.set_choice(key, selections)
                if not success:
                    QMessageBox.warning(self, "Invalid Selection",
                            "Please complete all required race choices.")
                    return False

            race_instance.apply_choices()

            self.character_data["race"] = race_instance
            self.character_data["subrace"] = subrace

        # ---------------------------
        # STEP 2 — CLASS
        # ---------------------------    
        elif step_index == 2:
            self.character_data["class"] = self.class_dropdown.currentText()

        # ---------------------------
        # STEP 3 — BACKGROUND
        # ---------------------------
        elif step_index == 3:
            self.character_data["background"] = self.background_dropdown.currentText()


        # ---------------------------
        # STEP 4 — STATS
        # ---------------------------
        elif step_index == 4:
            if not self.character_data["stats"]:
                self.character_data["stats"] = self.standard_array.copy()

            race = self.character_data["race"]

            base_stats = self.standard_array.copy()  # important
            final_stats = race.apply_racial_bonuses(base_stats)

            self.character_data["stats"] = final_stats

            self.update_stat_labels()
        return True

    # =====================================================
    # FINISH
    # =====================================================
    def finish_character(self):
        print("Character Created:", self.character_data)

        # TEMPORARY — you will replace this with real Character object
        self.main_window.characters.append(self.character_data)
        self.main_window.refresh_character_list()
        self.main_window.go_to_character_page()

        self.reset_wizard()

    def reset_wizard(self):
        self.character_data = {
            "name": "",
            "race": "",
            "subrace": "",
            "class": "",
            "subclass": "",
            "background": "",
            "stats": [],
            "skills": [],
            "equipment": [],
            "alignment": ""
        }

        self.name_input.clear()
        self.race_dropdown.setCurrentIndex(0)
        self.class_dropdown.setCurrentIndex(0)
        self.background_dropdown.setCurrentIndex(0)

        self.stack.setCurrentIndex(0)
        self.update_buttons()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.go_next()
        else:
            super().keyPressEvent(event)

    def cancel_creation(self):
        reply = QMessageBox.question(
            self,
            "Cancel Character Creation",
            "Are you sure you want to cancel?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Reset everything
            self.reset_wizard()

            # Return to main window character list page
            self.main_window.go_to_character_page()

    def update_stat_labels(self):
        """
        Updates the stat labels on the stats page based on the current base stats
        and the currently selected race/subrace bonuses.
        """
        base_stats = self.standard_array.copy()
        race = self.character_data.get("race")
        if race:
            base_stats = race.apply_racial_bonuses(base_stats)

        # Update array labels (top display)
        # in the future depending on method for stat selection

        # Update row labels and modifiers
        stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for stat, value in zip(stat_names, base_stats):
            self.stat_labels[stat].setText(str(value))
            self.modifier_labels[stat].setText(f"({self.calculate_modifier(value):+})")

        # Also update character_data
        self.character_data["stats"] = base_stats.copy()

