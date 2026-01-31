# dwarf.py
from .race import Race

class Dwarf(Race):
    def __init__(self, subrace: str = "Hill Dwarf"):
        super().__init__("Dwarf", subrace)
        self.set_bonuses()
        self.speed = 25
        self.features = ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning"]
        self.languages = ["Common", "Dwarvish"]
        self.other_proficiencies = {"Battleaxe", "Handaxe", "Light hammer", "Warhammer", 
                                    "Pick one of Smith's tools, Brewer's supplies, or Mason's tools"}
    
    def set_bonuses(self):
        # All dwarves get +2 CON
        self.bonuses = {"CON": 2}

        if self.subrace == "Hill Dwarf":
            self.bonuses["WIS"] = 1
            self.features.append("Dwarven Toughness") # plus 1 HP per level

        elif self.subrace == "Mountain Dwarf":
            self.bonuses["STR"] = 2
            self.other_proficiencies.add("light armor")
            self.other_proficiencies.add("medium armor")    

        # else: no extra subrace bonus

