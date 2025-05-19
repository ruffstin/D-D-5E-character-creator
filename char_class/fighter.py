#fighter.py 

from .char_class import CharClass

class Fighter(CharClass):
    def __init__(self, char_class: str, level: int = 1, subclass: str = None):
        super().__init__("Fighter", level, subclass)
        self.hit_die_value = 10
        self.proficient_saving_throws = ["STR", "CON"]
        self.skills_proficient = {"Athletics", "Acrobatics", "Animal Handling", "History", "Insight", "Intimidation", "Perception", "Survival"}
        self.items = ["Chain Mail", "Shield", "Longsword"] # ADD ALL ITEMS
        self.features = ["Second Wind", "Action Surge", "Extra Attack"]