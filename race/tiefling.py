# tiefling.py
from .race import Race

class Tiefling(Race):
    def __init__(self):
        super().__init__("Tiefling", None)
        self.set_bonuses()
        self.features = ["Darkvision", "Hellish Resistance (fire damage resistance)", "Infernal Legacy"]
        # Infernal Legacy: Thaumaturgy cantrip, Hellish Rebuke spell (2nd level), Darkness spell (3rd level)
        # Charisma is the spellcasting ability for these spells, you may cast them once per long rest
        self.languages = ["Common", "Infernal"]

    def set_bonuses(self):
        # All tieflings get +2 CHA and +1 to INT
        self.bonuses = {"CHA": 2, "INT": 1}

    def level_up(self, level, features):
        if level >= 3 and "level 3 spell" not in features:
            features.append("level 3 spell")
            
        if level >= 5 and "level 5 spell" not in features: 
            features.append("level 5 spell ")
        
        return features