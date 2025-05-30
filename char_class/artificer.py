# artificer.py

from .char_class import CharClass
from item import Item

class Artificer(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Artificer"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["CON", "INT"]
        self.skills_proficient = {"Arcana", "History", "Investigation", "Medicine", 
                                   "Nature", "Perception", "Sleight of Hand"}
        # update for choices 
        self.inventory = {
            "Studded Leather Armor": (Item("Studded Leather Armor"), 1),
            "Thieves' Tools": (Item("Thieves' Tools", "Tools for lockpicking and disarming traps."), 1),
            "Light Crossbow": (Item("Light Crossbow"), 1)
        }        
        self.features = ["Magical Tinkering", "Spellcasting", "Infuse Item"]