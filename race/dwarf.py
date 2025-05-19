# dwarf.py
from .race import Race

class Dwarf(Race):
    def __init__(self, subrace: str = "Hill Dwarf"):
        super().__init__("Dwarf", subrace)
        self.set_bonuses()
    
    def set_bonuses(self):
        # All elves get +2 CON
        self.bonuses = {"CON": 2}
        if self.subrace == "Hill Dwarf":
            self.bonuses["WIS"] = 1
        elif self.subrace == "Mountain Dwarf":
            self.bonuses["STR"] = 2
        # else: no extra subrace bonus

