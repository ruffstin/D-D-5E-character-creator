from character import Character
from race import Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, HalfElf, HalfOrc, Tiefling
from background import Acolyte, Charlatan, Criminal, Entertainer, Folk_Hero, Guild_Artisan, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin
from char_class import Fighter #Artificer, Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard

def main():
    base_stats = [15, 14, 13, 12, 10, 8] # Default stat spread for testing
    
    my_race = Elf(subrace = "High Elf")
    final_stats = my_race.apply_racial_bonuses(base_stats.copy())

    # my_background = Soldier()
    # my_char = Character("Thali", final_stats, "Fighter", race = my_race, background = my_background)
    # my_char.show_character()

    # my_background = Sage()
    # my_char = Character("Thalindra", final_stats, "Wizard", my_race, my_background)
    # my_char.show_character()

    # my_race = Human()
    # my_background = Acolyte()
    # my_char2 = Character("Lenora", my_race.apply_racial_bonuses(base_stats.copy()), "Cleric", my_race, my_background)
    # my_char2.show_character()

    # my_race = HalfElf()
    # my_background = Charlatan()
    # my_char = Character("Elandra", my_race.apply_racial_bonuses(base_stats.copy()), "Sorcerer", my_race, my_background)
    # my_char.show_character()

    # my_race = HalfOrc()
    # my_background = Criminal()
    # my_char = Character("Grom", my_race.apply_racial_bonuses(base_stats.copy()), "Barbarian", my_race, my_background)
    # my_char.show_character()

    # my_race = Gnome(subrace = "Forest Gnome")
    # my_background = Entertainer()
    # my_char = Character("Gimble", my_race.apply_racial_bonuses(base_stats.copy()), "Bard", my_race, my_background)
    # my_char.show_character()

    # my_race2 = Dwarf(subrace = "Mountain Dwarf")
    # final_stats2 = my_race2.apply_racial_bonuses(base_stats.copy())
    # my_background2 = Folk_Hero()
    # my_char2 = Character("Bruenor", final_stats2, "Fighter", my_race2, my_background2)
    # my_char2.show_character()

    # my_race3 = Halfling(subrace = "Lightfoot Halfling")
    # my_background3 = Outlander()
    # my_char3 = Character("Frodo", my_race3.apply_racial_bonuses(base_stats.copy()), 
    #                      "Rogue", my_race3, my_background3)
    # my_char3.show_character()

    # my_race = Human()
    # my_background = Guild_Artisan()
    # my_char = Character("Bob", my_race.apply_racial_bonuses(base_stats.copy()), "Fighter", my_race, my_background)
    # my_char.show_character()

    my_race = Dragonborn(subrace = "Gold Dragonborn")
    my_background = Noble()
    my_char = Character("Ryder", my_race.apply_racial_bonuses(base_stats.copy()), "Paladin", my_race, my_background)
    my_char.show_character()

    my_race = Tiefling()
    my_background = Urchin()
    my_char = Character("Zara", my_race.apply_racial_bonuses(base_stats.copy()), "Warlock", my_race, my_background)
    my_char.show_character()

if __name__ == "__main__":
    main()