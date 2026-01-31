# ranger.py
from .char_class import CharClass
from item import Item

class Ranger(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Ranger"
        self.subclass_options = {"Hunter", "Beast Master"}
        self.hit_die_value = 10
        self.proficient_saving_throws = ["STR", "DEX"]
        self.skills_known = 3
        self.skills_proficient = {"Animal Handling", "Athletics", "Insight", "Investigation", 
                                   "Nature", "Perception", "Stealth", "Survival"}
        # update for choices
        self.inventory = {
            "Scale Mail": (Item("Scale Mail"), 1),
            "Shortsword": (Item("Shortsword"), 1),
            "Longbow": (Item("Longbow"), 1),
        }
        self.features = ["Favored Enemy", "Natural Explorer"] # implement leveling up for more features
        self.language = "" # set language based off favored enemy
        self.enclave_features = {}

    def get_langauge(self) -> str:
        return self.language

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Fighting Style" not in self.features:
                        self.features.append("Fighting Style")
                        char_features.append("Fighting Style")
                
                    if "Spellcasting" not in self.features: 
                        self.features.append("Spellcasting")
                        char_features.append("Spellcasting")

                if self.level == 3: 
                    if "Primeval Awareness" not in self.features: 
                        self.features.append("Primeval Awareness")
                        char_features.append("Primeval Awareness")

                    if "Ranger Enclave" not in self.features: 
                        self.features.append("Ranger Enclave")
                        char_features.append("Ranger Enclave")
                        # call pick ranger enclave function
                
                if self.level == 5: 
                    if "Extra Attack" not in self.features: 
                        self.features.append("Extra Attack")
                        char_features.append("Extra Attack")
                
                if self.level == 8: 
                    if "Land's Stride" not in self.features: 
                        self.features.append("Land's Stride")
                        char_features.append("Land's Stride")

                if self.level == 10: 
                    if "Hide in Plain Sight" not in self.features: 
                        self.features.append("Hide in Plain Sight")
                        char_features.append("Hide in Plain Sight")

                if self.level == 14: 
                    if "Vanish" not in self.features:
                        self.features.append("Vanish")
                        char_features.append("Vanish")
                    
                if self.level == 18: 
                    if "Feral Senses" not in self.features: 
                        self.features.append("Feral Senses")
                        char_features.append("Feral Senses")

                if self.level == 20: 
                    if "Foe Slayer" not in self.features: 
                        self.features.append("Foe Slayer")
                        char_features.append("Foe Slayer")
                
                # if self.level in {} call enclave feature

        # def pick ranger enclave function 
            
        # def enclave feature function    
            #self.enclave_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen