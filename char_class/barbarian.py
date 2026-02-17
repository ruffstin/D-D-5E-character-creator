# barbarian.py 

from .char_class import CharClass
from item import Item
RAGE_DAMAGE = [0, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
RAGE_USES = ["0", "2", "2", "3", "3", "3", "4", "4", "4", "4", "4", "4", "5", "5", "5", "5", "5", "6", "6", "6", "Unlimited"]

class Barbarian(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Barbarian"
        self.subclass_options = {
            "berserker": "Berserker",
            "totem warrior": "Totem Warrior",
            "totem": "Totem Warrior",
        }
        self.hit_die_value = 12
        self.proficient_saving_throws = ["STR", "CON"]
        self.skills_proficient = {"Animal Handling", "Athletics", "Intimidation", "Nature", 
                                  "Perception", "Survival"}
        self.armor_proficient = ["light armor", "medium armor", "shields"]
        self.weapons_proficient = ["simple weapons", "martial weapons"]

        # Define equipment choices at level 1
        self.equipment_choices = [
            {
                "description": "Choose (a) a greataxe or (b) any martial melee weapon:",
                "options": [
                    {"choice": "a", "items": ["greataxe"]},
                    {"choice": "b", "items": ["battleaxe", "flail", "glaive", "halberd", "lance", "longsword", "maul", "morningstar", "pike", "rapier", "scimitar", "trident", "war_pick", "warhammer", "whip"]}
                ]
            },
            {
                "description": "Choose (a) two handaxes or (b) any simple weapon (not handaxe):",
                "options": [
                    {"choice": "a", "items": ["handaxe"]},  # Special handling: will add 2 total
                    {"choice": "b", "items": ["club", "dagger", "greatclub", "javelin", "light_hammer", "mace", "quarterstaff", "sickle", "spear", "crossbow_light", "dart", "shortbow", "sling"]}
                ]
            }
        ]
        
        # Static items all barbarians get
        self.static_items = ["explorers_pack"]
        
        # Build inventory
        self.inventory = {}
        self._setup_inventory()
        
        # Handle special cases: if handaxe was chosen in option (a), ensure we have 2
        if "Handaxe" in self.inventory:
            item, qty = self.inventory["Handaxe"]
            if qty == 1:
                # User chose option (a) "two handaxes", so add a second
                self.inventory["Handaxe"] = (item, 2)
        
        # Add 4 javelins
        from item import create_item_from_template
        javelin = create_item_from_template("javelin")
        self.inventory["Javelin"] = (javelin, 4)

        # Apply level 1 features
        self.features = ["Rage", "Unarmored Defense"]
        self.primal_path_features = []
    
    # make our getters visable to character sheet
    def get_rage_damage(self, level):
        return RAGE_DAMAGE[level]
    
    def get_rage_uses(self, level):
        return RAGE_USES[level]
    
    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Reckless Attack" not in self.features:
                        self.features.append("Reckless Attack")
                        char_features.append("Reckless Attack")

                    if "Danger Sense" not in self.features:
                        self.features.append("Danger Sense")
                        char_features.append("Danger Sense")

                if self.level == 3:    
                    if "Primal Path" not in self.features: 
                        self.features.append("Primal Path")
                        path = self.pick_primal_path()
                        if path:
                            char_features.append("Primal Path: " + path)
                    
                if self.level == 5:
                    if "Extra Attack" not in self.features:
                        self.features.append("Extra Attack")
                        char_features.append("Extra Attack")

                    if "Fast Movement" not in self.features:
                        self.features.append("Fast Movement")
                        char_features.append("Fast Movement")

                if self.level == 7: 
                    if "Feral Instinct" not in self.features:
                        self.features.append("Feral Instinct")
                        char_features.append("Feral Instinct")

                if self.level == 9:
                    if "Brutal Critical" not in self.features:
                        self.features.append("Brutal Critical")
                        char_features.append("Brutal Critical")

                if self.level == 11:
                    if "Relentless Rage" not in self.features:
                        self.features.append("Relentless Rage")
                        char_features.append("Relentless Rage")

                if self.level == 15:
                    if "Persistent Rage" not in self.features:
                        self.features.append("Persistent Rage")
                        char_features.append("Persistent Rage")

                if self.level == 18:
                    if "Indomitable Might" not in self.features:
                        self.features.append("Indomitable Might")
                        char_features.append("Indomitable Might")

                if self.level == 20:
                    if "Primal Champion" not in self.features:
                        self.features.append("Primal Champion")
                        char_features.append("Primal Champion")
                        # pass in stats to increase STR and CON by 4 each, max 24
                if self.level in {3, 6, 10, 14}:
                    self.apply_primal_path_features(char_features, self.level)

    def pick_primal_path(self):
        prompt = "Choose a Primal Path (Berserker or Totem Warrior): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose 'Berserker' or 'Totem Warrior': ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice

    def apply_primal_path_features(self, char_features: list[str], level: int):
        if self.subclass == "Berserker":
            if level == 3 and "Frenzy" not in self.primal_path_features:
                self.primal_path_features.append("Frenzy")
                char_features.append("Frenzy")

            if level == 6 and "Mindless Rage" not in self.primal_path_features:
                self.primal_path_features.append("Mindless Rage")
                char_features.append("Mindless Rage")
            
            if level == 10 and "Intimidating Presence" not in self.primal_path_features:
                self.primal_path_features.append("Intimidating Presence")
                char_features.append("Intimidating Presence")

            if level == 14 and "Retaliation" not in self.primal_path_features:
                self.primal_path_features.append("Retaliation")
                char_features.append("Retaliation")
        
        elif self.subclass == "Totem Warrior":
            if level == 3:
                if "Spirit Seeker" not in self.primal_path_features:
                    self.primal_path_features.append("Spirit Seeker")
                    char_features.append("Spirit Seeker")
                
                if "Totem Spirit" not in self.primal_path_features:
                    self.primal_path_features.append("Totem Spirit")
                    totem = input("Choose a Totem Spirit (Bear, Eagle, Wolf): ").strip().lower()
                    while totem not in ["bear", "eagle", "wolf"]:
                        totem = input("Invalid choice. Please choose 'Bear', 'Eagle', or 'Wolf': ").strip().lower()
                    
                    char_features.append("Totem Spirit: " + totem.capitalize())            

            if level == 6 and "Aspect of the Beast" not in self.primal_path_features:
                self.primal_path_features.append("Aspect of the Beast")
                totem = input("Choose an Aspect of the Beast (Bear, Eagle, Wolf): ").strip().lower()
                while totem not in ["bear", "eagle", "wolf"]:
                    totem = input("Invalid choice. Please choose 'Bear', 'Eagle', or 'Wolf': ").strip().lower()

                char_features.append("Aspect of the Beast: " + totem.capitalize())
            
            if level == 10 and "Spirit Walker" not in self.primal_path_features:
                self.primal_path_features.append("Spirit Walker")
                char_features.append("Spirit Walker")

            if level == 14 and "Totemic Attunement" not in self.primal_path_features:
                self.primal_path_features.append("Totemic Attunement")
                totem = input("Choose a Totemic Attunement (Bear, Eagle, Wolf): ").strip().lower()
                while totem not in ["bear", "eagle", "wolf"]:
                    totem = input("Invalid choice. Please choose 'Bear', 'Eagle', or 'Wolf': ").strip().lower()

                char_features.append("Totemic Attunement: " + totem.capitalize()) 