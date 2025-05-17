# outlander.py
from .background import Background

class Outlander(Background):
    def __init__(self):
        super().__init__("Outlander")
        self.skills = {"Athletics", "Survival"}
        self.items = [
            "A staff",
            "A hunting trap",
            "A trophy from an animal you killed",
            "A set of traveler's clothes",
            "A belt pouch containing 10 gp"
        ]

