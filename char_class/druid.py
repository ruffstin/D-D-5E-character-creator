# druid.py 
from .char_class import CharClass

class Druid(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Druid"
        self.subclass_options = {
            "circle of the land": "Circle of the Land",
            "land": "Circle of the Land",
            "circle of the moon": "Circle of the Moon",
            "moon": "Circle of the Moon",
        }
        self.hit_die_value = 8
        self.proficient_saving_throws = ["INT", "WIS"]
        self.skills_proficient = {"Animal Handling", "Arcana", "History", "Insight", 
                                  "Medicine", "Nature", "Perception", "Religion"}

        self.armor_proficient = ["light armor", "medium armor", "shields", "druids will not wear armor or use shields made of metal"]
        self.weapons_proficient = ["clubs", "daggers", "darts", "javelins", "maces", "quarterstaffs", "scimitars", "sickles", "slings", "spears"]
        self.tools_proficient = ["Herbalism kit"]

        # Define equipment choices at level 1
        self.equipment_choices = [
            {
                "description": "Choose (a) a wooden shield or (b) any simple weapon:",
                "options": [
                    {"choice": "a", "items": ["wooden_shield"]},
                    {"choice": "b", "items": ["club", "dagger", "greatclub", "handaxe", "javelin", "light_hammer", "mace", "quarterstaff", "sickle", "spear"]}
                ]
            },
            {
                "description": "Choose (a) a scimitar or (b) any simple melee weapon:",
                "options": [
                    {"choice": "a", "items": ["scimitar"]},
                    {"choice": "b", "items": ["club", "dagger", "greatclub", "handaxe", "javelin", "light_hammer", "mace", "quarterstaff", "sickle", "spear"]}
                ]
            }
        ]
        
        # Static items all druids get
        self.static_items = ["leather", "explorers_pack", "druidic_focus"]
        
        # Build inventory
        self.inventory = {}
        self._setup_inventory()

        # Apply level 1 features
        self.features = ["Druidic", "Spellcasting"] 
        self.secret_languages = ["Druidic"]
        self.circle_features = {}

    def get_languages(self):
        return self.secret_languages

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Wild Shape" not in self.features:
                        self.features.append("Wild Shape")
                        char_features.append("Wild Shape")
                        #implement wild shapes uses
                
                    if "Druid Circle" not in self.features: 
                        self.features.append("Druid Circle")
                        circle = self.pick_circle()
                        if circle:
                            char_features.append("Druid Circle: " + circle)
                    
                if self.level == 18: 
                    if "Timeless Body" not in self.features: 
                        self.features.append("Timeless Body")
                        char_features.append("Timeless Body")
                    
                    if "Beast Spells" not in self.features: 
                        self.features.append("Beast Spells")
                        char_features.append("Beast Spells")

                if self.level == 20: 
                    if "Archdruid" not in self.features: 
                        self.features.append("Archdruid")
                        char_features.append("Archdruid")
                
                # if self.level in {} call circle feature

    def pick_circle(self):
        prompt = "Choose a Druid Circle(Circle of the Land or Circle of the Moon): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose either 'Circle of the Land' or 'Circle of the Moon': ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice
    
    # def circle feature function    
            #self.circle_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen
