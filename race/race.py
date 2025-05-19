# parent - race.py
# A race may have a subrace, and will provide a bonus to stats

STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

class Race:
    def __init__(self, name: str, subrace: str = None):
        self.name = name
        self.subrace = subrace
        self.bonuses = {}  # e.g., {"DEX": +2, "WIS": +1}

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats

    def description(self) -> str:
        return self.subrace if self.subrace else self.name
    