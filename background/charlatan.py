# charlatan.py
from .background import Background

class Charlatan(Background):
    def __init__(self):
        super().__init__("Charlatan")
        self.skills = {"Deception", "Sleight of Hand"}
        self.items = [
            "Fine clothes",
            "disguise kit",
            "Tools of the con of your choice",
            "Belt pouch with 15 gp"
        ]
        self.features = ["Favorite Schemes", "False Identity"]
        self.tools_proficient = {"Disguise kit", "Forgery kit"}
