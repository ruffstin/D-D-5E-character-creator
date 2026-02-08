# monk.py
from .char_class import CharClass
from item import Item
UNARMORED_MOVEMENT = [0, 0, 10, 10, 10, 10, 15, 15, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 30, 30, 30]
MARTIAL_ARTS_DIE = ["0", "1d4", "1d4", "1d4", "1d4", "1d6", "1d6", "1d6", "1d6", "1d6", "1d6", "1d8", "1d8", "1d8", "1d8", "1d8", "1d8", "1d10", "1d10", "1d10", "1d10"]

class Monk(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Monk"
        self.subclass_options = {"Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"}
        self.hit_die_value = 8
        self.proficient_saving_throws = ["STR", "DEX"]
        # choose 2
        self.skills_proficient = {"Acrobatics", "Athletics", "History", "Insight", 
                                  "Religion", "Stealth"}
        self.martial_arts_die = MARTIAL_ARTS_DIE[level]
        # tool proficiency - Tools: Choose one type of artisan's tools or one musical instrument
        
        # Define equipment choices at level 1
        self.equipment_choices = [
            {
                "description": "Choose (a) a shortsword or (b) any simple weapon:",
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
        
        # Static items: darts will be added manually as quantity 10
        self.static_items = []
        
        # Build inventory
        self.inventory = {}
        self._setup_inventory()
        
        # Add 10 darts manually
        from item import create_item_from_template
        dart = create_item_from_template("dart")
        self.inventory["Dart"] = (dart, 10)
                
        # Apply level 1 features
        self.features = ["Unarmored Defense", "Martial Arts"]
        self.monastic_tradition_features = {}
    
    def get_max_ki_points(self, level):
        if "Ki" in self.features:
            return level
        else: 
            return 0
    
    def get_unarmored_movement(self, level):
        return UNARMORED_MOVEMENT[level]
    
    def get_martial_arts_die(self, level):
        return MARTIAL_ARTS_DIE[level]
    
    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Ki" not in self.features:
                        self.features.append("Ki")
                        char_features.append("Ki")
                        # implement ki features
                
                    if "Unarmored Movement" not in self.features:
                        self.features.append("Unarmored Movement")
                        char_features.append("Unarmored Movement")
                
                if self.level == 3:    
                    if "Monastic Tradition" not in self.features: 
                        self.features.append("Monastic Tradition")
                        char_features.append("Monastic Tradition")
                        # call pick tradition function

                    if "Deflect Missiles" not in self.features:
                        self.features.append("Deflect Missiles")
                        char_features.append("Deflect Missiles")
                    
                if self.level == 4:
                    if "Slow Fall" not in self.features:
                        self.features.append("Slow Fall")
                        char_features.append("Slow Fall")

                if self.level == 5:
                    if "Extra Attack" not in self.features:
                        self.features.append("Extra Attack")
                        char_features.append("Extra Attack")

                    if "Stunning Strike" not in self.features:
                        self.features.append("Stunning Strike")
                        char_features.append("Stunning Strike")
                
                if self.level == 6:
                    if "Ki-Empowered Strikes" not in self.features:
                        self.features.append("Ki-Empowered Strikes")
                        char_features.append("Ki-Empowered Strikes")

                if self.level == 7:
                    if "Evasion" not in self.features:
                        self.features.append("Evasion")
                        char_features.append("Evasion")

                    if "Stillness of Mind" not in self.features:
                        self.features.append("Stillness of Mind")
                        char_features.append("Stillness of Mind")
                
                if self.level == 10:
                    if "Purity of Body" not in self.features:
                        self.features.append("Purity of Body")
                        char_features.append("Purity of Body")

                if self.level == 13:
                    if "Tongue of the Sun and Moon" not in self.features:
                        self.features.append("Tongue of the Sun and Moon")
                        char_features.append("Tongue of the Sun and Moon")

                if self.level == 14:
                    if "Diamond Soul" not in self.features:
                        self.features.append("Diamond Soul")
                        char_features.append("Diamond Soul")

                if self.level == 15:
                    if "Timeless Body" not in self.features:
                        self.features.append("Timeless Body")
                        char_features.append("Timeless Body")

                if self.level == 18:
                    if "Empty Body" not in self.features:
                        self.features.append("Empty Body")
                        char_features.append("Empty Body")

                if self.level == 20:
                    if "Perfect Self" not in self.features:
                        self.features.append("Perfect Self")
                        char_features.append("Perfect Self")    


            # if self.level in {} call monastic_tradition feature

        # def pick monastic_tradition function 
            
        # def monastic_tradition feature function    
            #self.monastic_tradition_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen
