# wizard.py 
from .char_class import CharClass
from item import Item

class Wizard(CharClass): 
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Wizard"
        self.hit_die_value = 6
        self.proficient_saving_throws = ["INT", "WIS"]
        # choose 2 
        self.skills_proficient = {"Arcana", "History", "Insight", 
                                  "Investigation", "Medicine", "Religion"}
        # update for choices and all items
        self.inventory = {
            "Quarterstaff": (Item("Quarterstaff"), 1),
            "Arcane Focus": (Item("Arcane Focus", "A focus for casting spells"), 1),
            "Spellbook": (Item("Spellbook", "A book to record spells in, requires a special ink"), 1),
        }
        self.features = ["Spellcasting", "Arcane Recovery"] # implement leveling up for more features