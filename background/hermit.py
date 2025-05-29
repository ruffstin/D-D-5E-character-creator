# Hermit.py
from .background import Background
from item import Item

class Hermit(Background):
    def __init__(self):
        super().__init__("Hermit")
        self.skills = {"Medicine", "Religion"}
        self.inventory = {
            "Scroll Case": (Item("Scroll Case", "Stuffed full of notes."), 1),
            "Winter Blanket": (Item("Winter Blanket", "A warm blanket."), 1),
            "Common Clothes": (Item("Common Clothes", "A set of common clothes."), 1),
            "Herbalism Kit": (Item("Herbalism Kit", "A kit for making herbal remedies."), 1),
            "Pouch": (Item("Pouch", "A belt pouch for coins or trinkets."), 1)
        }
        self.currency = 5
        self.features = ["Life of Seclusion", "Discovery"]
        self.tools_proficient = {"Herbalism kit"}
        self.languages = {"One of your choice"}