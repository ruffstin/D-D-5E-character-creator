#Beta design of a character class generator for D&D 5e

import random

#constants 
STAT_NAMES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
CLASSES = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
           "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
RACES = ["Human", "Elf", "Dwarf", "Halfling", "Dragonborn", "Gnome", "Half-Orc", "Tiefling"]
BACKGROUNDS = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermit"
            "Noble", "Outlander", "Sage", "Sailor," "Soldier", "Urchin"]

# Function to roll 4d6 and drop the lowest
def roll_stat():
    return sum(sorted([random.randint(1, 6) for _ in range(4)])[1:])

class Character:
    def __init__(self, name, race, char_class, background, stats=None):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.background = background
        self.stats = stats or self.generate_stats()

    def generate_stats(self):
        return {stat: roll_stat() for stat in STAT_NAMES}

    def display(self):
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.char_class}")
        print(f"Background: {self.background}")
        print("Stats:")
        for stat, val in self.stats.items():
            print(f"  {stat}: {val}")

# Create a random but viable character
def create_random_character(viable=True):
    name = "Adventurer_" + str(random.randint(1000, 9999))
    race = random.choice(RACES)
    char_class = random.choice(CLASSES)
    background = random.choice(BACKGROUNDS)
    stats = {stat: roll_stat() for stat in STAT_NAMES}

    if viable:
        # Slightly boost key stats based on class
        key_stat = {
            "Artificer": "INT", "Barbarian": "STR", "Fighter": "STR", 
            "Paladin": "CHA", "Rogue": "DEX", "Monk": "DEX", "Ranger": "DEX",
            "Wizard": "INT", "Sorcerer": "CHA", "Warlock": "CHA",
            "Cleric": "WIS", "Druid": "WIS", "Bard": "CHA"
        }[char_class]
        stats[key_stat] = max(stats[key_stat], 14)

    return Character(name, race, char_class, background, stats)

def main():
    print("Creating a random viable character:\n")
    char = create_random_character(viable=True)
    char.display()

if __name__ == "__main__":
    main()