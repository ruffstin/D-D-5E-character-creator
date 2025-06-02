# elf.py
from .race import Race
from languages import LANGUAGES

class Elf(Race):
    def __init__(self, subrace: str = "High Elf"):
        super().__init__("elf", subrace)
        if subrace not in ["High Elf", "Wood Elf", "Dark Elf", "Drow"]:
            raise ValueError("Invalid subrace. Choose from 'High Elf', 'Wood Elf', or 'Dark Elf' / 'Drow'.")
       
        self.features = ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"]
        self.skills_proficient = {"Perception"}
        self.languages = ["Common", "Elvish"]
        self.size = "Medium"
        self.set_bonuses()
    
    def set_bonuses(self):
        # All elves get +2 DEX
        self.bonuses = {"DEX": 2}
        if self.subrace == "High Elf":
            self.bonuses["INT"] = 1
            self.features.append("Cantrip") 
            # High elves know one cantrip of their choice from the wizard spell list
            # they can cast this spell using INT as the spellcasting ability
            self.features.append("Elf Weapon Training")
            self.other_proficiencies.update({"longsword", "shortsword", "shortbow", "longbow"})
            extra_lang = self.choose_languages(set(self.languages), 1)
            if extra_lang:
                for lang in extra_lang:
                    self.languages.append(lang)

        elif self.subrace == "Wood Elf":
            self.bonuses["WIS"] = 1
            self.features.append("Fleet of Foot")
            self.speed = 35
            self.features.append("Mask of the Wild")
            self.features.append("Elf Weapon Training")
            self.other_proficiencies.update({"longsword", "shortsword", "shortbow", "longbow"})

        elif self.subrace == "Dark Elf" or self.subrace == "Drow":
            self.bonuses["CHA"] = 1
            self.features.append("Drow Magic") # Drow Magic
            # Dark elves know the dancing light cantrip
            # at 3rd level, they can cast faerie fire once per long rest
            # at 5th level, they can cast darkness once per long rest
            # they can cast these spells using CHA as the spellcasting ability
            self.features.append("Drow Weapon Training")
            self.other_proficiencies.update({"rapier", "shortsword", "hand crossbow"}) 
            self.features.remove("Darkvision") # Drow have superior darkvision
            self.features.append("Superior Darkvision") 
            self.features.append("Sunlight Sensitivity")

        # else: no additional bonuses
    
    def level_up(self, level, features):
        if (self.subrace == "Drow" or self.subrace == "Dark Elf"):
            if level >= 3:
                features.append("level 3 spell")
            
            if level >= 5: 
                features.append("level 5 spell ")
        
        return features
    
    def choose_languages(self, known_languages: set, n: int) -> set:
        # Filter out already known and secret languages        
        chosen = set()
        current_known = set(known_languages)
        while len(chosen) < n:
            available = [name for name, lang in LANGUAGES.items()
                if lang.lang_type != "secret" and name not in current_known]
            standard = [name for name in available if LANGUAGES[name].lang_type == "standard"]
            exotic = [name for name in available if LANGUAGES[name].lang_type == "exotic"]
            print("\nChoose a language you do not already know:")
            print("Standard Languages:")
            for i, lang in enumerate(standard):
                print(f"  {i+1}. {lang}")
            print("Exotic Languages:")
            for i, lang in enumerate(exotic):
                print(f"  {i+1+len(standard)}. {lang}")

            choice = input(f"Enter the name of language {len(chosen)+1}/{n}: ").strip()
            # Find a matching language in available, case-insensitive
            matching_lang = next((lang for lang in available if lang.lower() == choice.lower()), None)
            if matching_lang and matching_lang not in chosen:
                chosen.add(matching_lang)
                current_known.add(matching_lang)
            else:
                print("Invalid or duplicate choice. Please try again.")
        return chosen
