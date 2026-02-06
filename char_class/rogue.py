# rogue.py

from .char_class import CharClass
from item import Item
SNEAK_ATTACK_DICE = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

class Rogue(CharClass):
    ABILITY_SCORE_IMPROVEMENT = {4, 8, 10, 12, 16, 19}

    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Rogue"
        self.subclass_options = {"Thief ", "Assassin", "Arcane Tricker"}

        self.hit_die_value = 8
        self.proficient_saving_throws = ["DEX", "INT"]
        self.skills_known = 4
        self.skills_proficient = {"Acrobatics", "Athletics", "Deception", "Insight", 
                                  "Intimidation", "Investigation", "Perception", 
                                  "Performance", "Persuasion", "Sleight of Hand", 
                                  "Stealth"}
        # update for choices and add all items
        self.inventory = {
            "Leather Armor": (Item("Leather Armor", armor_type="light"), 1),
            "Rapier": (Item("Rapier"), 1),
            "Thieves' Tools": (Item("Thieves' Tools", "Tools for lockpicking and disarming traps."), 1)
        }

        # Apply level 1 features
        self.features = ["Sneak Attack", "Thieves' Cant", "Expertise"]
        self.sneak_attack_die = 6
        self.secret_languages = ["Thieves' Cant"]
        self.roguish_features = {}
        self.expertise = set()
        # def set expertise, 2 skills your proficient in, or 1 and thieves tools

    def get_sneak_attack(self, level):    
        return SNEAK_ATTACK_DICE[level] #d6 implement more clear return?
        
    def get_languages(self):
        return self.secret_languages
        
    # def set expertise(self, current list of proficient skills, current list of expertise skills, tool list)
    


    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Cunning Action" not in self.features:
                        self.features.append("Cunning Action")
                        char_features.append("Cunning Action")
                
                if self.level == 3:
                    if "Roguish Archetype" not in self.features: 
                        self.features.append("Roguish Archetype")
                        char_features.append("Roguish Archetype")
                        # call pick Roguish Archetype function

                if self.level == 5: 
                    if "Uncanny Dodge" not in self.features: 
                        self.features.append("Uncanny Dodge")
                        char_features.append("Uncanny Dodge")

                if self.level == 6:
                    if "Additional Expertise" not in self.features:
                        self.features.append("Additional Expertise")
                        char_features.append("Additional Expertise")
                        # implement expertise choice function
                        # def set expertise, 2 skills your proficient in, or 1 and thieves tools

                if self.level == 7: 
                    if "Evasion" not in self.features: 
                        self.features.append("Evasion")
                        char_features.append("Evasion")

                if self.level == 11: 
                    if "Reliable Talent" not in self.features: 
                        self.features.append("Reliable Talent")
                        char_features.append("Reliable Talent")

                if self.level == 14:
                    if "Blindsense" not in self.features: 
                        self.features.append("Blindsense")
                        char_features.append("Blindsense")

                if self.level == 15: 
                    if "Slippery Mind" not in self.features:
                        self.features.append("Slippery Mind")
                        char_features.append("Slippery Mind")

                if self.level == 18: 
                    if "Elusive" not in self.features: 
                        self.features.append("Elusive")
                        char_features.append("Elusive")

                if self.level == 20: 
                    if "Stroke of Luck" not in self.features: 
                        self.features.append("Stroke of Luck")
                        char_features.append("Stroke of Luck")
                
                # if self.level in {} call roguish_archetype feature

    # def pick roguish archetype function 
            
    # def roguish_archetype feature function    
        #self.roguish_features.append
        # char_features.append

        #which if statement will depend on sublcass chosen