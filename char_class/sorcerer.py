# sorcerer.py
from .char_class import CharClass
from item import Item

class Sorcerer(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Sorcerer"
        self.subclass_options = {"Draconic Bloodline", "Wild Magic"}
        self.hit_die_value = 6
        self.proficient_saving_throws = ["CON", "CHA"]
        # choose 2
        self.skills_proficient = {"Arcana", "Deception", "Insight", "Intimidation", 
                                  "Persuasion", "Religion"}
        # update for choices and all items 
        self.inventory = {
            "Dagger": (Item("Dagger"), 1),
            "Light Crossbow": (Item("Light Crossbow"), 1),
            "Arcane Focus": (Item("Arcane Focus", "A focus for casting spells"), 1)

        }

        # Apply level 1 features
        self.features = ["Spellcasting", "Sorcerous Origin"]
        #call sorcerous_origin since subclass is chosen at level 1

    def get_max_sorcery_points(self, level):
        if "Font of Magic" in self.features:
            return level
        else: 
            return 0

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Font of Magic" not in self.features:
                        self.features.append("Font of Magic")
                        char_features.append("Font of Magic")
                        #implement font of magic features

                if self.level == 3:
                    if "Metamagic" not in self.features: 
                        self.features.append("Metamagic")
                        char_features.append("Metamagic")
                        # call pick metamagic function   
                        # pick another option at 10th level 
                        # pick another option at 17th level

                if self.level == 20: 
                    if "Sorcerous Restoration" not in self.features:
                        self.features.append("Sorcerous Restoration")
                        char_features.append("Sorcerous Restoration")     


        # if self.level in {} call sorcerous_origin feature

        # def pick sorcerous_origin function 
            
        # def sorcerous_origin feature function    
            #self.sorcerous_origin_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen