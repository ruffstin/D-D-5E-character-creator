# acolyte.py
from .background import Background

class Acolyte(Background):
    def __init__(self):
        super().__init__("Acolyte")
        self.skills = {"Insight", "Religion"}
        self.items = [
            "A holy symbol",
            "A prayer book or prayer wheel",
            "5 sticks of incense",
            "Vestments",
            "Common clothes",
            "Belt pouch with 15 gp"
        ]
