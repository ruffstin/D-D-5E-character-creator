# outlander.py
from .background import Background
from item import Item

class Outlander(Background):
    def __init__(self):
        super().__init__("Outlander")
        self.skills = {"Athletics", "Survival"}
        self.inventory = {
            "Staff": (Item("Staff", "A sturdy staff."), 1),
            "Hunting Trap": (Item("Hunting Trap", "A trap for catching animals."), 1),
            "Trophy": (Item("Trophy", "A trophy from an animal you killed."), 1),
            "Traveler's Clothes": (Item("Traveler's Clothes", "A set of traveler's clothes."), 1),
            "Pouch": (Item("Pouch", "A belt pouch for coins or trinkets."), 1)
        }
        self.currency = 10
        self.features = ["Origin", "Wanderer"]
        self.tools_proficient = {"Musical Instrument"}
        self.num_languages = 1