from character import Character
from race import Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, HalfElf, HalfOrc, Tiefling
from background import Acolyte, Charlatan, Criminal, Entertainer, Folk_Hero, Guild_Artisan, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin
from char_class import Artificer, Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard

def main():
    base_stats = [15, 14, 13, 12, 10, 8] # Default stat spread for testing

    my_char = Character("Thalindra", base_stats, Wizard(level = 1, subclass = "Evocation"), Elf(subrace = "High Elf"), Sage())
    my_char.show_character()

    my_race = Elf(subrace = "Drow")
    my_background = Soldier()
    my_char = Character("Thali", base_stats, Druid(level = 1), 
                        race = my_race, background = my_background)
    my_char.show_character()

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

if __name__ == "__main__":
    main()