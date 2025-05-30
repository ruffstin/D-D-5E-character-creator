# cleric.py 
from .char_class import CharClass
from item import Item

class Cleric(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Cleric"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["WIS", "CHA"]
        self.skills_proficient = {"History", "Insight", "Medicine", "Persuasion", 
                                  "Religion"}
        # update for choices
        self.inventory = {
            "Shield": (Item("Shield"), 1),
            "Mace": (Item("Mace"), 1),
            "Holy Symbol": (Item("Holy Symbol", "A source for holy magic and prayer"), 1),
        }
        self.features = ["Spellcasting", "Channel Divinity", "Destroy Undead"] # implement leveling up for more features
        