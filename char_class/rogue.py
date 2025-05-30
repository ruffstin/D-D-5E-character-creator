# rogue.py

from .char_class import CharClass
from item import Item

class Rogue(CharClass):
    ABILITY_SCORE_IMPROVEMENT = {4, 8, 10, 12, 16, 19}

    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Rogue"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["DEX", "INT"]
        self.skills_known = 4
        self.skills_proficient = {"Acrobatics", "Athletics", "Deception", "Insight", 
                                  "Intimidation", "Investigation", "Perception", 
                                  "Performance", "Persuasion", "Sleight of Hand", 
                                  "Stealth"}
        # update for choices and add all items
        self.inventory = {
            "Leather Armor": (Item("Leather Armor"), 1),
            "Rapier": (Item("Rapier"), 1),
            "Thieves' Tools": (Item("Thieves' Tools", "Tools for lockpicking and disarming traps."), 1)
        }
        self.features = ["Sneak Attack", "Thieves' Cant", "Cunning Action", "Expertise"]