# folk_hero.py
from .background import Background

class Folk_Hero(Background):
    def __init__(self):
        super().__init__("Folk Hero")
        self.skills = {"Animal Handling", "Survival"}
        self.items = [
            "Set of artisan's tools (one of your choice)",
            "A shovel",
            "An iron pot",
            "A set of common clothes",
            "A belt pouch containing 10 gp"
        ]
        self.features = ["Defining Event", "Rustic Hospitality"]
        self.tools_proficient = {"One type of artisan's tools", "Vehicles (land)"}
        