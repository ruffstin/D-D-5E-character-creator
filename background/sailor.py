# sailor.py
from .background import Background

class Sailor(Background):
    def __init__(self):
        super().__init__("Sailor")
        self.skills = {"Athletics", "Perception"}
        self.items = [
            "A belaying pin (club)",
            "50 feet of silk rope",
            "A lucky charm (a rabbit's foot, a small stone with a hole in it, or a similar token)",
            "A set of common clothes",
            "A belt pouch containing 10 gp",
        ]
