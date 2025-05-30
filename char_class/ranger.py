# ranger.py
from .char_class import CharClass
from item import Item

class Ranger(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Ranger"
        self.hit_die_value = 10
        self.proficient_saving_throws = ["STR", "DEX"]
        self.skills_known = 3
        self.skills_proficient = {"Animal Handling", "Athletics", "Insight", "Investigation", 
                                   "Nature", "Perception", "Stealth", "Survival"}
        # update for choices
        self.inventory = {
            "Scale Mail": (Item("Scale Mail"), 1),
            "Shortsword": (Item("Shortsword"), 1),
            "Longbow": (Item("Longbow"), 1),
        }
        self.features = ["Favored Enemy", "Natural Explorer", "Fighting Style", "Spellcasting"] # implement leveling up for more features