# entertainer.py
from .background import Background
from item import Item

class Entertainer(Background):
    def __init__(self):
        super().__init__("Entertainer")
        self.skills = {"Acrobatics", "Performance"}
        self.skills = {"Acrobatics", "Performance"}
        self.inventory = {
            "Musical Instrument": (Item("Musical Instrument", "An instrument of your choice."), 1),
            "Favor": (Item("Favor", "The favor of an admirer."), 1),
            "Costume": (Item("Costume", "A costume for performances."), 1),
            "Pouch": (Item("Pouch", "A belt pouch for coins or trinkets."), 1)
        }
        self.currency = 15
        self.features = ["Entertainer Routines", "By Popular Demand"]
        self.tools_proficient = {"Disguise kit", "Musical Instrument"}