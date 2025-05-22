# rogue.py

from .char_class import CharClass

class Rogue(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Rogue"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["DEX", "INT"]
        # choose four
        self.skills_proficient = {"Acrobatics", "Athletics", "Deception", "Insight", 
                                  "Intimidation", "Investigation", "Perception", 
                                  "Performance", "Persuasion", "Sleight of Hand", 
                                  "Stealth"}
        # update for choices
        self.items = ["Leather Armor", "Rapier", "thieves' tools"] # ADD ALL ITEMS
        self.features = ["Sneak Attack", "Thieves' Cant", "Cunning Action", "Expertise"]