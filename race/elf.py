# elf.py
from .race import Race

class Elf(Race):
    def __init__(self, subrace: str = "High Elf"):
        super().__init__("Elf", subrace)
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
            self.languages.append("one extra language of your choice")

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
