from character import Character
from race import Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, HalfElf, HalfOrc, Tiefling
from background import Acolyte, Charlatan, Criminal, Entertainer, Folk_Hero, Guild_Artisan, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin
from char_class import Artificer, Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard
from stats import StatGenerator  

def main():
    base_stats = [15, 14, 13, 12, 10, 8] # Default stat spread for testing

    # my_char = Character("Thalindra", base_stats, Wizard(level = 1, subclass = "Evocation"), Elf(subrace = "High Elf"), Sage())
    # my_char.show_character()

    # my_race = Elf(subrace = "Drow")
    # my_background = Soldier()
    # my_char = Character("Thali", base_stats, Druid(level = 1), race = my_race, background = my_background)
    # my_char.show_character()

    # my_char2 = Character("Lenora", base_stats, Cleric(1), Human(), Acolyte())
    # my_char2.show_character()

    # my_char = Character("Elandra", base_stats, Sorcerer(), HalfElf(), Charlatan())
    # my_char.show_character()

    # my_char = Character("Grom", base_stats, Barbarian(level = 1, subclass = "Berserker"), 
    #                     HalfOrc(), Criminal())
    # my_char.show_character()

    # my_race = Gnome(subrace = "Forest Gnome")
    # my_background = Entertainer()
    # my_char = Character("Gimble", base_stats, Bard(level = 1), my_race, my_background)
    # my_char.show_character()

    # my_char2 = Character("Bruenor", base_stats, Fighter(1), Dwarf(subrace = "Mountain Dwarf"), 
    #                      Folk_Hero())
    # my_char2.show_character()

    # my_char3 = Character("Frodo", base_stats, Rogue(), Halfling(), Outlander())
    # my_char3.show_character()

    # my_char = Character("Bob", base_stats, Ranger(), Human(), Guild_Artisan())
    # my_char.show_character()

    # my_char = Character("Ryder", base_stats, Paladin(), Dragonborn(subrace = "Gold Dragonborn"),  Noble())
    # my_char.show_character()

    # my_char = Character("Zara", base_stats, Warlock(level = 1), Tiefling(), Urchin())
    # my_char.show_character()

    # my_char = Character("Seraphina", base_stats, Artificer(level = 1, subclass = "Armorer"), 
    #                     Dragonborn(subrace = "Silver Dragonborn"), Hermit())
    # my_char.show_character()

    # my_char = Character("Pollo", base_stats, Monk(1), Dragonborn(subrace = "Copper Dragonborn"), Sailor())
    # my_char.show_character()

    print("=== Welcome to the D&D 5E Character Creator ===")

    creating_char = True
    while creating_char:
        # Name
        name = input("Enter your character's name: ")

        # Race selection
        while True: 
            race_choice = input("Choose a race (Dwarf Elf, Halfling, Human, Dragonborn, Gnome, Half Elf, Half Orc, or Tiefling): ").strip().lower()
            if race_choice == "dwarf":
                while True:
                    subrace = input("Choose a subrace (Hill Dwarf, Mountain Dwarf): ").strip().lower()

                    if subrace in ["hill dwarf", "hill"]:
                        race = Dwarf("Hill Dwarf")
                        break
                    elif subrace in ["mountain dwarf", "mountain"]:
                        race = Dwarf("Mountain Dwarf")
                        break
                    else:
                        print("Invalid subrace. Please enter 'Hill Dwarf' or 'Mountain Dwarf'.")
                    
                break

            elif race_choice == "elf":
                while True:
                    subrace = input("Choose a subrace (High Elf, Wood Elf, Dark Elf (Drow)): ").strip().lower()
                    
                    if subrace in ["high elf", "high"]:
                        race = Elf("High Elf")
                        break
            
                    elif subrace in ["wood elf", "wood"]:
                        race = Elf("Wood Elf")
                        break
            
                    elif subrace in ["dark elf", "dark"]:
                        race = Elf("Dark Elf")
                        break

                    elif subrace == "drow":
                        race = Elf("Drow")
                        break
                    else:
                        print("Invalid subrace. Please enter 'High Elf', 'Wood Elf', 'Dark Elf'(Drow)")
                break
        
            elif race_choice == "halfling":
                while True:

                    subrace = input("Choose a subrace (Lightfoot Halfling, Stout Halfling): ").strip().lower()
                    
                    if subrace in ["lightfoot halfling", "lightfoot"]:
                        race = Halfling("Lightfoot Halfling")
                        break
                    
                    elif subrace in ["stout halfling", "stout"]:
                        race = Halfling("Stout Halfling")
                        break
                    else:
                        print("Invalid subrace. Please enter 'Lightfoot Halfling' or 'Stout Halfling'.")
                break
            
            elif race_choice == "human":
                race = Human()
                break

            elif race_choice == "dragonborn":
                valid_subraces = {
                    "gold": "Gold Dragonborn",
                    "silver": "Silver Dragonborn",
                    "brass": "Brass Dragonborn",
                    "bronze": "Bronze Dragonborn",
                    "copper": "Copper Dragonborn",
                    "black": "Black Dragonborn",
                    "blue": "Blue Dragonborn",
                    "green": "Green Dragonborn",
                    "red": "Red Dragonborn",
                    "white": "White Dragonborn",
                    "gold dragonborn": "Gold Dragonborn",
                    "silver dragonborn": "Silver Dragonborn",
                    "brass dragonborn": "Brass Dragonborn",
                    "bronze dragonborn": "Bronze Dragonborn",
                    "copper dragonborn": "Copper Dragonborn",
                    "black dragonborn": "Black Dragonborn",
                    "blue dragonborn": "Blue Dragonborn",
                    "green dragonborn": "Green Dragonborn",
                    "red dragonborn": "Red Dragonborn",
                    "white dragonborn": "White Dragonborn"
                }
                while True: 
                    subrace = input("Choose a subrace (Gold, Silver, Brass, Bronze, Copper, Black, Blue, Green, Red, White Dragonborn): ").strip().lower()
                    if subrace in valid_subraces:
                        race = Dragonborn(valid_subraces[subrace])
                        break
                    
                    else:
                        print("Invalid subrace. Please enter a valid Dragonborn subrace.")
                break

            elif race_choice == "gnome": 
                while True: 
                    subrace = input("Choose a subrace (Forest Gnome, Rock Gnome): ").strip().lower()
                    
                    if subrace in ["forest gnome", "forest"]:
                        race = Gnome("Forest Gnome")
                        break
            
                    elif subrace in ["rock gnome", "rock"]:
                        race = Gnome("Rock Gnome")
                        break
                    
                    else:
                        print("Invalid subrace. Please enter 'Forest Gnome' or 'Rock Gnome'.")
                break

            elif race_choice in ["half elf", "half-elf", "halfelf"]:
                race = HalfElf()
                break
    
            elif race_choice in ["half orc", "half-orc", "halforc"]:
                race = HalfOrc()
                break
    
            elif race_choice == "tiefling":
                race = Tiefling()
                break
        
            else:
                print("Unknown race selected. Please enter a valid race.")           

        # Class selection
        class_map = {
            "artificer": Artificer,
            "barbarian": Barbarian,
            "bard": Bard,
            "cleric": Cleric,
            "druid": Druid,
            "fighter": Fighter,
            "monk": Monk,
            "paladin": Paladin,
            "ranger": Ranger,
            "rogue": Rogue,
            "sorcerer": Sorcerer,
            "warlock": Warlock,
            "wizard": Wizard
        }

        while True: 
            class_choice = input("Choose a class (Artificer, Barbarian, Bard, Cleric, Druid, " \
            "Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard): ").strip().lower()

            if class_choice in class_map:
                char_class = class_map[class_choice]()
                break
            else:
                print("Unknown class requested. Please enter a valid class.") 

        # Background selection
        background_map = {
            "acolyte": Acolyte,
            "charlatan": Charlatan,
            "criminal": Criminal,
            "entertainer": Entertainer,
            "folk hero": Folk_Hero,
            "folk-hero": Folk_Hero,
            "folkhero": Folk_Hero,
            "guild artisan": Guild_Artisan,
            "guild-artisan": Guild_Artisan,
            "guildartisan": Guild_Artisan,
            "hermit": Hermit,
            "noble": Noble,
            "outlander": Outlander,
            "sage": Sage,
            "sailor": Sailor,
            "soldier": Soldier,
            "urchin": Urchin
        }

        while True:
            background_choice = input("Choose a background (Acolyte, Charlatan, Criminal, " \
                "Entertainer, Folk Hero, Guild Artisan, Hermit, Noble, Outlander, " \
                "Sage, Sailor, Soldier, Urchin): ").strip().lower()
    
            if background_choice in background_map:
                background = background_map[background_choice]()
                break
            else:
                print("Unknown background selected. Please enter a valid background.") 

        print("Choose a method for stat generation: default / roll / point buy")
        while True:
            method = input("Method: ").strip().lower()
            if method in ["default", "roll", "point buy", "d", "r", "pb"]: 
                stat_gen = StatGenerator(method)
                stats = stat_gen.generate_stats()
                break
            else: 
                print("Invalid method. Please choose 'default', 'roll', or 'point buy'.")
        
        # Build character
        character = Character(name, stats, char_class, race, background)
        
        # Level up?
        while True:
            level = input("Are you level 1? (yes/no) ").strip().lower()
            if level == "yes" or level == "y":
                 print("You are level 1. You can level up later once you get some exp!")
                 break   
            elif level == "no" or level == "n": 
                what_level = True
                while what_level:
                    try: 
                        level = int(input("What level are you? ").strip())       
                        if (level > 20 or level < 1):
                            print("That is not a valid level... try again? ")
                        else: 
                            character.level_up(level)
                            print("You are now level", level)
                            what_level = False

                    except ValueError: 
                        print("Please enter a valid integer between 1 and 20.")
                break
        # Display summary
        print("\n=== Character Summary ===")
        character.show_character()  # Assuming you’ve written this display method

        # Ask if the user wants to create another character
        while True:
            another = input("Do you want to create another character? (yes/no): ").strip().lower()
            if another == "no" or another == "n":
                creating_char = False
                print("=== Thank you for using the D&D 5E Character Creator! ===")
                break
            
            elif another == "yes" or another == "y":
                print("=== Lets make a new character! ===")
                break

if __name__ == "__main__":
    main()