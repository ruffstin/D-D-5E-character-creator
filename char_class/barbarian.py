# barbarian.py 

from .char_class import CharClass

class Barbarian(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Barbarian"
        self.hit_die_value = 12
        self.proficient_saving_throws = ["STR", "CON"]
        self.skills_proficient = {"Animal Handling", "Athletics", "Intimidation", "Nature", 
                                  "Perception", "Survival"}
        # update for choices
        # proficient items/tools= ["light armor", "medium armor", "shields"]  # ADD ALL PROFICEINCIES
        self.items = ["greataxe", "handaxe", "handaxe", "explorer's pack"] # ADD ALL ITEMS
        self.features = ["Rage", "Unarmored Defense", "Danger Sense"] # implement leveling up for more features
        