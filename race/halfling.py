# halfling.py
from .race import Race
STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

class Halfling(Race):
    def __init__(self, subrace: str = "Lightfoot Halfling"):
        super().__init__("Halfling", subrace)
        self.set_bonuses()
    
    def set_bonuses(self):
        # All elves get +2 DEX
        self.bonuses = {"DEX": 2}
        if self.subrace == "Lightfoot Halfling":
            self.bonuses["CHA"] = 1
        elif self.subrace == "Stout Halfling":
            self.bonuses["CON"] = 1
        # else: no extra subrace bonus

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats