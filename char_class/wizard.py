# wizard.py 
from .char_class import CharClass
from item import Item

class Wizard(CharClass): 
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Wizard"
        self.subclass_options = {"School of Abjuration", "School of Conjuration", "School of Divination",
                                 "School of Enchantment", "School of Evocation", 
                                 "School of Illusion", "School of Necromancy", 
                                 "School of Transmutation"}
        self.hit_die_value = 6
        self.proficient_saving_throws = ["INT", "WIS"]
        # choose 2 
        self.skills_proficient = {"Arcana", "History", "Insight", 
                                  "Investigation", "Medicine", "Religion"}
        # update for choices and all items
        self.inventory = {
            "Quarterstaff": (Item("Quarterstaff"), 1),
            "Arcane Focus": (Item("Arcane Focus", "A focus for casting spells"), 1),
            "Spellbook": (Item("Spellbook", "A book to record spells in, requires a special ink"), 1),
        }

        # Apply level 1 features
        self.features = ["Spellcasting", "Arcane Recovery"]
        self.arcane_tradition_features = {}

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)

                if self.level == 2:
                    if "Arcane Tradition" not in self.features: 
                        self.features.append("Arcane Tradition")
                        char_features.append("Arcane Tradition")
                        # call pick arcane_tradition function

                if self.level == 18: 
                    if "Spell Mastery" not in self.features: 
                        self.features.append("Spell Mastery")
                        char_features.append("Spell Mastery")
                
                if self.level == 20: 
                    if "Signature Spells" not in self.features: 
                        self.features.append("Signature Spells")
                        char_features.append("Signature Spells")

        # if self.level in {} call arcane_tradition feature

        # def pick arcane_tradition function 
            
        # def arcane_tradition feature function    
            #self.arcane_tradition_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen