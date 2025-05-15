# dwarf.py
from .race import Race
STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

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

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats
