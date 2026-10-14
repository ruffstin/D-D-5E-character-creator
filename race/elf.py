# elf.py
from .race import Race
from languages import LANGUAGES

class Elf(Race):
    SUBRACES = {
            "High Elf": "",
            "Wood Elf": "",
            "Dark Elf": ""
        }
    
    def __init__(self, subrace: str = "High Elf"):
        super().__init__("Elf", subrace)
        self.features = {
            "Darkvision": "", 
            "Keen Senses": "", 
            "Fey Ancestry": "", 
            "Trance": ""
        }
        
        # Skill Proficiency:
        self.fixed_skills = {"Perception"}
        
        # -----------------------------
        # Languages
        # -----------------------------
        self.add_language("Common")
        self.add_language("Elvish")
        
        self.set_bonuses()
    
    def set_bonuses(self):
        # All elves get +2 DEX
        self.bonuses = {"DEX": 2}
        
        if self.subrace == "High Elf":
            self.bonuses["INT"] = 1
            self.features.update({
                "Cantrip": "", 
                "Elf Weapon Training": ""
            })
            # High elves know one cantrip of their choice from the wizard spell list
            # they can cast this spell using INT as the spellcasting ability
            self.other_proficiencies.update({"longsword", "shortsword", "shortbow", "longbow"})
            self.choice_options["language"] = {
            "type": "language",
            "options": list(LANGUAGES.keys()),
            "choose": 1
            }            
            
        elif self.subrace == "Wood Elf":
            self.bonuses["WIS"] = 1
            self.speed = 35
            self.features.update({
                "Fleet of Foot": "", 
                "Mask of the Wild": "", 
                "Elf Weapon Training": ""
            })
            self.other_proficiencies.update({"longsword", "shortsword", "shortbow", "longbow"})

        elif self.subrace == "Dark Elf": # Drow
            self.bonuses["CHA"] = 1
            # Drow Magic
            # Dark elves know the dancing lights cantrip
            # they can cast these spells using CHA as the spellcasting ability
            self.other_proficiencies.update({"rapier", "shortsword", "hand crossbow"}) 
            self.features.pop("Darkvision", None)  # removes if exists, otherwise does nothing
             # Drow have superior darkvision
            self.features.update({
                "Drow Magic": "", 
                "Dancing Lights": "", 
                "Drow Weapon Training": "", 
                "Superior Darkvision": "", 
                "Sunlight Sensitivity": ""
            }) 

    def _initialize_fixed_traits(self):
        self.features = {
            "Darkvision": "", 
            "Keen Senses": "", 
            "Fey Ancestry": "", 
            "Trance": ""
        }
        self.speed = 30
        self.other_proficiencies = set()
        self.choice_options.pop("language", None)
        self.set_bonuses()

    def level_up(self, level, features):
        if (self.subrace == "Dark Elf"):
            if level >= 3:
                self.features["Faerie Fire (1/long rest)"] = "use your charisma mod"            
            if level >= 5: 
                self.features["Darkness (1/long rest)"] = "use your charisma mod"

        return features 
    