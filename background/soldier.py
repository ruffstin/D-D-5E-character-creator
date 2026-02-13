# soldier.py
from .background import Background
from item import Item

class Soldier(Background):
    def __init__(self):
        super().__init__("Soldier")
        self.skills = {"Athletics", "Intimidation"}
        self.inventory = {
            "Insignia of Rank": (Item("Insignia of Rank", "Your military insignia."), 1),
            "Trophy": (Item("Trophy", "A trophy from a fallen enemy."), 1),
            "Gaming Set": (Item("Gaming Set", "Bone dice or a deck of playing cards."), 1),
            "Common Clothes": (Item("Common Clothes", "A set of common clothes."), 1),
            "Pouch": (Item("Pouch", "A belt pouch for coins or trinkets."), 1)
        }
        self.currency = 10
        self.features = ["Specialty", "Military Rank"]
        self.tools_proficient = {"Gaming Set", "Vehicles (land)"} # 1 gaming set and one land vehicle