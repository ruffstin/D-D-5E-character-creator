# tiefling.py
from .race import Race

class Tiefling(Race):
    def __init__(self):
        super().__init__("Tiefling", None)
        self.set_bonuses()
    
    def set_bonuses(self):
        # All tieflings get +2 CHA and +1 to INT
        self.bonuses = {"CHA": 2, "INT": 1}

