# barbarian.py 

from .char_class import CharClass
from item import Item

class Barbarian(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Barbarian"
        self.subclass_options = {"Berserker", "Totem Warrior"}
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

        # Apply level 1 features
        self.features = ["Rage", "Unarmored Defense", "Danger Sense"] # implement leveling up for more features
        self.primal_path_features = {}

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Reckless Attack" not in self.features:
                        self.features.append("Reckless Attack")
                        char_features.append("Reckless Attack")

                    if "Danger Sense" not in self.features:
                        self.features.append("Danger Sense")
                        char_features.append("Danger Sense")

                if self.level == 3:    
                    if "Primal Path" not in self.features: 
                        self.features.append("Primal Path")
                        char_features.append("Primal Path")
                        # call pick path function
                    
                if self.level == 5:
                    if "Extra Attack" not in self.features:
                        self.features.append("Extra Attack")
                        char_features.append("Extra Attack")

                    if "Fast Movement" not in self.features:
                        self.features.append("Fast Movement")
                        char_features.append("Fast Movement")

                if self.level == 7: 
                    if "Feral Instinct" not in self.features:
                        self.features.append("Feral Instinct")
                        char_features.append("Feral Instinct")

                if self.level == 9:
                    if "Brutal Critical" not in self.features:
                        self.features.append("Brutal Critical")
                        char_features.append("Brutal Critical")

                if self.level == 11:
                    if "Relentless Rage" not in self.features:
                        self.features.append("Relentless Rage")
                        char_features.append("Relentless Rage")

                if self.level == 15:
                    if "Persistent Rage" not in self.features:
                        self.features.append("Persistent Rage")
                        char_features.append("Persistent Rage")

                if self.level == 20:
                    if "Primal Champion" not in self.features:
                        self.features.append("Primal Champion")
                        char_features.append("Primal Champion")
                
                # if self.level in {} call path feature

        # def pick Primal Path function 
            
        # def primal path feature function    
            #self.primal_features.append
            # char_features.append

            #which if statement will depend on subclass chosen