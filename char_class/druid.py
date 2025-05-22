# druid.py 

from .char_class import CharClass

class Druid(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Druid"
        self.hit_die_value = 8
        self.proficient_saving_throws = ["INT", "WIS"]
        self.skills_proficient = {"Animal Handling", "Arcana", "History", "Insight", 
                                  "Medicine", "Nature", "Perception", "Religion"}
        # tool proficiencies herbalism kit
        # update for choices
        self.items = ["leather armor", "shield", "scimitar", "druidic focus"] # ADD ALL ITEMS
        self.features = ["Druidic", "Wild Shape", "Spellcasting"] # implement leveling up for more features