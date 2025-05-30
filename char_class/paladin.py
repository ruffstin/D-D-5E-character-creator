# paladin.py
from .char_class import CharClass
from item import Item

class Paladin(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Paladin"
        self.hit_die_value = 10
        self.proficient_saving_throws = ["WIS", "CHA"]
        # choose 2
        self.skills_proficient = {"Athletics", "Insight", "Intimidation", 
                                  "Medicine", "Persuasion", "Religion"}
        # update for choices and all items
        self.inventory = {
            "Chain Mail": (Item("Chain Mail"), 1),
            "Shield": (Item("Shield"), 1),
            "Longsword": (Item("Longsword"), 1)
        }

        self.features = ["Divine Sense", "Lay on Hands", "Fighting Style", 
                         "Spellcasting"] # implement leveling up for more features