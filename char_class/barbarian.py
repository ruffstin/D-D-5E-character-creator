# barbarian.py 

from .char_class import CharClass
from item import Item

class Barbarian(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Barbarian"
        self.hit_die_value = 12
        self.proficient_saving_throws = ["STR", "CON"]
        self.skills_proficient = {"Animal Handling", "Athletics", "Intimidation", "Nature", 
                                  "Perception", "Survival"}
        # update for choices and all items
        # proficient items/tools= ["light armor", "medium armor", "shields"]  # ADD ALL PROFICEINCIES
        self.inventory = {
            "Greataxe": (Item("Greataxe"), 1),
            "Handaxe": (Item("Handaxe"), 2),
            "Explorer's Pack": (Item("Explorer's Pack", "A pack with adventuring gear."), 1)
        }
        self.features = ["Rage", "Unarmored Defense", "Danger Sense"] # implement leveling up for more features
        