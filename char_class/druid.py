# druid.py 
from .char_class import CharClass
from item import Item

class Druid(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Druid"
        self.subclass_options = {"Circle of the Land", "Circle of the Moon"}
        self.hit_die_value = 8
        self.proficient_saving_throws = ["INT", "WIS"]
        self.skills_proficient = {"Animal Handling", "Arcana", "History", "Insight", 
                                  "Medicine", "Nature", "Perception", "Religion"}
        # tool proficiencies herbalism kit
        # update for choices and all items
        self.inventory = {
            "Leather Armor": (Item("Leather Armor", armor_type="light"), 1),
            "Shield": (Item("Shield", armor_type="shield"), 1),
            "Scimitar": (Item("Scimitar"), 1),
            "Druidic Focus": (Item("Druidic Focus", "A focus for druidic spells."), 1)
        }

        # Apply level 1 features
        self.features = ["Druidic", "Spellcasting"] 
        self.secret_languages = ["Druidic"]
        self.circle_features = {}

    def get_languages(self):
        return self.secret_languages

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Wild Shape" not in self.features:
                        self.features.append("Wild Shape")
                        char_features.append("Wild Shape")
                        #implement wild shapes uses
                
                    if "Druid Circle" not in self.features: 
                        self.features.append("Druid Circle")
                        char_features.append("Druid Circle")
                        # call pick circle function
                    
                if self.level == 18: 
                    if "Timeless Body" not in self.features: 
                        self.features.append("Timeless Body")
                        char_features.append("Timeless Body")
                    
                    if "Beast Spells" not in self.features: 
                        self.features.append("Beast Spells")
                        char_features.append("Beast Spells")

                if self.level == 20: 
                    if "Archdruid" not in self.features: 
                        self.features.append("Archdruid")
                        char_features.append("Archdruid")
                
                # if self.level in {} call circle feature

        # def pick circle function 
            
        # def circle feature function    
            #self.circle_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen