# soldier.py
from .background import Background

class Soldier(Background):
    def __init__(self):
        super().__init__("Soldier")
        self.skills = {"Athletics", "Intimidation"}
        self.items = [
            "Insignia of rank",
            "Trophy from a fallen enemy",
            "Set of bone dice or a deck of playing cards",
            "Common clothes",
            "Belt pouch with 10 gp"
        ]
        self.features = ["Specialty", "Military Rank"]