# dragonborn.py
from .race import Race

class Dragonborn(Race):
    def __init__(self, subrace: str = "Gold Dragonborn"):
        super().__init__("Dragonborn", subrace)
        self.set_bonuses()

    def set_bonuses(self):
        # All dragonborn get +2 STR and +1 CHA
        self.bonuses = {"STR": 2, "CHA": 1}        
        # else: no additional bonuses
    