# half_elf.py
from .race import Race
STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

class Half_Elf(Race):
    def __init__(self):
        super().__init__("Half-Elf", None)
        self.set_bonuses()

    def set_bonuses(self):
        # All half-elves get +2 CHA and +1 to two other stats
        self.bonuses = {"CHA": 2}

        # we are not prompting the user yet so we will not set any other bonuses yet

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats
