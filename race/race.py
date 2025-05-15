# parent - race.py
# A race may have a subrace, and will provide a bonus to stats

class Race:
    def __init__(self, name: str, subrace: str = None):
        self.name = name
        self.subrace = subrace
        self.bonuses = {}  # e.g., {"DEX": +2, "WIS": +1}

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        # By default: no bonuses
        return stats

    def description(self) -> str:
        return self.subrace if self.subrace else self.name
    