# acolyte.py
from .background import Background
from item import Item

class Acolyte(Background):
    def __init__(self):
        super().__init__("Acolyte")
 
        self.skills = {"Insight", "Religion"}
        self.inventory = {
            "Holy Symbol": (Item("Holy Symbol", "A symbol of your faith."), 1),
            "Prayer Book": (Item("Prayer Book", "A book or wheel for prayers."), 1),
            "Incense": (Item("Incense", "Stick of incense."), 5),
            "Vestments": (Item("Vestments", "Religious clothing."), 1),
            "Common Clothes": (Item("Common Clothes", "Simple everyday clothing."), 1),
            "Pouch": (Item("Pouch", "A small belt pouch for coins or trinkets."), 1)

        }
        self.currency = 15
        self.features = ["Shelter of the Faithful"]
        self.num_languages = 2
    
