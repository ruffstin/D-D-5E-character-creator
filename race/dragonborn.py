# dragonborn.py
from .race import Race

class Dragonborn(Race):
    def __init__(self, subrace: str = "Gold Dragonborn"):
        super().__init__("Dragonborn", subrace)
        self.features = ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"]
        self.set_bonuses()
        self.languages = ["Common", "Draconic"]

    def set_bonuses(self):
        # All dragonborn get +2 STR and +1 CHA
        self.bonuses = {"STR": 2, "CHA": 1}

        if self.subrace == "Gold Dragonborn":
            self.features = ["Gold Dragon Ancestry", "Breath Weapon (Fire):", 
                             "Damage Resistance (Fire)"]
        
        elif self.subrace == "Silver Dragonborn":
            self.features = ["Silver Dragon Ancestry", "Breath Weapon (Cold):", 
                             "Damage Resistance (Cold)"]
        
        elif self.subrace == "Brass Dragonborn":
            self.features = ["Brass Dragon Ancestry", "Breath Weapon (Fire):", 
                             "Damage Resistance (Fire)"]

        elif self.subrace == "Bronze Dragonborn":
            self.features = ["Bronze Dragon Ancestry", "Breath Weapon (Lightning):", 
                             "Damage Resistance (Lightning)"]
        
        elif self.subrace == "Copper Dragonborn":
            self.features = ["Copper Dragon Ancestry", "Breath Weapon (Acid):", 
                             "Damage Resistance (Acid)"]
        
        elif self.subrace == "Black Dragonborn":
            self.features = ["Black Dragon Ancestry", "Breath Weapon (Acid):", 
                             "Damage Resistance (Acid)"]
        
        elif self.subrace == "Blue Dragonborn":
            self.features = ["Blue Dragon Ancestry", "Breath Weapon (Lightning):", 
                             "Damage Resistance (Lightning)"]
            
        elif self.subrace == "Green Dragonborn":
             self.features = ["Green Dragon Ancestry", "Breath Weapon (Poison):", 
                             "Damage Resistance (Poison)"]
        
        elif self.subrace == "Red Dragonborn":
            self.features = ["Red Dragon Ancestry", "Breath Weapon (Fire):", 
                             "Damage Resistance (Fire)"]
        
        elif self.subrace == "White Dragonborn":
            self.features = ["White Dragon Ancestry", "Breath Weapon (Cold):", 
                             "Damage Resistance (Cold)"]      
        # else: no additional bonuses
    