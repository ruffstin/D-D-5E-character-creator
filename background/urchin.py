# urchin.py
from .background import Background

class Urchin(Background):
    def __init__(self):
        super().__init__("Urchin")
        self.skills = {"Sleight of Hand", "Stealth"}
        self.items = [
            "A small knife",
            "A map of the city you grew up in",
            "A pet mouse",
            "A set of common clothes",
            "A belt pouch containing 10 gp"
        ]
        self.features = ["City Secrets"]
        self.tools_proficient = {"Disguise kit", "Thieves' tools"}