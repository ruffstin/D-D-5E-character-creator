# ranger.py

from .char_class import CharClass

class Ranger(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Ranger"
        self.hit_die_value = 10
        self.proficient_saving_throws = ["STR", "DEX"]
        # choose 3 
        self.skills_proficient = {"Animal Handling", "Athletics", "Insight", "Investigation", 
                                   "Nature", "Perception", "Stealth", "Survival"}
        # update for choices
        self.items = ["scale mail", "shortsword", "longbow"]
        self.features = ["Favored Enemy", "Natural Explorer", "Fighting Style", "Spellcasting"] # implement leveling up for more features