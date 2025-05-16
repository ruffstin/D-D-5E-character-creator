from character import Character
from race import Elf, Dwarf, Halfling, Human, Dragonborn, Gnome, Half_Elf, Half_Orc, Tiefling

def main():
    base_stats = [15, 14, 13, 12, 10, 8] # Default stat spread for testing
    my_race = Elf(subrace = "High Elf")
    final_stats = my_race.apply_racial_bonuses(base_stats.copy())

    my_char = Character("Thalindra", final_stats, "Wizard", race = my_race, background = "Sage")
    #my_char.show_character()
        
        
    my_char = Character("Thali", final_stats, "Fighter", race = my_race, background = "Soldier")


    my_race2 = Dwarf(subrace = "Mountain Dwarf")
    final_stats2 = my_race2.apply_racial_bonuses(base_stats.copy())
    my_char2 = Character("Bruenor", final_stats2, "Fighter", my_race2, "Soldier")
    #my_char2.show_character()

    my_race3 = Halfling(subrace = "Lightfoot Halfling")
    my_char3 = Character("Frodo", my_race3.apply_racial_bonuses(base_stats.copy()), 
                         "Rogue", my_race3, "Outlander")
    #my_char3.show_character()

    my_race = Human()
    my_char = Character("Bob", my_race.apply_racial_bonuses(base_stats.copy()), "Fighter", my_race, "Soldier")
    #my_char.show_character()

    my_char2 = Character("Lenora", my_race.apply_racial_bonuses(base_stats.copy()), "Cleric", my_race, "Acolyte")
    #my_char2.show_character()

    my_race = Dragonborn(subrace = "Gold Dragonborn")
    my_char = Character("Ryder", my_race.apply_racial_bonuses(base_stats.copy()), "Paladin", my_race, "Noble")
    #my_char.show_character()

    my_race = Gnome(subrace = "Forest Gnome")
    my_char = Character("Gimble", my_race.apply_racial_bonuses(base_stats.copy()), "Bard", my_race, "Entertainer")
    #my_char.show_character()

    my_race = Half_Elf()
    my_char = Character("Elandra", my_race.apply_racial_bonuses(base_stats.copy()), "Sorcerer", my_race, "Charlatan")
    #my_char.show_character()

    my_race = Half_Orc()
    my_char = Character("Grom", my_race.apply_racial_bonuses(base_stats.copy()), "Barbarian", my_race, "Criminal")
    #my_char.show_character()

    my_race = Tiefling()
    my_char = Character("Zara", my_race.apply_racial_bonuses(base_stats.copy()), "Warlock", my_race, "Urchin")
    #my_char.show_character()

if __name__ == "__main__":
    main()