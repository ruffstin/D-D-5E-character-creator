# warlock.py
from .char_class import CharClass
from item import Item

class Warlock(CharClass): 
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Warlock"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["WIS", "CHA"]
        # choose 2 
        self.skills_proficient = {"Arcana", "Deception", "History", "Intimidation", 
                                  "Investigation", "Nature", "Religion"}
        # update for choices and all items
        self.inventory = {
            "Arcane Focus": (Item("Arcane Focus", "A focus for casting spells"), 1),
            "Light Crossbow": (Item("Light Crossbow"), 1)
        }
        self.features = ["Pact Magic", "Eldritch Invocations", "Pact Boon"] # implement leveling up for more features