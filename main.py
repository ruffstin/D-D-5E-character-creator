from character import Character
from race import Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, HalfElf, HalfOrc, Tiefling
from background import Acolyte, Charlatan, Criminal, Entertainer, Folk_Hero, Guild_Artisan, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin
from char_class import Artificer, Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard

def main():
    base_stats = [15, 14, 13, 12, 10, 8] # Default stat spread for testing

    my_char = Character("Thalindra", base_stats, Wizard(level = 1, subclass = "Evocation"), Elf(subrace = "High Elf"), Sage())
    #my_char.show_character()

    my_race = Elf(subrace = "Drow")
    my_background = Soldier()
    my_char = Character("Thali", base_stats, Druid(level = 1), 
                        race = my_race, background = my_background)
    #my_char.show_character()

    my_char2 = Character("Lenora", base_stats, Cleric(1), Human(), Acolyte())
    #my_char2.show_character()

    my_char = Character("Elandra", base_stats, Sorcerer(), HalfElf(), Charlatan())
    #my_char.show_character()

    my_char = Character("Grom", base_stats, Barbarian(level = 1, subclass = "Berserker"), 
                        HalfOrc(), Criminal())
    #my_char.show_character()

    my_race = Gnome(subrace = "Forest Gnome")
    my_background = Entertainer()
    my_char = Character("Gimble", base_stats, Bard(level = 1), my_race, my_background)
    #my_char.show_character()

    my_char2 = Character("Bruenor", base_stats, Fighter(1), Dwarf(subrace = "Mountain Dwarf"), 
                         Folk_Hero())
    #my_char2.show_character()

    my_char3 = Character("Frodo", base_stats, Rogue(), Halfling(), Outlander())
    #my_char3.show_character()

    my_char = Character("Bob", base_stats, Ranger(), Human(), Guild_Artisan())
    #my_char.show_character()

    my_char = Character("Ryder", base_stats, Paladin(), Dragonborn(subrace = "Gold Dragonborn"),  Noble())
    #my_char.show_character()

    my_char = Character("Zara", base_stats, Warlock(level = 1), Tiefling(), Urchin())
    #my_char.show_character()

    my_char = Character("Seraphina", base_stats, Artificer(level = 1, subclass = "Armorer"), 
                        Dragonborn(subrace = "Silver Dragonborn"), Hermit())
    #my_char.show_character()

    my_char = Character("Pollo", base_stats, Monk(1), Dragonborn(subrace = "Copper Dragonborn"), Sailor())
    #my_char.show_character()

    print("=== Welcome to the D&D 5E Character Creator ===")

    creating_char = True
    while creating_char:
        # Name
        name = input("Enter your character's name: ")

        # Race selection
        race_choice = input("Choose a race (Dwarf Elf, Halfling, Human, Dragonborn, Gnome, Half Elf, Half Orc, or Tiefling): ").strip()
        if race_choice.lower() == "dwarf":
            subrace = input("Choose a subrace (Hill Dwarf, Mountain Dwarf): ").strip()
            if subrace.lower() not in ["hill dwarf", "mountain dwarf", "hill", "mountain"]:
                print("Invalid subrace. Defaulting to Hill Dwarf.")
            
            elif subrace.lower() == "hill dwarf" or subrace.lower() == "hill":
                race = Dwarf("Hill Dwarf")
            
            elif subrace.lower() == "mountain dwarf" or subrace.lower() == "mountain":
                race = Dwarf("Mountain Dwarf")

        elif race_choice.lower() == "elf":
            subrace = input("Choose a subrace (High Elf, Wood Elf, Dark Elf (Drow)): ").strip()
            if subrace.lower() not in ["high elf", "wood elf", "dark elf", "drow", "high", "wood", "dark"]:
                print("Invalid subrace. Defaulting to High Elf.")
                race = Elf("High Elf")

            elif subrace.lower() == "high elf" or subrace.lower() == "high":
                race = Elf("High Elf")

            elif subrace.lower() == "wood elf" or subrace.lower() == "wood":
                race = Elf("Wood Elf")

            elif subrace.lower() == "dark elf" or subrace.lower() == "drow" or subrace.lower() == "dark":
                if subrace.lower() == "dark elf" or subrace.lower() == "dark":
                    race = Elf("Dark Elf")
                else: 
                    race = Elf("Drow")
        
        elif race_choice.lower() == "halfling":
            subrace = input("Choose a subrace (Lightfoot Halfling, Stout Halfling): ").strip()
            if subrace.lower() not in ["lightfoot halfling", "stout halfling", "lightfoot", "stout"]:
                print("Invalid subrace. Defaulting to Lightfoot Halfling.")
            
            elif subrace.lower() == "lightfoot halfling" or subrace.lower() == "lightfoot":
                race = Halfling("Lightfoot Halfling")
            
            elif subrace.lower() == "stout halfling" or subrace.lower() == "stout":
                race = Halfling("Stout Halfling")
            
        elif race_choice.lower() == "human":
            race = Human()

        elif race_choice.lower() == "dragonborn":
            subrace = input("Choose a subrace (Gold Dragonborn, Silver Dragonborn, Brass Dragonborn, Bronze Dragonborn, Copper Dragonborn, Black Dragonborn, Blue Dragonborn, Green Dragonborn, Red Dragonborn, White Dragonborn): ").strip()
            if subrace.lower() not in ["gold dragonborn", "silver dragonborn", "brass dragonborn", "bronze dragonborn", "copper dragonborn", "black dragonborn", "blue dragonborn", "green dragonborn", "red dragonborn", "white dragonborn", "gold", "silver", "brass", "bronze", "copper", "black", "blue", "green", "red", "white"]:
                print("Invalid subrace. Defaulting to Gold Dragonborn.")
            
            elif subrace.lower() == "gold dragonborn" or subrace.lower() == "gold":
                race = Dragonborn("Gold Dragonborn")
            
            elif subrace.lower() == "silver dragonborn" or subrace.lower() == "silver":
                race = Dragonborn("Silver Dragonborn")

            elif subrace.lower() == "brass dragonborn" or subrace.lower() == "brass":
                race = Dragonborn("Brass Dragonborn")

            elif subrace.lower() == "bronze dragonborn" or subrace.lower() == "bronze":
                race = Dragonborn("Bronze Dragonborn")

            elif subrace.lower() == "copper dragonborn" or subrace.lower() == "copper":
                race = Dragonborn("Copper Dragonborn")

            elif subrace.lower() == "black dragonborn" or subrace.lower() == "black":
                race = Dragonborn("Black Dragonborn")
            
            elif subrace.lower() == "blue dragonborn" or subrace.lower() == "blue":
                race = Dragonborn("Blue Dragonborn")

            elif subrace.lower() == "green dragonborn" or subrace.lower() == "green":
                race = Dragonborn("Green Dragonborn")

            elif subrace.lower() == "red dragonborn" or subrace.lower() == "red":
                race = Dragonborn("Red Dragonborn")
            
            elif subrace.lower() == "white dragonborn" or subrace.lower() == "white":
                race = Dragonborn("White Dragonborn")

        elif race_choice.lower() == "gnome": 
            subrace = input("Choose a subrace (Forest Gnome, Rock Gnome): ").strip()
            if subrace.lower() not in ["forest gnome", "rock gnome", "forest", "rock"]:
                print("Invalid subrace. Defaulting to Forest Gnome.")
            
            elif subrace.lower() == "forest gnome" or subrace.lower() == "forest":
                race = Gnome("Forest Gnome")
            
            elif subrace.lower() == "rock gnome" or subrace.lower() == "rock":
                race = Gnome("Rock Gnome")

        elif race_choice.lower() == "half elf" or race_choice.lower() == "half-elf" or race_choice.lower() == "halfelf":   
            race = HalfElf()

        elif race_choice.lower() == "half orc" or race_choice.lower() == "half-orc" or race_choice.lower() == "halforc":
            race = HalfOrc()

        elif race_choice.lower() == "tiefling":
            race = Tiefling()
        
        else:
            print("Unknown race selected. Defaulting to Human.")
            race = Human()

        # Class selection
        class_choice = input("Choose a class (Artificer, Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard): ").strip()
        class_chosen = class_choice.lower()
        if class_chosen == "artificer":
            char_class = Artificer()
        
        elif class_chosen == "barbarian":
            char_class = Barbarian()
        
        elif class_chosen == "bard":
            char_class = Bard()
        
        elif class_chosen == "cleric":
            char_class = Cleric()

        elif class_chosen == "druid":
            char_class = Druid()
        
        elif class_chosen.lower() == "fighter":
            char_class = Fighter()
             
        elif class_chosen == "monk":
            char_class = Monk()

        elif class_chosen == "paladin":
            char_class = Paladin()
        
        elif class_chosen == "ranger":
            char_class = Ranger()
        
        elif class_chosen == "rogue":
            char_class = Rogue()

        elif class_chosen == "sorcerer":
            char_class = Sorcerer()

        elif class_chosen == "warlock":
            char_class = Warlock()
        
        elif class_chosen == "wizard":
            char_class = Wizard()

        else:
            print("Unknown class selected. Defaulting to Fighter.")
            char_class = Fighter()

        # Background selection
        background_choice = input("Choose a background (Acolyte, Charlatan, Criminal, Entertainer, Folk_Hero, Guild_Artisan, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin): ").strip()
        if background_choice.lower() == "acolyte":
            background = Acolyte()
        
        elif background_choice.lower() == "charlatan":
            background = Charlatan()

        elif background_choice.lower() == "criminal":
            background = Criminal()

        elif background_choice.lower() == "entertainer":
            background = Entertainer()
        
        elif background_choice.lower() == "folk hero" or background_choice.lower() == "folk-hero" or background_choice.lower() == "folkhero":
            background = Folk_Hero()

        elif background_choice.lower() == "guild artisan" or background_choice.lower() == "guild-artisan" or background_choice.lower() == "guildartisan":
            background = Guild_Artisan()
        
        elif background_choice.lower() == "hermit":
            background = Hermit()
        
        elif background_choice.lower() == "noble":
            background = Noble()

        elif background_choice.lower() == "outlander":
            background = Outlander()
        
        elif background_choice.lower() == "sage":
            background = Sage()
        
        elif background_choice.lower() == "sailor":
            background = Sailor()
        
        elif background_choice.lower() == "soldier":
            background = Soldier()
        
        elif background_choice.lower() == "urchin":
            background = Urchin()
        
        else:
            print("Unknown background selected. Defaulting to Soldier.")
            background = Soldier()

        # Stat input - default to 15, 14, 13, 12, 10, 8 or prompt for random generated stats
        print("You can either use the default stats (15, 14, 13, 12, 10, 8) or enter your own.")
        print("Enter your character’s stats in order: STR, DEX, CON, INT, WIS, CHA")
        try:
            stats_input = input("Enter 6 integers separated by spaces: ")
            stats = list(map(int, stats_input.strip().split()))
            if len(stats) != 6:
                raise ValueError
        except ValueError:
            print("Invalid input. Using default stats: 15 14 13 12 10 8")
            stats = [15, 14, 13, 12, 10, 8]

        # Build character
        character = Character(name, stats, char_class, race, background)

        # Display summary
        print("\n=== Character Summary ===")
        character.show_character()  # Assuming you’ve written this display method

        # Ask if the user wants to create another character
        another = input("Do you want to create another character? (yes/no): ").strip().lower()
        if another != "yes" and another != "y":
            creating_char = False
            print("=== Thank you for using the D&D 5E Character Creator! ===")
    

if __name__ == "__main__":
    main()