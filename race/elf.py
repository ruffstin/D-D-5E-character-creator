# elf.py
from .race import Race
STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

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

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats
