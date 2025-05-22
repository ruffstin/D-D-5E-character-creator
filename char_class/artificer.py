# artificer.py

from .char_class import CharClass

class Artificer(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Artificer"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["CON", "INT"]
        self.skills_proficient = {"Arcana", "History", "Investigation", "Medicine", 
                                   "Nature", "Perception", "Sleight of Hand"}
        # update for choices
        self.items = ["studded leather armor", "thieves' tools", "light crossbow"]  # ADD ALL ITEMS
        self.features = ["Magical Tinkering", "Spellcasting", "Infuse Item"]