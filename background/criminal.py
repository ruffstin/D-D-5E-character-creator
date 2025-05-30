# criminal.py 
from .background import Background
from item import Item

class Criminal(Background):
    def __init__(self):
        super().__init__("Criminal")
        self.skills = {"Deception", "Stealth"}
        self.inventory = {
            "Crowbar": (Item("Crowbar", "A basic tool for prying."), 1),
            "Dark Common Clothes": (Item("Dark Common Clothes", "Set of dark common clothes including a hood."), 1),
            "Pouch": (Item("Pouch", "A small belt pouch for coins or trinkets."), 1)
        }
        self.currency = 15 
        self.features = ["Criminal Specialty", "Criminal Contact"]
        self.tools_proficient = {"One gaming set", "Thieves' tools"}
