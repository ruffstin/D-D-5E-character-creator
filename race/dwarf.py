# dwarf.py
from .race import Race

class Dwarf(Race):
    SUBRACES = {
        "Hill Dwarf": "",
        "Mountain Dwarf": ""
    }

    def __init__(self, subrace: str = "Hill Dwarf"):
        super().__init__("Dwarf", subrace)
        
        self.speed = 25

        # -----------------------------
        # Languages
        # -----------------------------
        self.add_language("Common")
        self.add_language("Dwarvish")

        self.features = {
            "Darkvision": "",
            "Dwarven Resilience": "",
            "Dwarven Combat Training": "",
            "Stonecunning": "",
            "Tool Proficiency": ""
        }

        self.other_proficiencies = {
            "Battleaxe", "Handaxe", "Light hammer", "Warhammer"
        }
        
        self.choice_options["tool_proficiency"] = {
            "type": "tool",
            "options": [
            "Smith's Tools",
            "Brewer's Supplies",
            "Mason's Tools"
            ],
            "choose": 1
        }

        # -----------------------------
        # Apply Subrace
        # -----------------------------
        self.set_bonuses()

    def set_bonuses(self):
        #  Base dwarf bonus: All dwarves get +2 CON
        self.bonuses = {"CON": 2}

        if self.subrace == "Hill Dwarf":
            self.bonuses["WIS"] = 1
            self.features["Dwarven Toughness"] = "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
            
        elif self.subrace == "Mountain Dwarf":
            self.bonuses["STR"] = 2
            self.features["Dwarven Armor Training"] = ""
            self.other_proficiencies.update({"Light armor", "Medium armor"})   

        # else: no extra subrace bonus

