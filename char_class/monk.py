# monk.py
 
from .char_class import CharClass

class Monk(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Monk"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["STR", "DEX"]
        # choose 2
        self.skills_proficient = {"Acrobatics", "Athletics", "History", "Insight", 
                                  "Religion", "Stealth"}
        # tool proficiency
        # update for choices
        self.items = ["shortsword", "dart"] # ADD ALL ITEMS, 10 darts?!
        self.features = ["Unarmored Defense", "Martial Arts", "Ki"] # implement leveling up for more features

