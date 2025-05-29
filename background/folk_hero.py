# folk_hero.py
from .background import Background
from item import Item

class Folk_Hero(Background):
    def __init__(self):
        super().__init__("Folk Hero")
        self.skills = {"Animal Handling", "Survival"}
        self.inventory = {
            "Artisan's Tools": (Item("Artisan's Tools", "A set of artisan's tools (one of your choice)."), 1),
            "Shovel": (Item("Shovel", "A sturdy shovel."), 1),
            "Iron Pot": (Item("Iron Pot", "A simple iron pot."), 1),
            "Common Clothes": (Item("Common Clothes", "A set of common clothes."), 1),
            "Pouch": (Item("Pouch", "A belt pouch for coins or trinkets."), 1)
        }
        self.currency = 10
        self.features = ["Defining Event", "Rustic Hospitality"]
        self.tools_proficient = {"One type of artisan's tools", "Vehicles (land)"}
        