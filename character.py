# character.py
# a character has a race, class, background, stats, features, skills/saving throws, 
# and an inventory
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

class Character:    
    def __init__(self, name: str, stats: list[int], char_class: str, race: Race, 
                 background: Background, level: int = 1):
        if len(stats) != 6:
            raise ValueError("Stats list must contain exactly 6 integers (STR, DEX, CON, INT, WIS, CHA)")
        
        self.name = name
        self.stats = stats  # Should be in STR, DEX, CON, INT, WIS, CHA order
        self.char_class = char_class 
        self.race = race
        self.background = background
        self.level = level
        self.proficiency_bonus = Character.get_proficiency_bonus(self.level)
        self.skills_proficient: set[str] = set()
        self.skills_expert: set[str] = set()
        self.items = []
        self.apply_background_features()

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
    
    def apply_background_features(self):
        if self.background:
            # Apply skill proficiencies
            for skill in self.background.get_skills():
                self.skills_proficient.add(skill)
                # self.skills_expert.add(skill)  # for expertise note for later

            # Apply items
            self.items.extend(self.background.get_items())

    
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

    def show_character(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.char_class} Level {self.level}") #implement adding subclass
        print(f"Race: {self.race.description()}")
        print(f"Background: {self.background}")
        print("Stats:")
        for i, stat in enumerate(STAT_NAMES):
            stat_value = self.stats[i]
            stat_bonus = (stat_value // 2) - 5
            print(f"  {stat}: {stat_value:2} ({stat_bonus:+2})")
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
        print("Items:")
        for item in self.items:
            print(f"  - {item}")
        print() # for visual clarity