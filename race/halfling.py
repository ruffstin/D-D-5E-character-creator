# halfling.py
from .race import Race

class Halfling(Race):
    def __init__(self, subrace: str = "Lightfoot Halfling"):
        super().__init__("Halfling", subrace)
        self.set_bonuses()
        self.size = "Small"
        self.speed = 25 
        self.features = ["Lucky", "Brave", "Halfling Nimbleness"]
        self.languages = ["Common", "Halfling"]
    
    def set_bonuses(self):
        # All elves get +2 DEX
        self.bonuses = {"DEX": 2}
        if self.subrace == "Lightfoot Halfling":
            self.bonuses["CHA"] = 1
            self.features.append("Naturally Stealthy")

        elif self.subrace == "Stout Halfling":
            self.bonuses["CON"] = 1
            self.features.append("Stout Resilience")
        # else: no extra subrace bonus
