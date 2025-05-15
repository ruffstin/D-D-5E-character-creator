# character.py
# a character has a race, class, background, stats, features, skills/saving throws, 
# and an inventory
# features include proficiencies, languages, and abilities

STAT_NAMES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
from race.race import Race

class Character:    
    def __init__(self, name: str, stats: list[int], char_class: str, race: Race, background: str):
        if len(stats) != 6:
            raise ValueError("Stats list must contain exactly 6 integers (STR, DEX, CON, INT, WIS, CHA)")
        
        self.name = name
        self.stats = stats  # Should be in STR, DEX, CON, INT, WIS, CHA order
        self.char_class = char_class 
        self.race = race
        self.background = background

    def show_character(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.char_class}")
        print(f"Race: {self.race.description()}")
        print(f"Background: {self.background}")
        print("Stats:")
        for i, stat in enumerate(STAT_NAMES):
            print(f"  {stat}: {self.stats[i]}")