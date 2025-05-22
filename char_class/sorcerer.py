# sorcerer.py

from .char_class import CharClass

class Sorcerer(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Sorcerer"
        self.hit_die_value = 6
        self.proficient_saving_throws = ["CON", "CHA"]
        # choose 2
        self.skills_proficient = {"Arcana", "Deception", "Insight", "Intimidation", 
                                  "Persuasion", "Religion"}
        # update for choices
        self.items = ["dagger", "light crossbow", "arcane focus"]
        self.features = ["Spellcasting", "Font of Magic"]