# charlatan.py
from .background import Background
from item import Item

class Charlatan(Background):
    def __init__(self):
        super().__init__("Charlatan")
        self.skills = {"Deception", "Sleight of Hand"}
        self.inventory = {
            "Fine Clothes": (Item("Fine Clothes", "Expensive, stylish clothing."), 1),
            "Disguise Kit": (Item("Disguise Kit", "A kit for creating disguises."), 1),
            "Tools of the Con": (Item("Tools of the Con", "Tools for your chosen con."), 1),
            "Pouch": (Item("Pouch", "A small belt pouch for coins or trinkets."), 1)
        }
        self.currency = 15
        self.features = ["Favorite Schemes", "False Identity"]
        self.tools_proficient = {"Disguise kit", "Forgery kit"}
