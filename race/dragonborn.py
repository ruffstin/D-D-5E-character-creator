# dragonborn.py
from .race import Race
STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

class Dragonborn(Race):
    def __init__(self, subrace: str = "Gold Dragonborn"):
        super().__init__("Dragonborn", subrace)
        self.set_bonuses()

    def set_bonuses(self):
        # All dragonborn get +2 STR and +1 CHA
        self.bonuses = {"STR": 2, "CHA": 1}        
        # else: no additional bonuses
    
    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats