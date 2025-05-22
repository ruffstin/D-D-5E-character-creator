# entertainer.py
from .background import Background

class Entertainer(Background):
    def __init__(self):
        super().__init__("Entertainer")
        self.skills = {"Acrobatics", "Performance"}
        self.items = [
            "Musical instrument of your choice",
            "the favor of an admirer",
            "a costume",
            "a belt pouch containing 15 gp"
        ]
        self.features = ["Entertainer Routines", "By Popular Demand"]
        self.tools_proficient = {"Disguise kit", "Musical instrument (one of your choice)"}