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
from item import Item
from languages import LANGUAGES

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

        self.currency = {"copper": 0, "silver": 0, "gold": 0, "electrum": 0, "platinum": 0}
        self.inventory = {} # {Item: quantity}
        
        self.features: list[str] =  []
        self.maxhp = 0
        self.currhp = 0
        #self.hit_die = {}  # implement hit dice tracker instead of display 
        self.temphp = 0
        self.speed = 0
        self.armor_class = 0
        self.inspiration = "none"

        self.proficiency_bonus = 2
        self.skills_proficient: set[str] = set()
        self.skills_expert: set[str] = set()
        self.saving_throws_proficient: set[str] = set()

        self.other_proficiencies: set[str] = set() # tools and items
        self.languages: set[str] = set()
        self.language_order = []

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
        self.apply_class_features()
        self.apply_background_features()
        self.passive_perception = 10 + self.get_skill_bonus("Perception") #update with level up
        # self.attacks: set[str] = set() # implement attacks
        self.deathsaves = {"success": 0, "failure": 0}
        self.exhaustion = 0
        self.initiative = stats[1] // 2 - 5 # DEX mod, update with level up
        self.level_up()

    def get_proficiency_bonus(self) -> int:
        if self.level < 5:
            return 2
        elif self.level < 9:
            return 3
        elif self.level < 13:
            return 4
        elif self.level < 17:
            return 5
        else:
            return 6
    
    def apply_racial_features(self):
         if self.race:
            for lang in self.race.get_languages():
                self.add_language(lang)
            self.speed = self.race.get_speed()
            self.features.extend(self.race.get_features())
            for skill in self.race.get_skills():
                self.skills_proficient.add(skill)
            self.size = self.race.size
            # Apply tool proficiencies

    def apply_class_features(self):
        if self.char_class:
            # Apply saving throw proficiencies
            for stat in STAT_NAMES:
                self.saving_throws_proficient.add(stat)

            # Apply skill proficiencies
            self.choose_class_skills()   
            # self.skills_expert.add(skill)  # for expertise note for later

            self.maxhp = self.char_class.hit_die_value + ((self.stats[2] // 2) - 5)
            self.currhp = self.maxhp

            # Apply features
            self.features.extend(self.char_class.get_features())
            
            for lang in self.char_class.get_languages():
                self.add_language(lang)

            # Apply items
            for item_name, (item, qty) in self.char_class.get_inventory().items():
                if item_name in self.inventory:
                    _, current_qty = self.inventory[item_name]
                    self.inventory[item_name] = (item, current_qty + qty)
                else:
                    self.inventory[item_name] = (item, qty)    
    
    def choose_class_skills(self):
        """
        Choose class skills, prompting for class options first, then falling back to all skills if needed.
        """
        class_options = list(self.char_class.skills_proficient)
        num_to_choose = self.char_class.skills_known
        already = set(self.skills_proficient)
        chosen = set()

        # Offer class-specific options first (excluding ones already proficient)
        available = [s for s in class_options if s not in already]
        while len(chosen) < num_to_choose and available:
            print(f"\nChoose class skill {len(chosen)+1}/{num_to_choose}:")
            print("Options:", ", ".join(available))
            choice_input = input("Enter skill: ").strip()
            # Find matching skill in available (case-insensitive)
            choice = next((s for s in available if s.lower() == choice_input.lower()), None)
            if choice and choice not in chosen:
                chosen.add(choice)
                already.add(choice)
                available.remove(choice)
            else:
                print("Invalid or duplicate choice. Try again.")

        # If class options didn't cover the full number, let the user pick from any remaining skills
        while len(chosen) < num_to_choose:
            pool = [s for s in ALL_SKILLS if s not in already]
            if not pool:
                print("No skills left to choose.")
                break
            print(f"\nChoose replacement skill {len(chosen)+1}/{num_to_choose}:")
            print("Available:", ", ".join(pool))
            choice_input = input("Enter skill: ").strip()
            # Find matching skill in pool (case-insensitive)
            choice = next((s for s in pool if s.lower() == choice_input.lower()), None)
            if choice:
                chosen.add(choice)
                already.add(choice)
            else:
                print("Invalid choice. Try again.")

        self.skills_proficient.update(chosen)
                

    def apply_background_features(self):
        if self.background:
            # Apply skill proficiencies
            self.choose_background_skills()
            # self.skills_expert.add(skill)  # for expertise note for later
            
            # Apply features
            self.features.extend(self.background.get_features())
            
            # Apply items
            for item_name, (item, qty) in self.background.get_inventory().items():
                if item_name in self.inventory:
                    _, current_qty = self.inventory[item_name]
                    self.inventory[item_name] = (item, current_qty + qty)
                else:
                    self.inventory[item_name] = (item, qty)
            self.currency["gold"] += self.background.currency
            # Apply languages
            if (self.background.get_num_lang() > 0):
                chosen = self.background.choose_languages(self.languages, self.background.get_num_lang())
                if chosen:
                    for lang in chosen:
                        self.add_language(lang)
            
            # If the background has automatic languages, add them as well
            for lang in self.background.get_languages():
                self.add_language(lang)
            # Apply tool proficiencies

    def choose_background_skills(self):
        """
        Choose background skills. Automatically apply available background skills,
        but prompt for replacements if a background skill is already proficient.
        """
        bg_options = list(self.background.get_skills())
        already = set(self.skills_proficient)
        chosen = set()
        
        # Separate background skills into available vs already proficient
        available_bg = [s for s in bg_options if s not in already]
        duplicate_bg = [s for s in bg_options if s in already]
        
        # Auto-add available background skills
        chosen.update(available_bg)
        already.update(available_bg)
        
        # Notify user what was granted
        print(f"\nAs a {self.background.name}, you are proficient in {' and '.join(bg_options)}")
        
        # For duplicates, prompt for replacements
        for dup_skill in duplicate_bg:
            print(f"\nYou are already proficient in {dup_skill}. Let's choose a replacement skill:")
            while True:
                pool = [s for s in ALL_SKILLS if s not in already]
                if not pool:
                    print("No skills left to choose.")
                    break
                print("Available:", ", ".join(pool))
                choice_input = input("Enter skill: ").strip()
                # Find matching skill in pool (case-insensitive)
                choice = next((s for s in pool if s.lower() == choice_input.lower()), None)
                if choice:
                    chosen.add(choice)
                    already.add(choice)
                    break
                else:
                    print("Invalid choice. Try again.")
        
        self.skills_proficient.update(chosen)

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
    
    def level_up(self, next_level = 1):
        times_to_roll = 0
        if (next_level < 21):
            while (self.level < next_level):           
                self.level += 1
                times_to_roll += 1

        self.proficiency_bonus  = self.get_proficiency_bonus()
        char_hp = [self.maxhp]
        self.char_class.level_up(self.level, self.stats, self.features, char_hp)
        self.maxhp = char_hp[0]
        self.race.level_up(self.level, self.features)

        while times_to_roll > 0:
            while True: 
                level_for_this_roll = self.level - times_to_roll + 1
                choice = input(f"Do you want to roll for your hit points or take the average for level {level_for_this_roll}? (roll/average): ").strip().lower()
                if choice in ['roll', 'average', 'r', 'a', 'avg']:
                    break
                print("Invalid input. Please enter 'roll' or 'average'.")
            if choice in ['roll', 'r']:
                import random
                roll = random.randint(1, self.char_class.hit_die_value)
                print(f"You rolled a {roll} for your hit points.")
        
            elif choice in ['average', 'a', 'avg']:
                roll = (self.char_class.hit_die_value // 2) + 1
                print(f"You take the average of {roll} for your hit points.")

            self.maxhp += roll + ((self.stats[2] // 2) - 5)  # CON mod
            self.currhp = self.maxhp
            times_to_roll -= 1
            
        # with multi-classing, need to know which class to level up

    def add_item(self, item: Item, quantity: int = 1):
        if item.name in self.inventory:
            _, current_qty = self.inventory[item.name]
            self.inventory[item.name] = (item, current_qty + quantity)
        else:
            self.inventory[item.name] = (item, quantity)
    
    def remove_item(self, item_name: str, quantity: int = 1):
        if item_name in self.inventory:
            item, current_qty = self.inventory[item_name]
            new_qty = current_qty - quantity
            if new_qty > 0: 
                self.inventory[item_name] = (item, new_qty)
            else: 
                del self.inventory[item_name]

    def get_item(self, item_name: str):
        return self.inventory.get(item_name, (None, 0))
    
    def add_language(self, lang):
        if lang not in self.languages:
            self.languages.add(lang)
            self.language_order.append(lang)
    
    def print_essentials (self):
        print(f"Name: {self.name}")
        print(f"Class: Level {self.level} {self.char_class.name} ") #implement adding subclass
        print(f"Race: {self.race.description()}")
        print(f"Background: {self.background}")
        #print(f"Alignment: {self.alignment}")
        print(f"Proficiency Bonus: {self.proficiency_bonus}")
        print(f"Speed: {self.speed}")
        print(f"Hit Points: {self.currhp}/{self.maxhp} (Temporary: {self.temphp})")
        print(f"Hit Die: {self.level}d{self.char_class.hit_die_value} ")
        print()

        print("Stats:")
        for i, stat in enumerate(STAT_NAMES):
            stat_value = self.stats[i]
            stat_bonus = (stat_value // 2) - 5
            print(f"  {stat}: {stat_value:2} ({stat_bonus:+2})")
        print()

    def print_skills_and_saves(self):
        print("Saving Throws:") # Edit to show full name of stat
        for stat, value in zip(STAT_NAMES, self.stats):
            bonus = value // 2 - 5
            if stat in self.char_class.get_proficient_saving_throws():
                bonus += self.proficiency_bonus
                print(f"  {stat:<16}: {bonus:+2} *")
            else:
                print(f"  {stat:<16}: {bonus:+2}")

        print()
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
        print()
        print(f" (* = Proficient, ** = Expertise)")
        print()

    def print_items_tool_profs_lang(self):
        print("Equipment:")
        for item_name, (item, qty) in self.inventory.items():
            print(f"  - {item.name} x{qty}")
        print()

        print("Coins:")
        for coin, amount in self.currency.items():
            print(f"  {coin.capitalize()}: {amount}")
        print()
        
        print("Tool Proficiencies:")
        for tool in self.other_proficiencies:
            print(f"  - {tool}")
        print()

        print("Languages:")
        for lang_name in self.language_order:
            lang_obj = LANGUAGES[lang_name]
            print(f"{lang_obj.name}, script: {lang_obj.script}")
        print()

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