# monk.py
from .char_class import CharClass
from item import Item

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
        # update for choices and all items
        self.inventory = {
            "Shortsword": (Item("Shorsword"), 1),
            "Dart": (Item("Dart"), 10)
        }
        self.features = ["Unarmored Defense", "Martial Arts", "Ki"] # implement leveling up for more features

