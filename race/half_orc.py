# half_orc.py
from .race import Race

class HalfOrc(Race):
    def __init__(self):
        super().__init__("Half-Orc", None)
        self.set_bonuses()

    def set_bonuses(self):
        # All half-orcs get +2 STR and +1 CON
        self.bonuses = {"STR": 2, "CON": 1}

