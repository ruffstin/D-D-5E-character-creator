# sage.py
from .background import Background
from item import Item

class Sage(Background):
    def __init__(self):
        super().__init__("Sage")
        self.skills = {"Arcana", "History"}
        self.inventory = {
            "Black Ink": (Item("Black Ink", "A bottle of black ink."), 1),
            "Quill": (Item("Quill", "A writing quill."), 1),
            "Small Knife": (Item("Small Knife", "A small knife."), 1),
            "Letter": (Item("Letter", "A letter from a dead colleague posing a question."), 1),
            "Common Clothes": (Item("Common Clothes", "A set of common clothes."), 1),
            "Pouch": (Item("Pouch", "A belt pouch for coins or trinkets."), 1)
        }
        self.currency = 10
        self.features = ["Specialty", "Researcher"]
        self.num_languages = 2