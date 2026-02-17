# ranger.py
from .char_class import CharClass
from item import Item

class Ranger(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Ranger"
        # Normalize enclave inputs to canonical names
        self.subclass_options = {
            "hunter": "Hunter",
            "beast master": "Beast Master",
            "beastmaster": "Beast Master",
            "beast": "Beast Master",
        }
        self.hit_die_value = 10
        self.proficient_saving_throws = ["STR", "DEX"]
        self.skills_known = 3
        self.skills_proficient = {"Animal Handling", "Athletics", "Insight", "Investigation", 
                                   "Nature", "Perception", "Stealth", "Survival"}
        
        self.armor_proficient = ["light armor", "medium armor", "shields"]
        self.weapons_proficient = ["simple weapons", "martial weapons"]
        
        # Equipment choices and static items
        self.equipment_choices = [
            {
                "description": "Choose (a) scale mail or (b) leather armor:",
                "options": [
                    {"choice": "a", "items": ["scale_mail"]},
                    {"choice": "b", "items": ["leather"]}
                ]
            },
            {
                "description": "Choose (a) two shortswords or (b) two simple melee weapons:",
                "options": [
                    {"choice": "a", "items": ["shortsword"]},
                    {"choice": "b", "items": ["club", "dagger", "greatclub", "handaxe", "javelin", "light_hammer", "mace", "quarterstaff", "sickle", "spear"]}
                ]
            },
            {
                "description": "Choose (a) a dungeoneer's pack or (b) an explorer's pack:",
                "options": [
                    {"choice": "a", "items": ["dungeoneers_pack"]},
                    {"choice": "b", "items": ["explorers_pack"]}
                ]
            }
        ]

        # Static items: longbow and 20 arrows
        self.static_items = ["longbow"]

        # Build inventory from templates
        self.inventory = {}
        self._setup_inventory()

        # Post-setup handling for combos
        from item import create_item_from_template
        # If shortsword (option 2a), ensure qty is 2
        if "Shortsword" in self.inventory:
            item, qty = self.inventory["Shortsword"]
            if qty == 1:
                self.inventory["Shortsword"] = (item, 2)
        else:
            # Option 2b: two simple melee weapons - add a second one
            simple_melee_names = {"Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear"}
            for name in self.inventory:
                if name in simple_melee_names:
                    item, qty = self.inventory[name]
                    if qty == 1:
                        self.inventory[name] = (item, 2)
                    break
        # Add 20 arrows for the longbow
        arrow = create_item_from_template("arrow")
        self.inventory[arrow.name] = (arrow, 20)

        # Apply level 1 features
        self.features = ["Favored Enemy", "Natural Explorer"] 
        self.language = "" # set language based off favored enemy
        self.enclave_features = []

    def get_langauge(self) -> str:
        return self.language

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Fighting Style" not in self.features:
                        self.features.append("Fighting Style")
                        char_features.append("Fighting Style")
                
                    if "Spellcasting" not in self.features: 
                        self.features.append("Spellcasting")
                        char_features.append("Spellcasting")

                if self.level == 3: 
                    if "Primeval Awareness" not in self.features: 
                        self.features.append("Primeval Awareness")
                        char_features.append("Primeval Awareness")

                    if "Ranger Enclave" not in self.features: 
                        self.features.append("Ranger Enclave")
                        enclave = self.pick_ranger_enclave()
                        if enclave:
                            char_features.append(enclave)
                
                if self.level == 5: 
                    if "Extra Attack" not in self.features: 
                        self.features.append("Extra Attack")
                        char_features.append("Extra Attack")
                
                if self.level == 8: 
                    if "Land's Stride" not in self.features: 
                        self.features.append("Land's Stride")
                        char_features.append("Land's Stride")

                if self.level == 10: 
                    if "Hide in Plain Sight" not in self.features: 
                        self.features.append("Hide in Plain Sight")
                        char_features.append("Hide in Plain Sight")

                if self.level == 14: 
                    if "Vanish" not in self.features:
                        self.features.append("Vanish")
                        char_features.append("Vanish")
                    
                if self.level == 18: 
                    if "Feral Senses" not in self.features: 
                        self.features.append("Feral Senses")
                        char_features.append("Feral Senses")

                if self.level == 20: 
                    if "Foe Slayer" not in self.features: 
                        self.features.append("Foe Slayer")
                        char_features.append("Foe Slayer")
                
                if self.level in {3, 7, 11, 15}:
                    self.apply_enclave_features(self.level, char_features)

    def pick_ranger_enclave(self):
        prompt = "Choose a Ranger Enclave (Hunter or Beast Master): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose Hunter or Beast Master: ").strip().lower()
        subclass_Choice = self.subclass_options[user_input]
        self.subclass = subclass_Choice
        return subclass_Choice

    def apply_enclave_features(self, level, char_features):
        if self.subclass == "Hunter":
            if level == 3 and "Hunter's Prey" not in self.enclave_features:
                self.enclave_features.append("Hunter's Prey")
                char_features.append("Hunter's Prey")
                # implement options for Hunter's Prey (Colossus Slayer, Giant Killer, Horde Breaker)
        
            if level == 7 and "Defensive Tactics" not in self.enclave_features:
                self.enclave_features.append("Defensive Tactics")
                char_features.append("Defensive Tactics")
        
            if level == 11 and "Multiattack" not in self.enclave_features:
                self.enclave_features.append("Multiattack")
                char_features.append("Multiattack")
                # implement options for multiattack (Volley or Whirlwind Attack)

            if level == 15 and "Superior Hunter's Defense" not in self.enclave_features:
                self.enclave_features.append("Superior Hunter's Defense")
                char_features.append("Superior Hunter's Defense")
                # implement options for Superior Hunter's Defense (Evasion, Stand Against the Tide, Uncanny Dodge)

        if self.subclass == "Beast Master":
            if level == 3 and "Ranger's Companion" not in self.enclave_features:
                self.enclave_features.append("Ranger's Companion")
                char_features.append("Ranger's Companion")
            
            if level == 7 and "Exceptional Training" not in self.enclave_features:
                self.enclave_features.append("Exceptional Training")
                char_features.append("Exceptional Training")
            
            if level == 11 and "Bestial Fury" not in self.enclave_features:
                self.enclave_features.append("Bestial Fury")
                char_features.append("Bestial Fury")

            if level == 15 and "Share Spells" not in self.enclave_features:
                self.enclave_features.append("Share Spells")
                char_features.append("Share Spells")

            