# fighter.py 
from .char_class import CharClass
from item import Item

class Fighter(CharClass):
    ABILITY_SCORE_IMPROVEMENT = {4, 6, 8, 12, 14, 16, 19}

    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Fighter"
        self.subclass_options = {"Champion", "Battle Master", "Eldritch Knight"}
        self.hit_die_value = 10
        self.proficient_saving_throws = ["STR", "CON"]
        self.skills_proficient = {"Athletics", "Acrobatics", "Animal Handling", "History", 
                                  "Insight", "Intimidation", "Perception", "Survival"}
        
        # update for choices and add all items
        self.inventory = {
            "Chain Mail": (Item("Chain Mail"), 1),
            "Shield": (Item("Shield"), 1),
            "Longsword": (Item("Longsword"), 1)
        }

        # Apply level 1 features
        self.features = ["Fighting Style", "Second Wind"] # implement choices for fighting style
        self.martial_archetype_features = {}

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Action Surge" not in self.features:
                        self.features.append("Action Surge x 1")
                        char_features.append("Action Surge x 1")
                        #implement number of uses based on level
                
                if self.level == 3:    
                    if "Martial Archetype" not in self.features: 
                        self.features.append("Martial Archetype")
                        char_features.append("Martial Archetype")
                        # call pick archetype function
                    
                if self.level == 5 or self.level == 11 or self.level == 20:
                    if "Extra Attack Fighter x1" not in self.features:
                        self.features.append("Extra Attack Fighter x1")
                        char_features.append("Extra Attack Fighter x1")
                    
                    elif self.level == 11: 
                        self.features.append("Extra Attack Fighter x2")
                        char_features.append("Extra Attack Fighter x2")
                    
                    elif self.level == 20:
                        self.features.append("Extra Attack Fighter x3")
                        char_features.append("Extra Attack Fighter x3")

                if self.level == 9:
                    if "Indomitable" not in self.features:
                        self.features.append("Indomitable")
                        char_features.append("Indomitable")
                        # implement number of uses based on level

                # if self.level in {} call martial_archetype feature

        # def pick martial_archetype function 
            
        # def martial_archetype feature function    
            #self.martial_archetype_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen