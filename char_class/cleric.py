# cleric.py 

from .char_class import CharClass

class Cleric(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Cleric"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["WIS", "CHA"]
        self.skills_proficient = {"History", "Insight", "Medicine", "Persuasion", 
                                  "Religion"}
        # update for choices
        self.items = ["shield", "mace", "holy symbol"] # ADD ALL ITEMS
        self.features = ["Spellcasting", "Channel Divinity", "Destroy Undead"] # implement leveling up for more features
        