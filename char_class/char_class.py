# char_class.py 

# A class has a subclass, will provide features for a character, 
# and will provide items

STAT_NAMES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
from item import Item, create_item_from_template

class CharClass:
    ABILITY_SCORE_IMPROVEMENT = {4, 8, 12, 16, 19}

    def __init__(self, level: int = 1, subclass: str = None):
        if level < 1:
            raise ValueError("Level must be at least 1")
        if level > 20:
            raise ValueError("Level must be at most 20")
        self.name = "char_class"
        self.subclass = subclass
        self.subclass_options = {}
        self.level = level
        self.num_hit_die = level
        self.hit_die_value = 0
        self.inventory: dict[str, tuple[Item, int]] = {}
        self.features = []
        self.skills_known = 2
        self.skills_proficient = set()
        self.proficient_saving_throws = []
        self.features = []
        self.expertise1 = False

    def get_subclass(self) -> str:
        return self.subclass or "None"
    
    def get_languages(self):
        return []

    def _setup_inventory(self) -> None:
        """Build inventory from static items and player equipment choices.
        
        Subclasses should define:
        - self.static_items: list of template keys for items all instances get
        - self.equipment_choices: list of dicts with equipment choice groups
        """
        # Add static items
        if hasattr(self, 'static_items'):
            for template_key in self.static_items:
                item = create_item_from_template(template_key)
                self.inventory[item.name] = (item, 1)
        
        # Handle equipment choices
        if hasattr(self, 'equipment_choices'):
            for choice_group in self.equipment_choices:
                print(f"\n{choice_group['description']}")
                for option in choice_group["options"]:
                    print(f"  {option['choice']}) {', '.join(create_item_from_template(k).name for k in option['items'])}")
                
                while True:
                    user_choice = input("Enter your choice (a/b): ").strip().lower()
                    selected_option = next((opt for opt in choice_group["options"] if opt["choice"] == user_choice), None)
                    if selected_option:
                        items_in_option = selected_option["items"]
                        
                        # If only one item, add it directly
                        if len(items_in_option) == 1:
                            template_key = items_in_option[0]
                            item = create_item_from_template(template_key)
                            self.inventory[item.name] = (item, 1)
                        else:
                            # Multiple items - let user type the item name
                            item_names = [create_item_from_template(k).name for k in items_in_option]
                            item_dict = {name.lower(): key for name, key in zip(item_names, items_in_option)}
                            
                            print(f"  Available: {', '.join(item_names)}")
                            
                            while True:
                                item_input = input("Enter item: ").strip().lower()
                                if item_input in item_dict:
                                    template_key = item_dict[item_input]
                                    item = create_item_from_template(template_key)
                                    self.inventory[item.name] = (item, 1)
                                    break
                                else:
                                    print(f"'{item_input}' not found. Available: {', '.join(item_names)}")
                        break
                    else:
                        print("Invalid choice. Please enter 'a' or 'b'.")
    
    
    
    def get_inventory(self) -> dict[str, tuple[Item, int]]:
        return self.inventory
    
    def get_proficient_saving_throws(self) -> list[str]:
        return self.proficient_saving_throws
    
    def get_features (self) -> list[str]:
        return self.features
    
    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)

            # Add features based on level
                
    def ability_score_improve(self, stats: list[int], char_features, char_hp):
        old_con = stats[2]
        char_features.append(f"Ability Score Improvement lvl {self.level}")
        print("Ability Score Improvement gained at level", self.level)
        
        while True: 
            choice = input("Would you like to improve 1 stat by 2 or 2 stats by 1? (Enter '1' for one stat or '2' for two stats): ").strip()
            if choice in ['1', '2']:
                break
            print("Invalid input. Please enter '1' or '2'.")
                    
        if choice == '1':
            while True:
                # Only allow stats that are 18 or less to be selected for +2 (since 19+2 > 20)
                available = [i for i, val in enumerate(stats) if val <= 18]
                if not available:
                    print("No stats can be increased by 2 without exceeding 20.")
                    return
                
                print("Stats available for +2:")
                for i in available:
                    print(f"{i}: {STAT_NAMES[i]} (current: {stats[i]})")

                stat_input = input("Enter the stat to improve (index 0-5 or name, e.g., STR, DEX, CON, INT, WIS, CHA): ").strip().upper()
                # Try to interpret as index
                if stat_input.isdigit():
                    stat_index = int(stat_input)
                    
                elif stat_input in STAT_NAMES: 
                    stat_index = STAT_NAMES.index(stat_input)

                else: 
                    print("Invalid input. Please enter a valid index (0-5) or stat name (STR, DEX, CON, INT, WIS, CHA).")
                    continue

                if stat_index in available:
                    stats[stat_index] += 2
                    print(f"{STAT_NAMES[stat_index]} improved by 2. New value: {stats[stat_index]}")
                    break
                    
                else:
                    print("That stat cannot be increased by 2 without exceeding 20. Choose another.")
                
                        
        elif choice == '2':
            while True:
                # Only allow stats that are 19 or less to be selected for +1
                available = [i for i, val in enumerate(stats) if val < 20]
                if len(available) < 2:
                    print("Not enough stats can be increased by 1 without exceeding 20.")
                    return
                
                print("Stats available for +1:")
                for i in available:
                    print(f"{i}: {STAT_NAMES[i]} (current: {stats[i]})")

                stat_inputs = input("Enter the two stats to improve (indices 0-5 or names (STR, DEX, CON, INT, WIS, CHA), separated by spaces): ").strip().upper().split()
                if len(stat_inputs) != 2:
                    print("Please enter exactly two stats.")
                    continue

                indices = []
                for s in stat_inputs: 
                    if s.isdigit():
                        idx = int(s)
                    
                    elif s in STAT_NAMES: 
                        idx = STAT_NAMES.index(s)
                    
                    else: 
                        idx = None

                    if idx is None or idx not in available:
                        print(f"Invalid or unavailable stat: {s}. Choose from the list above.")
                        break
                    
                    indices.append(idx)
                
                else: 
                    if indices[0] == indices[1]:
                        print("Please enter two different stats.")
                        continue

                    for idx in indices: 
                        stats[idx] += 1
                        print(f"{STAT_NAMES[idx]} improved by 1. New value: {stats[idx]}")
                    break
        # After stat increases, check for CON modifier increase and apply additional hp
        old_con_mod = (old_con // 2) - 5
        new_con_mod = (stats[2] // 2) - 5
        if new_con_mod > old_con_mod:
            char_hp[0] += 1
    
    def choose_languages(self, known_languages: set, n: int) -> set:
        """
        Default: No language choices. Override in subclasses that grant language choices.
        """
        return None

    def apply_class_features(self, char_features: list[str]) -> None:
        """
        Defaut no class features to apply. Override in subclasses 
        that grant class features.
        """
        return None
    
    def apply_subclass_features(self, char_features: list[str]) -> None:
        """
        Default no subclass features to apply. Override in subclasses
        that grant subclass features.
        """
        return None

    def apply_expertise(self, char_proficient_skills: set, char_expertise_skills: set, tools: bool = False) -> None:
        """
        Allow the user to choose expertise in skills.
        If tools=True, reserved for thieves tools expertise implementation.
        If tools=False, prompts user to select 2 skills as expertise from proficient skills.
        Selected skills are added to expertise and removed from the selection pool.
        """
        if tools:
            # TODO: Implement thieves tools expertise selection in future
            return
        
        # Prompt user to select 2 expertise skills
        expertise_count = 0
        while expertise_count < 2:
            print(f"\nSelect expertise skill {expertise_count + 1} of 2")
            available_skills = char_proficient_skills - char_expertise_skills
            
            if not available_skills:
                print("No more skills available for expertise.")
                break
            
            print("Available skills:")
            skills_list = sorted(list(available_skills))
            for i, skill in enumerate(skills_list):
                print(f"  {i}: {skill}")
            
            while True:
                user_input = input("Enter the skill number: ").strip()
                if user_input.isdigit():
                    choice = int(user_input)
                    if 0 <= choice < len(skills_list):
                        selected_skill = skills_list[choice]
                        char_expertise_skills.add(selected_skill)
                        print(f"Added {selected_skill} to expertise.")
                        expertise_count += 1
                        break
                    else:
                        print("Invalid choice. Please enter a valid number.")
                else:
                    print("Invalid input. Please enter a number.")

    def description(self) -> str:
        if self.subclass:
            desc = f" ({self.subclass} {self.name})"
            return desc
        return f"{self.name}"