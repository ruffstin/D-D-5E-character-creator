# gnome.py

from .race import Race
STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

class Gnome(Race):
    def __init__(self, subrace: str = "Forest Gnome"):
        super().__init__("Gnome", subrace)
        self.set_bonuses()
    
    def set_bonuses(self):
        # All gnomes get +2 INT
        self.bonuses = {"INT": 2}
        if self.subrace == "Forest Gnome":
            self.bonuses["DEX"] = 1
        elif self.subrace == "Rock Gnome":
            self.bonuses["CON"] = 1
        # else: no additional bonuses

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats
