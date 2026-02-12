# cleric.py 
from .char_class import CharClass
from item import Item

class Cleric(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Cleric"
        self.subclass_options = {
            "knowledge domain": "Knowledge Domain",
            "knowledge": "Knowledge Domain",
            "life domain": "Life Domain",
            "life": "Life Domain",
            "light domain": "Light Domain",
            "light": "Light Domain",
            "nature domain": "Nature Domain",
            "nature": "Nature Domain",
            "tempest domain": "Tempest Domain",
            "tempest": "Tempest Domain",
            "trickery domain": "Trickery Domain",
            "trickery": "Trickery Domain",
            "war domain": "War Domain",
            "war": "War Domain",
        }
        self.hit_die_value = 8
        self.proficient_saving_throws = ["WIS", "CHA"]
        self.skills_proficient = {"History", "Insight", "Medicine", "Persuasion", 
                                  "Religion"}
        
        self.armor_proficient = ["light armor", "medium armor", "shields"]
        self.weapons_proficient = ["simple weapons"]
        
        # Equipment choices and static items
        self.equipment_choices = [
            {
                "description": "Choose (a) a mace or (b) a warhammer (if proficient):",
                "options": [
                    {"choice": "a", "items": ["mace"]},
                    {"choice": "b", "items": ["warhammer"]}
                ]
            },
            {
                "description": "Choose (a) scale mail, (b) leather armor, or (c) chain mail (if proficient):",
                "options": [
                    {"choice": "a", "items": ["scale_mail"]},
                    {"choice": "b", "items": ["leather"]},
                    {"choice": "c", "items": ["chain_mail"]}
                ]
            },
            {
                "description": "Choose (a) a light crossbow and 20 bolts or (b) any simple weapon:",
                "options": [
                    {"choice": "a", "items": ["crossbow_light"]},
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

        # Static items: shield and holy symbol
        self.static_items = ["shield", "holy_symbol"]

        # Build inventory from templates
        self.inventory = {}
        self._setup_inventory()

        # If the character chose a light crossbow, add 20 bolts
        if "Crossbow, Light" in self.inventory:
            from item import create_item_from_template
            bolt = create_item_from_template("crossbow_bolt")
            self.inventory[bolt.name] = (bolt, 20)

        # Apply level 1 features
        self.features = ["Spellcasting"]
        self.domain_features = {}
        #call domain function since subclass is chosen at level 1
        if not self.subclass:
            self.pick_domain()
        self.features.append("Divine Domain: " + self.subclass)
        

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Channel Divinity" not in self.features:
                        self.features.append("Channel Divinity")
                        char_features.append("Channel Divinity")
                        # implement types of channel divinity, Turn undead and specific domains
                
                if self.level == 5:
                    if "Destroy Undead" not in self.features: 
                        self.features.append("Destroy Undead")
                        char_features.append("Destroy Undead")

                if self.level == 8:
                    if "Divine Strike" not in self.features:
                        self.features.append("Divine Strike")
                        char_features.append("Divine Strike")
                
                if self.level == 10: 
                    if "Divine Intervention" not in self.features:
                        self.features.append("Divine Intervention")
                        char_features.append("Divine Intervention")
                        # it changes at lvl 20
            
            # if self.level in {} call domain feature

    def pick_domain(self):
        prompt = "Choose a Divine Domain (Knowledge, Life, Light, Nature, Tempest, Trickery, War): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose a valid Divine Domain: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice
    
    # def domain feature function    
            #self.domain_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen


