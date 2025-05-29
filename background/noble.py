# noble.py
from .background import Background
from item import Item

class Noble(Background):
    def __init__(self):
        super().__init__("Noble")
        self.skills = {"History", "Persuasion"}
        self.inventory = {
            "Fine Clothes": (Item("Fine Clothes", "A set of fine clothes."), 1),
            "Signet Ring": (Item("Signet Ring", "A ring bearing your family's crest."), 1),
            "Scroll of Pedigree": (Item("Scroll of Pedigree", "Proof of your noble lineage."), 1),
            "Pouch": (Item("Pouch", "A purse for coins."), 1)
        }
        self.currency = 25
        self.features = ["Position of Privilege"]
        self.languages = {"One of your choice"}
        self.tools_proficient = {"One gaming set of your choice"}