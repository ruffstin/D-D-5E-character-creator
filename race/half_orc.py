# half_orc.py
from .race import Race
STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

class Half_Orc(Race):
    def __init__(self):
        super().__init__("Half-Orc", None)
        self.set_bonuses()

    def set_bonuses(self):
        # All half-orcs get +2 STR and +1 CON
        self.bonuses = {"STR": 2, "CON": 1}


        # we are not prompting the user yet so we will not set any other bonuses yet

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats
