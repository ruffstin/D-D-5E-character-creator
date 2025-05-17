# sage.py
from .background import Background

class Sage(Background):
    def __init__(self):
        super().__init__("Sage")
        self.skills = {"Arcana", "History"}
        self.items = [
            "A bottle of black ink",
            "A quill",
            "A small knife",
            "A letter from a dead colleague posing a question you have not yet been able to answer",
            "A set of common clothes",
            "A belt pouch containing 10 gp"
        ]
