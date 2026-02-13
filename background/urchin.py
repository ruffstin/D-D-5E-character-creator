# urchin.py
from .background import Background
from item import Item

class Urchin(Background):
    def __init__(self):
        super().__init__("Urchin")
        self.skills = {"Sleight of Hand", "Stealth"}
        self.inventory = {
            "Small Knife": (Item("Small Knife", "A small knife."), 1),
            "City Map": (Item("City Map", "A map of the city you grew up in."), 1),
            "Pet Mouse": (Item("Pet Mouse", "A pet mouse."), 1),
            "Common Clothes": (Item("Common Clothes", "A set of common clothes."), 1),
            "Pouch": (Item("Pouch", "A belt pouch for coins or trinkets."), 1)
        }
        self.currency = 10
        self.features = ["City Secrets"]
        self.tools_proficient = {"Disguise Kit", "Thieves' Tools"}