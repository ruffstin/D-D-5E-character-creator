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
        race_choice = input("Choose a race (Elf, Tiefling): ").strip()
        if race_choice.lower() == "elf":
            subrace = input("Choose a subrace (High Elf, Wood Elf, Dark Elf): ").strip()
            race = Elf(subrace)
        elif race_choice.lower() == "tiefling":
            race = Tiefling()
        else:
            print("Unknown race selected. Defaulting to Elf (High Elf).")
            race = Elf("High Elf")

        # Class selection
        class_choice = input("Choose a class (Fighter, Wizard): ").strip()
        class_chosen = class_choice.lower()
        if class_chosen.lower() == "fighter":
            char_class = Fighter()
        else:
            char_class = Wizard()

        # Background selection
        background_choice = input("Choose a background (Acolyte, Soldier): ").strip()
        if background_choice.lower() == "acolyte":
            background = Acolyte()
        else:
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
        if another != "yes" or another != "y":
            creating_char = False
            print("=== Thank you for using the D&D 5E Character Creator! ===")
    

if __name__ == "__main__":
    main()