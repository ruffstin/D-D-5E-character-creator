# criminal.py 
from .background import Background

class Criminal(Background):
    def __init__(self):
        super().__init__("Criminal")
        self.skills = {"Deception", "Stealth"}
        self.items = [
            "Crowbar",
            "Set of dark common clothes including a hood",
            "Belt pouch with 15 gp"
        ]
        self.features = ["Criminal Specialty", "Criminal Contact"]
        self.tools_proficient = {"One gaming set", "Thieves' tools"}
