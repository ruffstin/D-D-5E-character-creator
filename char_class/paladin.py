# paladin.py
from .char_class import CharClass
from item import Item

class Paladin(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Paladin"
        self.subclass_options = {
            "oath of devotion": "Oath of Devotion",
            "devotion": "Oath of Devotion",
            "oath of the ancients": "Oath of the Ancients",
            "ancients": "Oath of the Ancients",
            "oath of vengeance": "Oath of Vengeance",
            "vengeance": "Oath of Vengeance",
        }
        self.hit_die_value = 10
        self.proficient_saving_throws = ["WIS", "CHA"]
        # choose 2
        self.skills_proficient = {"Athletics", "Insight", "Intimidation", 
                                  "Medicine", "Persuasion", "Religion"}
        
        self.armor_proficient = ["light armor", "medium armor", "heavy armor", "shields"] # paladins are proficient with all armor and shields
        self.weapons_proficient = ["simple weapons", "martial weapons"]
        
        # Equipment choices and static items
        self.equipment_choices = [
            {
                "description": "Choose (a) a martial weapon and a shield, or (b) two martial weapons:",
                "options": [
                    {"choice": "a", "items": ["longsword", "warhammer", "greatsword", "battleaxe", "flail", "glaive", "halberd", "lance", "maul", "morningstar", "pike", "rapier", "scimitar", "trident", "war_pick", "whip"]},
                    {"choice": "b", "items": ["longsword", "warhammer", "greatsword", "battleaxe", "flail", "glaive", "halberd", "lance", "maul", "morningstar", "pike", "rapier", "scimitar", "trident", "war_pick", "whip"]}
                ]
            },
            {
                "description": "Choose (a) five javelins or (b) any simple melee weapon:",
                "options": [
                    {"choice": "a", "items": ["javelin"]},
                    {"choice": "b", "items": ["club", "dagger", "greatclub", "handaxe", "javelin", "light_hammer", "mace", "quarterstaff", "sickle", "spear"]}
                ]
            },
            {
                "description": "Choose (a) a priest's pack or (b) an explorer's pack:",
                "options": [
                    {"choice": "a", "items": ["priests_pack"]},
                    {"choice": "b", "items": ["explorers_pack"]}
                ]
            }
        ]

        # Static items: chain mail and holy symbol
        self.static_items = ["chain_mail", "holy_symbol"]

        # Build inventory from templates
        self.inventory = {}
        self._setup_inventory()

        # Post-setup handling for combos
        from item import create_item_from_template
        # If no shield after choice 1, add it (option 1a includes shield)
        if "Shield" not in self.inventory:
            shield = create_item_from_template("shield")
            self.inventory[shield.name] = (shield, 1)
        else:
            # Option 1b: two martial weapons - add a second one
            martial_weapon_names = {"Longsword", "Warhammer", "Greatsword", "Battleaxe", "Flail", "Glaive", "Halberd", "Lance", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Trident", "War Pick", "Whip"}
            for name in self.inventory:
                if name in martial_weapon_names:
                    item, qty = self.inventory[name]
                    if qty == 1:
                        self.inventory[name] = (item, 2)
                    break
        # If javelin chosen (option 2a), ensure qty is 5
        if "Javelin" in self.inventory:
            item, qty = self.inventory["Javelin"]
            if qty == 1:
                self.inventory["Javelin"] = (item, 5)

        # Apply level 1 features
        self.features = ["Divine Sense", "Lay on Hands"] 
        self.sacred_oath_features = {}

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
                        # implement fighting styles choices

                    if "Spellcasting" not in self.features: 
                        self.features.append("Spellcasting")
                        char_features.append("Spellcasting")

                    if "Divine Smite" not in self.features:
                        self.features.append("Divine Smite")
                        char_features.append("Divine Smite")    
                
                if self.level == 3:
                    if "Divine Health" not in self.features: 
                        self.features.append("Divine Health")
                        char_features.append("Divine Health")

                    if "Sacred Oath" not in self.features: 
                        self.features.append("Sacred Oath")
                        oath = self.pick_sacred_oath()
                        if oath:
                            char_features.append("Sacred Oath: " + oath)
                        
                        # depending on your oath you get different channel divinity options
                        self.features.append("Channel Divinity")
                        char_features.append("Channel Divinity")

                if self.level == 5:
                    if "Extra Attack" not in self.features:
                        self.features.append("Extra Attack")
                        char_features.append("Extra Attack")

                if self.level == 6:
                    if "Aura of Protection" not in self.features:
                        self.features.append("Aura of Protection")
                        char_features.append("Aura of Protection") 

                if self.level == 10:
                    if "Aura of Courage" not in self.features:
                        self.features.append("Aura of Courage")
                        char_features.append("Aura of Courage")
                        #increase again at level 18
                
                if self.level == 11: 
                    if "Improved Divine Smite" not in self.features:
                        self.features.append("Improved Divine Smite")
                        char_features.append("Improved Divine Smite")

                if self.level == 14:    
                    if "Cleansing Touch" not in self.features:
                        self.features.append("Cleansing Touch")
                        char_features.append("Cleansing Touch")


    # if self.level in {} call sacred_oath feature

    def pick_sacred_oath(self):
        prompt = "Choose a Sacred Oath (Oath of Devotion, Oath of the Ancients, Oath of Vengeance): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose a valid Sacred Oath: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice

    # oath-specific feature functions can be added later