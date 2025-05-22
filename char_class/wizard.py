# wizard.py 

from .char_class import CharClass

class Wizard(CharClass): 
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Wizard"
        self.hit_die_value = 6
        self.proficient_saving_throws = ["INT", "WIS"]
        # choose 2 
        self.skills_proficient = {"Arcana", "History", "Insight", 
                                  "Investigation", "Medicine", "Religion"}
        # update for choices
        self.items = ["quarterstaff", "arcane focus", "spellbook"] # ADD ALL ITEMS
        self.features = ["Spellcasting", "Arcane Recovery"] # implement leveling up for more features