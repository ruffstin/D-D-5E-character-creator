# paladin.py
from .char_class import CharClass
from item import Item

class Paladin(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Paladin"
        self.subclass_options = {"Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"}
        self.hit_die_value = 10
        self.proficient_saving_throws = ["WIS", "CHA"]
        # choose 2
        self.skills_proficient = {"Athletics", "Insight", "Intimidation", 
                                  "Medicine", "Persuasion", "Religion"}
        # update for choices and all items
        self.inventory = {
            "Chain Mail": (Item("Chain Mail", armor_type="heavy"), 1),
            "Shield": (Item("Shield", armor_type="shield"), 1),
            "Longsword": (Item("Longsword"), 1)
        }

        # Apply level 1 features
        self.features = ["Divine Sense", "Lay on Hands"] 
        self.sacred_oath_features = {}

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
                        # implement fighting styles choices

                    if "Spellcasting" not in self.features: 
                        self.features.append("Spellcasting")
                        char_features.append("Spellcasting")

                    if "Divine Smite" not in self.features:
                        self.features.append("Divine Smite")
                        char_features.append("Divine Smite")    
                
                if self.level == 3:
                    if "Divine Health" not in self.features: 
                        self.features.append("Divine Health")
                        char_features.append("Divine Health")

                    if "Sacred Oath" not in self.features: 
                        self.features.append("Sacred Oath")
                        char_features.append("Sacred Oath")
                        # call pick oath function

                        self.features.append("Channel Divinity")
                        char_features.append("Channel Divinity")

                if self.level == 5:
                    if "Extra Attack" not in self.features:
                        self.features.append("Extra Attack")
                        char_features.append("Extra Attack")

                if self.level == 6:
                    if "Aura of Protection" not in self.features:
                        self.features.append("Aura of Protection")
                        char_features.append("Aura of Protection") 

                if self.level == 10:
                    if "Aura of Courage" not in self.features:
                        self.features.append("Aura of Courage")
                        char_features.append("Aura of Courage")
                        #increase again at level 18
                
                if self.level == 11: 
                    if "Improved Divine Smite" not in self.features:
                        self.features.append("Improved Divine Smite")
                        char_features.append("Improved Divine Smite")

                if self.level == 14:    
                    if "Cleansing Touch" not in self.features:
                        self.features.append("Cleansing Touch")
                        char_features.append("Cleansing Touch")


    # if self.level in {} call sacred_oath feature

        # def pick sacred_oath function 
            
        # def sacred_oath feature function    
            #self.sacred_oath_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen