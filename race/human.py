# human.py
from .race import Race
from languages import LANGUAGES

class Human(Race): 

    SUBRACES = {}

    def __init__(self, subrace: str = None):
        super().__init__("Human", subrace)

         # +1 to all six stats
        self.bonuses = {
            "STR": 1, 
            "DEX": 1, 
            "CON": 1, 
            "INT": 1, 
            "WIS": 1, 
            "CHA": 1
            } 

        # -----------------------------
        # Languages
        # -----------------------------
        self.add_language("Common")

        self.choice_options["language"] = {
            "type": "language",
            "options": list(LANGUAGES.keys()),
            "choose": 1
        }

