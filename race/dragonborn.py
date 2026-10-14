# dragonborn.py
from .race import Race

class Dragonborn(Race):
    SUBRACES = {
        "Gold Dragonborn": "",
        "Silver Dragonborn": "",
        "Brass Dragonborn": "",
        "Bronze Dragonborn": "",
        "Copper Dragonborn": "",
        "Black Dragonborn": "",
        "Blue Dragonborn": "",
        "Green Dragonborn": "",
        "Red Dragonborn": "",
        "White Dragonborn": ""
    }

    def __init__(self, subrace: str = "Gold Dragonborn"):
        super().__init__("Dragonborn", subrace)
       
        # -----------------------------
        # Languages
        # -----------------------------
        self.add_language("Common")
        self.add_language("Draconic")

        # All dragonborn get +2 STR and +1 CHA
        self.bonuses = {"STR": 2, "CHA": 1}
        self.set_features()

    def set_features(self):

        ancestry_map = {
            "Gold Dragonborn": ("Fire",),
            "Red Dragonborn": ("Fire",),
            "Brass Dragonborn": ("Fire",),

            "Silver Dragonborn": ("Cold",),
            "White Dragonborn": ("Cold",),

            "Blue Dragonborn": ("Lightning",),
            "Bronze Dragonborn": ("Lightning",),

            "Black Dragonborn": ("Acid",),
            "Copper Dragonborn": ("Acid",),

            "Green Dragonborn": ("Poison",),
        }

        damage_type = ancestry_map.get(self.subrace, ("Fire",))[0]

        self.features = {
            f"{self.subrace} Ancestry": "", 
            f"Breath Weapon ({damage_type})": "",
            f"Damage Resistance ({damage_type})": ""
        }
    