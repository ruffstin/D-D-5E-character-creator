# human.py
from .race import Race
STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

class Human(Race): 
    def __init__(self):
        super().__init__("Human", None)
        self.set_bonuses()
    
    def set_bonuses(self):
         self.bonuses = {stat: 1 for stat in STAT_INDEX}  # +1 to all six stats

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats
