# warlock.py
from .char_class import CharClass
from item import Item
INVOCATIONS_KNOWN = {0, 0, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8}

class Warlock(CharClass): 
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Warlock"
        self.subclass_options = {
            "the archfey": "The Archfey",
            "archfey": "The Archfey",
            "the fiend": "The Fiend",
            "fiend": "The Fiend",
            "the great old one": "The Great Old One",
            "great old one": "The Great Old One",
            "old one": "The Great Old One",
        }
        self.pact_boon_options = {
            "pact of the chain": "Pact of the Chain",
            "chain": "Pact of the Chain",
            "pact of the blade": "Pact of the Blade",
            "blade": "Pact of the Blade",
            "pact of the tome": "Pact of the Tome",
            "tome": "Pact of the Tome",
        }
        self.hit_die_value = 8
        self.proficient_saving_throws = ["WIS", "CHA"]
        # choose 2 
        self.skills_proficient = {"Arcana", "Deception", "History", "Intimidation", 
                                  "Investigation", "Nature", "Religion"}
        
        # Equipment choices and static items
        self.equipment_choices = [
            {
                "description": "Choose (a) a light crossbow and 20 bolts or (b) any simple weapon:",
                "options": [
                    {"choice": "a", "items": ["crossbow_light"]},
                    {"choice": "b", "items": ["club", "dagger", "greatclub", "handaxe", "javelin", "light_hammer", "mace", "quarterstaff", "sickle", "spear"]}
                ]
            },
            {
                "description": "Choose (a) a component pouch or (b) an arcane focus:",
                "options": [
                    {"choice": "a", "items": ["component_pouch"]},
                    {"choice": "b", "items": ["arcane_focus"]}
                ]
            },
            {
                "description": "Choose (a) a scholar's pack or (b) a dungeoneer's pack:",
                "options": [
                    {"choice": "a", "items": ["scholars_pack"]},
                    {"choice": "b", "items": ["dungeoneers_pack"]}
                ]
            }
        ]

        # Static items: leather armor, any simple weapon, and 2 daggers
        self.static_items = ["leather", "dagger"]

        # Build inventory from templates
        self.inventory = {}
        self._setup_inventory()

        # Post-setup handling for combos
        from item import create_item_from_template
        # Ensure 2 daggers total
        if "Dagger" in self.inventory:
            item, qty = self.inventory["Dagger"]
            self.inventory["Dagger"] = (item, 2)
        # If crossbow chosen (option 1a), add 20 bolts
        if "Crossbow, Light" in self.inventory:
            bolt = create_item_from_template("crossbow_bolt")
            self.inventory[bolt.name] = (bolt, 20)

        # Apply level 1 features
        self.features = ["Pact Magic"]
        self.pact_boon = None
        self.pact_features = {}
        # call otherworldly patron function since subclass is chosen at level 1
        if not self.subclass:
            self.pick_otherworldly_patron()
        self.features.append("Otherworldly Patron: " + self.subclass)

    def get_invocations_known(self, level):
        if "Invocations" in self.features:
            return INVOCATIONS_KNOWN[level]
        else: 
            return 0

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None: 
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
        
                if self.level == 2:
                    if "Invocations" not in self.features:
                        self.features.append("Invocations")
                        char_features.append("Invocations")
                # Add eldritch invocations based on level 
            
                if self.level == 3: 
                    if "Pact Boon" not in self.features: 
                        self.features.append("Pact Boon")
                        # call pick pact boon function
                        boon = self.pick_pact_boon()
                        if boon:
                            char_features.append("Pact Boon: " + boon)

                if self.level == 11 or self.level == 13 or self.level == 15 or self.level == 17: 
                    if "Mystic Arcanum (6th level)" not in self.features:
                        self.features.append("Mystic Arcanum (6th level)")
                        char_features.append("Mystic Arcanum (6th level)")

                    if self.level == 13:
                        if "Mystic Arcanum (7th level)" not in self.features:
                            self.features.append("Mystic Arcanum (7th level)")
                            char_features.append("Mystic Arcanum (7th level)")
                
                    if self.level == 15:
                        if "Mystic Arcanum (8th level)" not in self.features:
                            self.features.append("Mystic Arcanum (8th level)")
                            char_features.append("Mystic Arcanum (8th level)")
                
                    if self.level == 17: 
                        if "Mystic Arcanum (9th level)" not in self.features:
                            self.features.append("Mystic Arcanum (9th level)")
                            char_features.append("Mystic Arcanum (9th level)")
                
                    
                if self.level == 20: 
                    if "Eldritch Master" not in self.features:
                        self.features.append("Eldritch Master")
                        char_features.append("Eldritch Master")


    def pick_otherworldly_patron(self):
        prompt = "Choose an Otherworldly Patron (The Archfey, The Fiend, The Great Old One): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose a valid Otherworldly Patron: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice

    def pick_pact_boon(self):
        prompt = "Choose a Pact Boon (Pact of the Chain, Pact of the Blade, Pact of the Tome): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.pact_boon_options:
            user_input = input("Invalid choice. Please choose a valid Pact Boon: ").strip().lower()
        boon_choice = self.pact_boon_options[user_input]
        self.pact_boon = boon_choice
        return boon_choice