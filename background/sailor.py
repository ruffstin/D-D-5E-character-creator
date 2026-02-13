# sailor.py
from .background import Background
from item import Item

class Sailor(Background):
    def __init__(self):
        super().__init__("Sailor")
        self.skills = {"Athletics", "Perception"}
        self.inventory = {
            "Belaying Pin": (Item("Belaying Pin", "A club used on ships."), 1),
            "Silk Rope": (Item("Silk Rope", "50 feet of silk rope."), 1),
            "Lucky Charm": (Item("Lucky Charm", "A rabbit's foot, stone, or similar token."), 1),
            "Common Clothes": (Item("Common Clothes", "A set of common clothes."), 1),
            "Pouch": (Item("Pouch", "A belt pouch for coins or trinkets."), 1)
        }
        self.currency = 10
        self.features = ["Ship's Passage"]
        self.tools_proficient = {"Navigator's Tools", "Vehicles (water)"}