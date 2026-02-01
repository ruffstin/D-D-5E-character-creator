# cleric.py 
from .char_class import CharClass
from item import Item

class Cleric(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Cleric"
        self.subclass_options = {"Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", 
                                 "Tempest Domain", "Trickery Domain", "War Domain"}
        self.hit_die_value = 8
        self.proficient_saving_throws = ["WIS", "CHA"]
        self.skills_proficient = {"History", "Insight", "Medicine", "Persuasion", 
                                  "Religion"}
        # update for choices
        self.inventory = {
            "Shield": (Item("Shield", armor_type="shield"), 1),
            "Mace": (Item("Mace"), 1),
            "Holy Symbol": (Item("Holy Symbol", "A source for holy magic and prayer"), 1),
        }

        # Apply level 1 features
        self.features = ["Spellcasting", "Divine Domain"]
        self.domain_features = {}
        #call domain function since subclass is chosen at level 1

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Channel Divinity" not in self.features:
                        self.features.append("Channel Divinity")
                        char_features.append("Channel Divinity")
                        # implement types of channel divinity, Turn undead and specific domains
                
                if self.level == 5:
                    if "Destroy Undead" not in self.features: 
                        self.features.append("Destroy Undead")
                        char_features.append("Destroy Undead")

                if self.level == 8:
                    if "Divine Strike" not in self.features:
                        self.features.append("Divine Strike")
                        char_features.append("Divine Strike")
                
                if self.level == 10: 
                    if "Divine Intervention" not in self.features:
                        self.features.append("Divine Intervention")
                        char_features.append("Divine Intervention")
                        # it changes at lvl 20
            
            # if self.level in {} call domain feature

            # def domain feature function    
            #self.domain_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen

