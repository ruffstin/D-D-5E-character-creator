# elf.py
from .race import Race

class Elf(Race):
    def __init__(self, subrace: str = "High Elf"):
        super().__init__("Elf", subrace)
        self.set_bonuses()
    
    def set_bonuses(self):
        # All elves get +2 DEX
        self.bonuses = {"DEX": 2}
        if self.subrace == "High Elf":
            self.bonuses["INT"] = 1
        elif self.subrace == "Wood Elf":
            self.bonuses["WIS"] = 1
        elif self.subrace == "Dark Elf":
            self.bonuses["CHA"] = 1
        # else: no additional bonuses
