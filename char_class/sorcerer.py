# sorcerer.py
from .char_class import CharClass
from item import Item

class Sorcerer(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Sorcerer"
        self.subclass_options = {
            "draconic bloodline": "Draconic Bloodline",
            "draconic": "Draconic Bloodline",
            "wild magic": "Wild Magic",
            "wild": "Wild Magic",
        }
        self.hit_die_value = 6
        self.proficient_saving_throws = ["CON", "CHA"]
        # choose 2
        self.skills_proficient = {"Arcana", "Deception", "Insight", "Intimidation", 
                                  "Persuasion", "Religion"}
        
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
                "description": "Choose (a) a dungeoneer's pack or (b) an explorer's pack:",
                "options": [
                    {"choice": "a", "items": ["dungeoneers_pack"]},
                    {"choice": "b", "items": ["explorers_pack"]}
                ]
            }
        ]

        # Static items: 2 daggers
        self.static_items = ["dagger"]

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
        self.features = ["Spellcasting"]
        self.origin_features = {}
        # call sorcerous_origin since subclass is chosen at level 1
        if not self.subclass:
            self.pick_sorcerous_origin()
            self.features.append("Sorcerous Origin: " + self.subclass)
        
    def get_max_sorcery_points(self, level):
        if "Font of Magic" in self.features:
            return level
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
                    if "Font of Magic" not in self.features:
                        self.features.append("Font of Magic")
                        char_features.append("Font of Magic")
                        #implement font of magic features

                if self.level == 3:
                    if "Metamagic" not in self.features: 
                        self.features.append("Metamagic")
                        char_features.append("Metamagic")
                        # call pick metamagic function   
                        # pick another option at 10th level 
                        # pick another option at 17th level

                if self.level == 20: 
                    if "Sorcerous Restoration" not in self.features:
                        self.features.append("Sorcerous Restoration")
                        char_features.append("Sorcerous Restoration")     


        # if self.level in {} call sorcerous_origin feature

        # def pick sorcerous_origin function 
            
        # def sorcerous_origin feature function    
            #self.sorcerous_origin_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen

    def pick_sorcerous_origin(self):
        prompt = "Choose a Sorcerous Origin (Draconic Bloodline or Wild Magic): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose Draconic Bloodline or Wild Magic: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice