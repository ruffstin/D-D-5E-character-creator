# bard.py 
from .char_class import CharClass
from item import Item

class Bard(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Bard"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["DEX", "CHA"]
        self.skills_known = 3
        self.skills_proficient = {"Acrobatics", "Animal Handling", "Arcana", "Athletics", 
                                  "Deception", "History", "Insight", "Intimidation", 
                                  "Investigation", "Medicine", "Nature", "Perception", 
                                  "Performance", "Persuasion", "Religion", 
                                  "Sleight of Hand", "Stealth", "Survival"}
        # update for choices and all items
        self.inventory = {
            "Rapier": (Item("Rapier"), 1),
            "Lute": (Item("Lute", "A musical instrument."), 1),
            "Entertainer's Pack": (Item("Entertainer's Pack", "A pack with performance gear."), 1)
        }        
        self.features = ["Bardic Inspiration", "Spellcasting", "Jack of All Trades"] # implement leveling up for more features