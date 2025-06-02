# parent - race.py
# A race may have a subrace, and will provide a bonus to stats

STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

class Race:
    def __init__(self, name: str, subrace: str = None):
        self.name = name
        self.subrace = subrace
        self.bonuses = {}  # e.g., {"DEX": +2, "WIS": +1}
        self.languages: set[str] = set()
        self.speed = 30
        self.features = []
        self.skills_proficient = set()
        self.spells_known: set[str] = set()
        self.size = "Medium"
        self.other_proficiencies = set()

    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats
    
    def get_languages(self) -> list[str]:
        """
        Returns the list of languages in the order they were added.
        Internal storage is a set; only use .add() to preserve order and uniqueness.
        """
        return list(self.languages)    
    
    def get_speed(self) -> int:
        return self.speed if hasattr(self, 'speed') else 0
    
    def get_features(self) -> list[str]:
        return self.features if hasattr(self, 'features') else []

    def get_skills(self) -> set[str]:
        return self.skills_proficient if hasattr(self, 'skills_proficient') else set()
    
    def level_up(self, char_level: int, char_features: list[str]):
        return None

    def description(self) -> str:
        return self.subrace if self.subrace else self.name
    
def choose_languages(self, known_languages: set, n: int) -> set:
    """
    Default: No language choices. Override in subclasses that grant language choices.
    """
    return None
    