# noble.py
from .background import Background

class Noble(Background):
    def __init__(self):
        super().__init__("Noble")
        self.skills = {"History", "Persuasion"}
        self.items = [
            "A set of fine clothes",
            "A signet ring",
            "A scroll of pedigree",
            "A purse containing 25 gp"
        ]

