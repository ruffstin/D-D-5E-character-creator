# bard.py 
from .char_class import CharClass
from item import Item

class Bard(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Bard"
        self.subclass_options = {
            "college of lore": "College of Lore",
            "lore": "College of Lore",
            "college of valor": "College of Valor",
            "valor": "College of Valor"
        }
        self.hit_die_value = 8
        self.proficient_saving_throws = ["DEX", "CHA"]
        self.skills_known = 3
        self.skills_proficient = {"Acrobatics", "Animal Handling", "Arcana", "Athletics", 
                                  "Deception", "History", "Insight", "Intimidation", 
                                  "Investigation", "Medicine", "Nature", "Perception", 
                                  "Performance", "Persuasion", "Religion", 
                                  "Sleight of Hand", "Stealth", "Survival"}
        
        self.armor_proficient = ["light armor"]
        self.weapons_proficient = ["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"]
        self.tools_proficient = self.select_instruments()  # function to select 3 musical instruments from the list of options

        # Equipment choices and static items (level 1)
        self.equipment_choices = [
            {
                "description": "Choose (a) a rapier, (b) a longsword, or (c) any simple weapon:",
                "options": [
                    {"choice": "a", "items": ["rapier"]},
                    {"choice": "b", "items": ["longsword"]},
                    {"choice": "c", "items": ["club", "dagger", "greatclub", "handaxe", "javelin", "light_hammer", "mace", "quarterstaff", "sickle", "spear"]}
                ]
            },
            {
                "description": "Choose (a) a diplomat's pack or (b) an entertainer's pack:",
                "options": [
                    {"choice": "a", "items": ["diplomats_pack"]},
                    {"choice": "b", "items": ["entertainers_pack"]}
                ]
            },
            {
                "description": "Choose (a) a lute or (b) any other musical instrument:",
                "options": [
                    {"choice": "a", "items": ["lute"]},
                    {"choice": "b", "items": ["bagpipes", "drum", "dulcimer", "flute", "lyre", "horn", "pan_flute", "shawm"]}
                ]
            }
        ]

        # Static items: Leather armor and a dagger
        self.static_items = ["leather", "dagger"]

        # Build inventory from templates
        self.inventory = {}
        self._setup_inventory()

        # Apply level 1 features
        self.features = ["Bardic Inspiration", "Spellcasting"]
        
        # make visable to character sheet
        self.bardic_inspiration_dice = "d6" # uses is your charisma modifier per long rest
        self.college_features = {}
        self.expertise = set()

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Jack of All Trades" not in self.features:
                        self.features.append("Jack of All Trades")
                        char_features.append("Jack of All Trades")
                
                    if "Song of Rest" not in self.features:
                        self.features.append("Song of Rest")
                        char_features.append("Song of Rest")
                
                if self.level == 3:    
                    if "Bard College" not in self.features:
                        self.features.append("Bard College") 
                        college = self.pick_college()
                        if college:
                            char_features.append("Bard College: " + college)
                    
                    if "Expertise" not in self.features:
                        self.features.append("Expertise")
                        char_features.append("Expertise")
                        # implement expertise choice function
                    
                if self.level == 5:
                    if "Font of Inspiration" not in self.features:
                        self.features.append("Font of Inspiration")
                        char_features.append("Font of Inspiration")
                        self.bardic_inspiration_dice = "d8"

                if self.level == 6:
                    if "Countercharm" not in self.features:
                        self.features.append("Countercharm")
                        char_features.append("Countercharm")
                
                if self.level == 10 or self.level == 14 or self.level == 18: 
                    if "Magical Secrets" not in self.features:
                        self.features.append("Magical Secrets")
                        char_features.append("Magical Secrets") 
                        self.bardic_inspiration_dice = "d10"
                    
                    if self.level == 10: 
                        self.features.append("Additional Expertise")
                        char_features.append("Additional Expertise")

                    elif self.level == 14:
                        self.features.append("Additional Magical Secrets")
                        char_features.append("Additional Magical Secrets")
                    
                    elif self.level == 18:
                        self.features.append("Additional Magical Secrets x3")
                        char_features.append("Additional Magical Secrets x3")
                
                if self.level == 15: 
                    self.bardic_inspiration_dice = "d12"

                if self.level == 20: 
                    if "Superior Inspiration" not in self.features: 
                        self.features.append("Superior Inspiration")
                        char_features.append("Superior Inspiration")
                # if self.level in {} call college feature

    def pick_college(self):
        prompt = "Choose a Bard College (College of Lore or College of Valor): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose either 'College of Lore' or 'College of Valor': ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice

    def select_instruments(self):
        instruments = ["bagpipes", "drum", "dulcimer", "flute", "lyre", "horn", "pan_flute", "shawm"]
        selected_instruments = []
        while len(selected_instruments) < 3:
            prompt = f"Choose a musical instrument from the following list ({', '.join(instruments)}): "
            user_input = input(prompt).strip().lower()
            if user_input in instruments and user_input not in selected_instruments:
                selected_instruments.append(user_input)
                instruments.remove(user_input)  # Remove the selected instrument from the options
            else:
                print("Invalid choice or instrument already selected. Please choose a different instrument.")
        return selected_instruments
                    
    # def college feature function    
            #self.college_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen

              
                    