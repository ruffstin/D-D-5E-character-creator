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
        
        # Static items: shield and holy symbol
        self.static_items = ["shield", "holy_symbol"]

        # Equipment choices and static items # future implementations will require checking prof rather
        # than subclass
        self.equipment_choices = []

        # have the user choose their subclass first to allow equipment to be chosen based on their proficiency
        if not self.subclass:
            self.pick_domain()
        self.features.append("Divine Domain: " + self.subclass)

        # martial weapon proficiency
        if self.subclass in {"Tempest Domain", "War Domain"}:
            self.equipment_choices.append({
                "description": "Choose (a) a mace or (b) a warhammer",
                "options": [
                    {"choice": "a", "items": ["mace"]},
                    {"choice": "b", "items": ["warhammer"]}
                ]
            })
        else: 
            self.static_items.append("mace")

        # heavy armor proficiency
        if self.subclass in {"Life Domain", "Nature Domain", "Tempest Domain", "War Domain"}:
            self.equipment_choices.append({
                "description": "Choose (a) scale mail, (b) leather armor, or (c) chain mail:",
                "options": [
                    {"choice": "a", "items": ["scale_mail"]},
                    {"choice": "b", "items": ["leather"]},
                    {"choice": "c", "items": ["chain_mail"]}
                ]
            })
        else: 
            self.equipment_choices.append({
                "description": "Choose (a) scale mail, (b) leather armor:",
                "options": [
                    {"choice": "a", "items": ["scale_mail"]},
                    {"choice": "b", "items": ["leather"]}
                ]
            })

        # append remaining equipment choices

        self.equipment_choices.append({
                "description": "Choose (a) a light crossbow and 20 bolts or (b) any simple weapon:",
                "options": [
                    {"choice": "a", "items": ["crossbow_light"]},
                    {"choice": "b", "items": ["club", "dagger", "greatclub", "handaxe", "javelin", "light_hammer", "mace", "quarterstaff", "sickle", "spear"]}
                ]
            })
        self.equipment_choices.append({
                "description": "Choose (a) a priest's pack or (b) an explorer's pack:",
                "options": [
                    {"choice": "a", "items": ["priests_pack"]},
                    {"choice": "b", "items": ["explorers_pack"]}
                ]
            })
                    

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
        self.domain_features = []

        
        self.apply_domain_features(self.level, self.features)
        # apply spells per subclass
        

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
            
                if self.level in {2, 6, 8, 17}:
                    self.apply_domain_features(self.level, char_features)


    def pick_domain(self):
        prompt = "Choose a Divine Domain (Knowledge, Life, Light, Nature, Tempest, Trickery, War): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose a valid Divine Domain: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice
    
    # Divine Strike increases in damage at 14th level 
    def apply_domain_features(self, level, char_features):
        if self.subclass == "Knowledge Domain":
            if level == 1 and "Blessings of Knowledge" not in self.domain_features:
                self.domain_features.append("Blessings of Knowledge")
                char_features.append("Blessings of Knowledge")

            if level == 2 and "Channel Divinity: Knowledge of the Ages" not in self.domain_features:
                self.domain_features.append("Channel Divinity: Knowledge of the Ages")

            if level == 6 and "Channel Divinity: Read Thoughts" not in self.domain_features: 
                self.domain_features.append("Channel Divinity: Read Thoughts")
                char_features.append("Channel Divinity: Read Thoughts")

            if level == 8 and "Potent Spellcasting" not in self.domain_features: 
                self.domain_features.append("Potent Spellcasting")
                char_features.append("Potent Spellcasting")

            if level == 17 and "Visions of the Past" not in self.domain_features: 
                self.domain_features.append("Visions of the Past")
                char_features.append("Visions of the Past")            

        if self.subclass == "Life Domain":
            if level == 1 and "Bonus Proficiency" not in self.domain_features: 
                self.domain_features.append("Disciple of Life")
                char_features.append("Disciple of Life")

            if level == 2 and "Channel Divinity: Preserve Life" not in self.domain_features: 
                self.domain_features.append("Channel Divinity: Preserve Life")
                char_features.append("CHannel Divinity: Preserve Life")

            if level == 6 and "Blessed Healer" not in self.domain_features: 
                self.domain_features.append("Blessed Healer")
                char_features.append("Blessed Healer")

            if level == 8 and "Divine Strike" not in self.domain_features: 
                self.domain_features.append("Divine Strike")
                char_features.append("Divine Strike")

            if level == 17 and "Supreme Healing" not in self.domain_features:
                self.domain_features.append("Supreme Healing")
                char_features.append("Supreme Healing")

        if self.subclass == "Light Domain":
            if level == 1:
                if "Bonus Cantrip" not in self.domain_features: 
                    self.domain_features.append("Bonus Cantrip") 
                    char_features.append("Bonus Cantrip")               

                if "Warding Flare" not in self.domain_features: 
                    self.domain_features.append("Warding Flare")
                    char_features.append("Warding Flare")

            if level == 2 and "Channel Divinity: Radiance of the Dawn" not in self.domain_features: 
                self.domain_features.append("Channel Divinity: Radiance of the Dawn")
                char_features.append("Channel Divinity: Radiance of the Dawn")

            if level == 6 and "Improved Flare" not in self.domain_features: 
                self.domain_features.append("Improved Flare")
                char_features.append("Improved Flare")

            if level == 8 and "Potent Spellcasting":
                self.domain_features.append("Potent Spellcasting")
                char_features.append("Potent Spellcasting")

            if level == 17 and "Corona of Light" not in self.domain_features: 
                self.domain_features.append("Corona of Light")
                char_features.append("Corona of Light")

        if self.subclass == "Nature Domain":
            if level == 1: 
                if "Acolyte of Nature" not in self.domain_features:
                    self.domain_features.append("Acolyte of Nature")
                    char_features.append("Acolyte of Nature")

                if "Bonus Proficiency" not in self.domain_features: 
                    self.domain_features.append("Bonus Proficiency")
                    char_features.append("Bonus Proficiency")

            if level == 2 and "Channel Divinity: Charm Animal and Plants" not in self.domain_features:
                self.domain_features.append("Channel Divinity: Charm Animal and Plants")
                char_features.append("Channel Divinity: Charm Animal and Plants")

            if level == 6 and "Dampen Elements" not in self.domain_features:
                self.domain_features.append("Dampen Elements")
                char_features.append("Dampen Elements")

            if level == 8 and "Divine Strike" not in self.domain_features:
                self.domain_features.append("Divine Strike")
                char_features.append("Master of Nature")
            
            if level == 17 and "Master of Nature" not in self.domain_features: 
                self.domain_features.append("Master of Nature")
                char_features.append("Master of Nature")

        if self.subclass == "Tempest Domain":
            if level == 1: 
                if "Bonus Proficiencies" not in self.domain_features: 
                    self.domain_features.append("Bonus Proficiencies")
                    char_features.append("Bonus Proficiencies")

                if "Wrath of the Storm" not in self.domain_features: 
                    self.domain_features.append("Wrath of the Storm")
                    char_features.append("Wrath of the Storm")

            if level == 2 and "Channel Divinity: Destructive Wrath" not in self.domain_features:
                self.domain_features.append("Channel Divinity: Destructive Wrath")
                char_features.append("Channel Divinity: Destructive Wrath")

            if level == 6 and "Thunderous Strike" not in self.domain_features: 
                self.domain_features.append("Thunderous Strike")
                char_features.append("Thunderous Strike")

            if level == 8 and "Divine Strike" not in self.domain_features: 
                self.domain_features.append("Divine Strike")
                char_features.append("Divine Strike")

            if level == 17 and "Stormborn" not in self.domain_features: 
                self.domain_features.append("Stormborn")
                char_features.append("Stormborn")

        if self.subclass == "Trickery Domain":
            if level == 1 and "Blessing of the Trickster" not in self.domain_features:
                self.domain_features.append("Blessing of the Trickster")
                char_features.append("Blessings of the Trickster")

            if level == 2 and "Channel Divinity: Invoke Duplicity" not in self.domain_features: 
                self.domain_features.append("Channel Divinity: Invoke Duplicity")
                char_features.append("Channel Divinity: Invoke Duplicity")

            if level == 6 and "Channel Divinity: Cloack of Shadows" not in self.domain_features: 
                self.domain_features.append("Channel Divinity: Cloak of Shadows")
                char_features.append("Channel Divinity: Cloak of Shadows")

            if level == 8 and "Divine Strike" not in self.domain_features:
                self.domain_features.append("Divine Strike")
                char_features.append("Divine Strike")

            if level == 17 and "Improved Duplicity" not in self.domain_features: 
                self.domain_features.append("Improved Duplicity")
                char_features.append("Improved Duplicity")

        if self.subclass == "War Domain":
            if level == 1: 
                if "Bonus Proficiencies" not in self.domain_features: 
                    self.domain_features.append("Bonus Proficiencies")
                    char_features.append("Bonus Proficiencies")

                if "War Priest" not in self.domain_features:
                    self.domain_features.append("War Priest")
                    char_features.append("War Priest")

            if level == 2 and "Channel Divinity: Guided Strike" not in self.domain_features:
                self.domain_features.append("Channel Divinity: Guided Strike")
                char_features.append("Channel Divinity: Guided Strike")

            if level == 6 and "Channel Divinity: War God's Blessing" not in self.domain_features:
                self.domain_features.append("Channel Divinity: War God's Blessing")
                char_features.append("Channel Divinity: War God's Blessing")

            if level == 8 and "Divine Strike" not in self.domain_features:
                self.domain_features.append("Divine Strike")
                char_features.append("Divine Strike")

            if level == 17 and "Avatar of Battle" not in self.domain_features:
                self.domain_features.append("Avatar of Battle")
                char_features.append("Avatar of Battle")