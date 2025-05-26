# bard.py 

from .char_class import CharClass

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
        # update for choices
        self.items = ["rapier", "lute", "entertainer's pack"] # ADD ALL ITEMS
        self.features = ["Bardic Inspiration", "Spellcasting", "Jack of All Trades"] # implement leveling up for more features