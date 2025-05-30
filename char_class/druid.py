# druid.py 
from .char_class import CharClass
from item import Item

class Druid(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Druid"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["INT", "WIS"]
        self.skills_proficient = {"Animal Handling", "Arcana", "History", "Insight", 
                                  "Medicine", "Nature", "Perception", "Religion"}
        # tool proficiencies herbalism kit
        # update for choices and all items
        self.inventory = {
            "Leather Armor": (Item("Leather Armor"), 1),
            "Shield": (Item("Shield"), 1),
            "Scimitar": (Item("Scimitar"), 1),
            "Druidic Focus": (Item("Druidic Focus", "A focus for druidic spells."), 1)
        }
        self.features = ["Druidic", "Wild Shape", "Spellcasting"] # implement leveling up for more features
