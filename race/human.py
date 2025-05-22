# human.py
from .race import Race

class Human(Race): 
    def __init__(self):
        super().__init__("Human", None)
        self.set_bonuses()
        self.languages = ["Common", "Any one language of your choice"]
    
    def set_bonuses(self):
         self.bonuses = {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}  # +1 to all six stats

