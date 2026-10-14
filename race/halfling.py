# halfling.py
from .race import Race

class Halfling(Race):

    SUBRACES = {
        "Lightfoot Halfling": "",
        "Stout Halfling": ""
    }

    def __init__(self, subrace: str = "Lightfoot Halfling"):
        super().__init__("Halfling", subrace)
     
        self.size = "Small"
        self.speed = 25 

        self.features = {
            "Lucky": "", 
            "Brave": "", 
            "Halfling Nimbleness": ""
        }

        # -----------------------------
        # Languages
        # -----------------------------
        self.add_language("Common")
        self.add_language("Halfling")

        self.set_bonuses()
    
    def set_bonuses(self):
        # All halflings get +2 DEX
        self.bonuses = {"DEX": 2}
        
        if self.subrace == "Lightfoot Halfling":
            self.bonuses["CHA"] = 1
            self.features["Naturally Stealthy"] = ""

        elif self.subrace == "Stout Halfling":
            self.bonuses["CON"] = 1
            self.features["Stout Resilience"] = ""
        # else: no extra subrace bonus
