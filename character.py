# character.py
# a character has a race, class, background, stats, features, skills/saving throws, 
# and inventory
# features include proficiencies, languages, and abilities

STAT_NAMES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
ALL_SKILLS = [
    "Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception",
    "History", "Insight", "Intimidation", "Investigation", "Medicine",
    "Nature", "Perception", "Performance", "Persuasion", "Religion",
    "Sleight of Hand", "Stealth", "Survival"
]

from race.race import Race
from background.background import Background
from char_class.char_class import CharClass

class Character:    
    def __init__(self, name: str, stats: list[int], char_class: CharClass, race: Race, 
                 background: Background, level: int = 1):
        if len(stats) != 6:
            raise ValueError("Stats list must contain exactly 6 integers (STR, DEX, CON, INT, WIS, CHA)")
        if level < 1 or level > 20:
            raise ValueError("Level must be between 1 and 20")
        


        self.name = name
        self.stats = stats  # Should be in STR, DEX, CON, INT, WIS, CHA order
        self.alignment = "" # implement the 9 alignments
        self.char_class = char_class 
        self.race = race
        self.stats = self.race.apply_racial_bonuses(self.stats)
        self.background = background
        self.level = level
        self.exp = 0

        #self.currency = {"gold": 0, "silver": 0, "copper": 0, "electrum": 0, "platinum": 0}
        self.items = []
        
        self.features: list[str] =  []
        self.maxhp = 0
        self.currhp = 0
        #self.hit_die = {}  # implement hit dice
        self.temphp = 0
        self.speed = 0
        self.armor_class = 0
        self.inspiration = "none"

        self.proficiency_bonus = Character.get_proficiency_bonus(self.level)
        self.skills_proficient: set[str] = set()
        self.skills_expert: set[str] = set()
        self.saving_throws_proficient: set[str] = set()

        self.other_proficiencies: set[str] = set() # tools and items
        self.languages: set[str] = set()

        self.personality_traits: set[str] = set()
        self.ideals: set[str] = set()
        self.bonds: set[str] = set()
        self.flaws: set[str] = set()
        
        self.spell_casting_class = None
        self.spell_casting_ability = None
        self.spell_slots = {"1st": 0, "2nd": 0, "3rd": 0, "4th": 0, "5th": 0, "6th": 0, "7th": 0, "8th": 0, "9th": 0}
        self.cantrips_known: set[str] = set()
        self.spells_known: set[str] = set()
        self.spell_save_dc = 0
        self.spell_attack_bonus = 0
        self.spell_slots_used = {"1st": 0, "2nd": 0, "3rd": 0, "4th": 0, "5th": 0, "6th": 0, "7th": 0, "8th": 0, "9th": 0}
        
        self.size = "" # small, medium, large
        self.age = 0
        self.height = 0
        self.weight = 0
        self.appearance = ""
        self.eyes = ""
        self.skin = ""
        self.hair = ""
        
        self.apply_racial_features()  
        self.apply_background_features()
        self.apply_class_features()
        self.passive_perception = 10 + self.get_skill_bonus("Perception") #update with level up
        # self.attacks: set[str] = set() # implement attacks
        self.deathsaves = {"success": 0, "failure": 0}
        self.exhaustion = 0
        self.initiative = stats[1] // 2 - 5 # DEX mod, update with level up

    def get_proficiency_bonus(level: int) -> int:
        if level < 5:
            return 2
        elif level < 9:
            return 3
        elif level < 13:
            return 4
        elif level < 17:
            return 5
        else:
            return 6
    
    def apply_racial_features(self):
         if self.race:
            self.languages.update(self.race.get_languages())
            self.speed = self.race.get_speed()
            self.features.extend(self.race.get_features())
            for skill in self.race.get_skills():
                self.skills_proficient.add(skill)
            self.size = self.race.size
            # Apply tool proficiencies

    def apply_background_features(self):
        if self.background:
            # Apply skill proficiencies
            for skill in self.background.get_skills():
                self.skills_proficient.add(skill)
                # self.skills_expert.add(skill)  # for expertise note for later
            
            # Apply features
            self.features.extend(self.background.get_features())
            
            # Apply items
            self.items.extend(self.background.get_items())
            
            # Apply languages
            # Apply tool proficiencies

    def apply_class_features(self):
        if self.char_class:
            # Apply saving throw proficiencies
            for stat in STAT_NAMES:
                self.saving_throws_proficient.add(stat)

            # Apply skill proficiencies
            for skill in self.char_class.skills_proficient:
                self.skills_proficient.add(skill) # implement choices
                # self.skills_expert.add(skill)  # for expertise note for later

            # Apply features
            self.features.extend(self.char_class.get_features())

            # Apply items
            self.items.extend(self.char_class.get_items())
    
    def is_proficient(self, skill: str) -> bool:
        return skill in self.skills_proficient

    def has_expertise(self, skill: str) -> bool:
        return skill in self.skills_expert

    def get_skill_bonus(self, skill: str) -> int:
        # Match skill to the associated stat
        skill_to_stat = {
            "Athletics": "STR",
            "Acrobatics": "DEX", "Sleight of Hand": "DEX", "Stealth": "DEX",
            "Arcana": "INT", "History": "INT", "Investigation": "INT",
            "Nature": "INT", "Religion": "INT",
            "Animal Handling": "WIS", "Insight": "WIS", "Medicine": "WIS",
            "Perception": "WIS", "Survival": "WIS",
            "Deception": "CHA", "Intimidation": "CHA", "Performance": "CHA",
            "Persuasion": "CHA"
            }
        stat = skill_to_stat.get(skill)
            
        if stat is None:
            return 0

        stat_index = STAT_NAMES.index(stat)
        stat_value = self.stats[stat_index]
        stat_bonus = (stat_value // 2) - 5

        bonus = stat_bonus

        if self.has_expertise(skill):
            bonus += 2 * self.proficiency_bonus
            
        elif self.is_proficient(skill):
            bonus += self.proficiency_bonus

        return bonus
    
    def level_up(self):
        if self.level < 20:
            self.level += 1
            # Increase hit die, hit points
            # self.char_class.level_up() # implement in char_class for class features
            # or in race for racial features
            # update prof bonus

        # with multi-classing, need to know which class to level up
    def print_essentials (self):
        print(f"Name: {self.name}")
        print(f"Class: {self.char_class.name} Level {self.level}") #implement adding subclass
        print(f"Race: {self.race.description()}")
        print(f"Background: {self.background}")
        #print(f"Alignment: {self.alignment}")
        print(f"Speed: {self.speed}")
        print("Stats:")
        for i, stat in enumerate(STAT_NAMES):
            stat_value = self.stats[i]
            stat_bonus = (stat_value // 2) - 5
            print(f"  {stat}: {stat_value:2} ({stat_bonus:+2})")

    def print_skills_and_saves(self):
        print("Saving Throws:") # Edit to show full name of stat
        for stat, value in zip(STAT_NAMES, self.stats):
            bonus = value // 2 - 5
            if stat in self.char_class.get_proficient_saving_throws():
                bonus += self.proficiency_bonus
                print(f"  {stat:<16}: {bonus:+2} *")
            else:
                print(f"  {stat:<16}: {bonus:+2}")

        print("Skills:")
        for skill in ALL_SKILLS:
            bonus = self.get_skill_bonus(skill)
            if self.has_expertise(skill):
                suffix = " **"
            elif self.is_proficient(skill):
                suffix = " *"
            else:
                suffix = ""
            print(f"  {skill:<16}: {bonus:+2}{suffix}")
        #print(f" (* = Proficient, ** = Expertise)")

    def print_items_tool_profs_lang(self):
        print("Equipment:")
        for item in self.items:
            print(f"  - {item}")

        print("Tool Proficiencies:")
        for tool in self.other_proficiencies:
            print(f"  - {tool}")
        
        print("Languages:")
        for lang in self.languages:
            print(f"  - {lang}")
    
    def print_features(self):
        print("Features:")
        for feature in self.features:
            print(f"  - {feature}")
        print() # for visual clarity

    def show_character(self):
        self.print_essentials()
        self.print_skills_and_saves()
        self.print_items_tool_profs_lang() 
        self.print_features()
        #self.print_appearance()
        #self.print_personality()



