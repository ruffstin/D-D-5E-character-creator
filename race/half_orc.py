# half_orc.py
from .race import Race

class HalfOrc(Race):

    SUBRACES = {}
    
    def __init__(self, subrace: str = None):
        super().__init__("Half-Orc", subrace)
        self.features = {
            "Darkvision": "", 
            "Menacing": "", 
            "Relentless Endurance": "", 
            "Savage Attacks": ""
        }
        # Skill Proficiency:
        self.fixed_skills = {"Intimidation"}

        # -----------------------------
        # Languages
        # -----------------------------
        self.add_language("Common")
        self.add_language("Orc")
        
        # All half-orcs get +2 STR and +1 CON
        self.bonuses = {"STR": 2, "CON": 1}
        
