# fighter.py 
from .char_class import CharClass
from item import Item

class Fighter(CharClass):
    ABILITY_SCORE_IMPROVEMENT = {4, 6, 8, 12, 14, 16, 19}

    def __init__(self, level: int = 1, subclass: str  = None):
        super().__init__(level, subclass)
        self.name = "Fighter"
        self.subclass_options = {
            "champion": "Champion",
            "battle master": "Battle Master",
            "battlemaster": "Battle Master",
            "eldritch knight": "Eldritch Knight",
            "eldritchknight": "Eldritch Knight",
        }
        self.hit_die_value = 10
        self.proficient_saving_throws = ["STR", "CON"]
        self.skills_proficient = {"Athletics", "Acrobatics", "Animal Handling", "History", 
                                  "Insight", "Intimidation", "Perception", "Survival"}
        
        self.armor_proficient = ["light armor", "medium armor", "heavy armor", "shields"] # fighters are proficient in all armor and shields
        self.weapons_proficient = ["simple weapons", "martial weapons"]
        # Equipment choices and static items
        self.equipment_choices = [
            {
                "description": "Choose (a) chain mail, or (b) leather armor, longbow, and 20 arrows:",
                "options": [
                    {"choice": "a", "items": ["chain_mail"]},
                    {"choice": "b", "items": ["longbow"]}
                ]
            },
            {
                "description": "Choose (a) a martial weapon and a shield, or (b) two martial weapons:",
                "options": [
                    {"choice": "a", "items": ["longsword", "warhammer", "greatsword", "battleaxe", "flail", "glaive", "halberd", "lance", "maul", "morningstar", "pike", "rapier", "scimitar", "trident", "war_pick", "whip"]},
                    {"choice": "b", "items": ["longsword", "warhammer", "greatsword", "battleaxe", "flail", "glaive", "halberd", "lance", "maul", "morningstar", "pike", "rapier", "scimitar", "trident", "war_pick", "whip"]}
                ]
            },
            {
                "description": "Choose (a) a light crossbow and 20 bolts, or (b) two handaxes:",
                "options": [
                    {"choice": "a", "items": ["crossbow_light"]},
                    {"choice": "b", "items": ["handaxe"]}
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

        # Build inventory from templates
        self.inventory = {}
        self._setup_inventory()

        # Post-setup handling for combos
        from item import create_item_from_template
        # If longbow chosen (option 1b), add leather armor and 20 arrows
        if "Longbow" in self.inventory:
            if "Leather" not in self.inventory:
                leather = create_item_from_template("leather")
                self.inventory[leather.name] = (leather, 1)
            arrow = create_item_from_template("arrow")
            self.inventory[arrow.name] = (arrow, 20)
        # If no shield in inventory after choice 2, add it (option 2a includes shield)
        if "Shield" not in self.inventory:
            shield = create_item_from_template("shield")
            self.inventory[shield.name] = (shield, 1)
        else:
            # Option 2b: two martial weapons - add a copy of the first martial weapon found
            martial_weapon_names = {"Longsword", "Warhammer", "Greatsword", "Battleaxe", "Flail", "Glaive", "Halberd", "Lance", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Trident", "War Pick", "Whip"}
            for name in self.inventory:
                if name in martial_weapon_names:
                    item, qty = self.inventory[name]
                    if qty == 1:
                        self.inventory[name] = (item, 2)
                    break
        # If crossbow light chosen (option 3a), add 20 bolts
        if "Crossbow, Light" in self.inventory:
            bolt = create_item_from_template("crossbow_bolt")
            self.inventory[bolt.name] = (bolt, 20)
        # If handaxe (option 3b), ensure qty is 2
        elif "Handaxe" in self.inventory:
            item, qty = self.inventory["Handaxe"]
            if qty == 1:
                self.inventory["Handaxe"] = (item, 2)

        # Apply level 1 features
        self.features = ["Fighting Style", "Second Wind"] # implement choices for fighting style
        self.martial_archetype_features = []

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Action Surge" not in self.features:
                        self.features.append("Action Surge x 1")
                        char_features.append("Action Surge x 1")
                        #implement number of uses based on level
                
                if self.level == 3:    
                    if "Martial Archetype" not in self.features: 
                        self.features.append("Martial Archetype")
                        # call pick archetype function
                        archetype = self.pick_martial_archetype()
                        if archetype:
                            char_features.append("Martial Archetype: " + archetype)
                    
                if self.level == 5 or self.level == 11 or self.level == 20:
                    if "Extra Attack Fighter x1" not in self.features:
                        self.features.append("Extra Attack Fighter x1")
                        char_features.append("Extra Attack Fighter x1")
                    
                    elif self.level == 11: 
                        self.features.append("Extra Attack Fighter x2")
                        char_features.append("Extra Attack Fighter x2")
                    
                    elif self.level == 20:
                        self.features.append("Extra Attack Fighter x3")
                        char_features.append("Extra Attack Fighter x3")

                if self.level == 9:
                    if "Indomitable" not in self.features:
                        self.features.append("Indomitable")
                        char_features.append("Indomitable")
                        # implement number of uses based on level

                if self.level in {3, 7, 10, 15, 18}:
                    self.apply_martial_archetype_features(self.level, char_features)

    def pick_martial_archetype(self):
        prompt = "Choose a Martial Archetype (Champion, Battle Master, Eldritch Knight): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose Champion, Battle Master, or Eldritch Knight: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice

    def apply_martial_archetype_features(self, level, char_features):
        if self.subclass == "Champion":
            if level == 3 and "Improved Critical" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Improved Critical")
                char_features.append("Improved Critical")

            if level == 7 and "Remarkable Athlete" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Remarkable Athlete")
                char_features.append("Remarkable Athlete")

            if level == 10 and "Additional Fighting Style" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Additional Fighting Style")
                char_features.append("Additional Fighting Style")

            if level == 15 and "Superior Critical" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Superior Critical")
                char_features.append("Superior Critical")

            if level == 18 and "Survivor" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Survivor")
                char_features.append("Survivor")

        if self.subclass == "Battle Master":
            if level == 3:
                if "Combat Superiority" not in self.martial_archetype_features:
                    self.martial_archetype_features.append("Combat Superiority")
                    char_features.append("Combat Superiority")
                    # implement superiority dice and maneuvers known based on level
                
                if "Student of War" not in self.martial_archetype_features:
                    self.martial_archetype_features.append("Student of War")
                    char_features.append("Student of War")

            if level == 7 and "Know Your Enemy" not in self.martial_archetype_features:
                    self.martial_archetype_features.append("Know Your Enemy")
                    char_features.append("Know Your Enemy")

            if level == 10 and "Improved Combat Superiority" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Improved Combat Superiority")
                char_features.append("Improved Combat Superiority")

            if level == 15 and "Relentless" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Relentless")
                char_features.append("Relentless")
        
        if self.subclass == "Eldritch Knight":
            if level == 3:
                if "Spellcasting" not in self.martial_archetype_features:
                    self.martial_archetype_features.append("Spellcasting")
                    char_features.append("Spellcasting")
                    # implement spellcasting feature, cantrips known, spells known, spell slots based on level

                if "Weapon Bond" not in self.martial_archetype_features:
                    self.martial_archetype_features.append("Weapon Bond")
                    char_features.append("Weapon Bond")

            if level == 7 and "War Magic" not in self.martial_archetype_features:
                self.martial_archetype_features.append("War Magic")
                char_features.append("War Magic")

            if level == 10 and "Eldritch Strike" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Eldritch Strike")
                char_features.append("Eldritch Strike")

            if level == 15 and "Arcane Charge" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Arcane Charge")
                char_features.append("Arcane Charge")

            if level == 18 and "Improved War Magic" not in self.martial_archetype_features:
                self.martial_archetype_features.append("Improved War Magic")
                char_features.append("Improved War Magic")