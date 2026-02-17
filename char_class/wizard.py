# wizard.py 
from .char_class import CharClass
from item import Item

class Wizard(CharClass): 
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Wizard"
        self.subclass_options = {
            "school of abjuration": "School of Abjuration",
            "abjuration": "School of Abjuration",
            "school of conjuration": "School of Conjuration",
            "conjuration": "School of Conjuration",
            "school of divination": "School of Divination",
            "divination": "School of Divination",
            "school of enchantment": "School of Enchantment",
            "enchantment": "School of Enchantment",
            "school of evocation": "School of Evocation",
            "evocation": "School of Evocation",
            "school of illusion": "School of Illusion",
            "illusion": "School of Illusion",
            "school of necromancy": "School of Necromancy",
            "necromancy": "School of Necromancy",
            "school of transmutation": "School of Transmutation",
            "transmutation": "School of Transmutation",
        }
        self.hit_die_value = 6
        self.proficient_saving_throws = ["INT", "WIS"]
        # choose 2 
        self.skills_proficient = {"Arcana", "History", "Insight", 
                                  "Investigation", "Medicine", "Religion"}
        
        self.weapons_proficient = ["daggers", "darts", "slings", "quarterstaffs", "light_crossbows"]
        
        # Equipment choices and static items
        self.equipment_choices = [
            {
                "description": "Choose (a) a quarterstaff or (b) a dagger:",
                "options": [
                    {"choice": "a", "items": ["quarterstaff"]},
                    {"choice": "b", "items": ["dagger"]}
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
                "description": "Choose (a) a scholar's pack or (b) an explorer's pack:",
                "options": [
                    {"choice": "a", "items": ["scholars_pack"]},
                    {"choice": "b", "items": ["explorers_pack"]}
                ]
            }
        ]

        # Static items: spellbook
        self.static_items = ["spellbook"]

        # Build inventory from templates
        self.inventory = {}
        self._setup_inventory()

        # Apply level 1 features
        self.features = ["Spellcasting", "Arcane Recovery"]
        self.arcane_tradition_features = []

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)

                if self.level == 2:
                    if "Arcane Tradition" not in self.features: 
                        self.features.append("Arcane Tradition")
                        # call pick arcane_tradition function
                        tradition = self.pick_arcane_tradition()
                        if tradition:
                            char_features.append("Arcane Tradition: " + tradition)

                if self.level == 18: 
                    if "Spell Mastery" not in self.features: 
                        self.features.append("Spell Mastery")
                        char_features.append("Spell Mastery")
                
                if self.level == 20: 
                    if "Signature Spells" not in self.features: 
                        self.features.append("Signature Spells")
                        char_features.append("Signature Spells")

                if self.level in {2, 6, 10, 14}:
                    self.apply_arcane_tradition_features(self.level, char_features)

    def pick_arcane_tradition(self):
        prompt = "Choose an Arcane Tradition (Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose a valid Arcane Tradition: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice
    
    def apply_class_features(self, level, char_features):
        if self.subclass == "School of Abjuration":
            if level == 2:
                if "Abjuration Savant" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Abjuration Savant")
                    char_features.append("Abjuration Savant")
                if "Arcane Ward" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Arcane Ward")
                    char_features.append("Arcane Ward")
            
            if level == 6 and "Projected Ward" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Projected Ward")
                char_features.append("Projected Ward")
            
            if level == 10 and "Improved Abjuration" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Improved Abjuration")
                char_features.append("Improved Abjuration")

            if level == 14 and "Spell Resistance" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Spell Resistance")
                char_features.append("Spell Resistance")

        if self.subclass == "School of Conjuration":
            if level == 2:
                if "Conjuration Savant" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Conjuration Savant")
                    char_features.append("Conjuration Savant")
            
                if "Minor Conjuration" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Minor Conjuration")
                    char_features.append("Minor Conjuration")

            if level == 6 and "Benign Transposition" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Benign Transposition")
                char_features.append("Benign Transposition")
            
            if level == 10 and "Focused Conjuration" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Focused Conjuration")
                char_features.append("Focused Conjuration")

            if level == 14 and "Durable Summons" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Durable Summons")
                char_features.append("Durable Summons")

        if self.subclass == "School of Divination":
            if level == 2:
                if "Divination Savant" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Divination Savant")
                    char_features.append("Divination Savant")

                if "Portent" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Portent")
                    char_features.append("Portent")

            if level == 6 and "Expert Divination" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Expert Divination")
                char_features.append("Expert Divination")

            if level == 10 and "The Third Eye" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("The Third Eye")
                char_features.append("The Third Eye")

            if level == 14 and "Greater Portent" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Greater Portent")
                char_features.append("Greater Portent") 

        if self.subclass == "School of Enchantment":
            if level == 2:
                if "Enchantment Savant" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Enchantment Savant")
                    char_features.append("Enchantment Savant")

                if "Hypnotic Gaze" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Hypnotic Gaze")
                    char_features.append("Hypnotic Gaze")

            if level == 6 and "Instinctive Charm" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Instinctive Charm")
                char_features.append("Instinctive Charm")

            if level == 10 and "Split Enchantment" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Split Enchantment")
                char_features.append("Split Enchantment")

            if level == 14 and "Alter Memories" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Alter Memories")
                char_features.append("Alter Memories")
            
        if self.subclass == "School of Evocation":
            if self.level == 2:
                if "Evocation Savant" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Evocation Savant")
                    char_features.append("Evocation Savant")

                if "Sculpt Spells" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Sculpt Spells")
                    char_features.append("Sculpt Spells")

            if level == 6 and "Potent Cantrip" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Potent Cantrip")
                char_features.append("Potent Cantrip")
            
            if level == 10 and "Empowered Evocation" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Empowered Evocation")
                char_features.append("Empowered Evocation")

            if level == 14 and "Overchannel" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Overchannel")
                char_features.append("Overchannel")

        if self.subclass == "School of Illusion":
            if level == 2:
                if "Illusion Savant" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Illusion Savant")
                    char_features.append("Illusion Savant")

                if "Improved Minor Illusion" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Improved Minor Illusion")
                    char_features.append("Improved Minor Illusion")

            if level == 6 and "Malleable Illusions" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Malleable Illusions")
                char_features.append("Malleable Illusions")

            if level == 10 and "Illusory Self" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Illusory Self")
                char_features.append("Illusory Self")
            
            if level == 14 and "Illusionary Reality" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Illusionary Reality")
                char_features.append("Illusionary Reality")
            
        if self.subclass == "School of Necromancy":
            if level == 2:
                if "Necromancy Savant" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Necromancy Savant")
                    char_features.append("Necromancy Savant")

                if "Grim Harvest" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Grim Harvest")
                    char_features.append("Grim Harvest")

            if level == 6 and "Undead Thralls" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Undead Thralls")
                char_features.append("Undead Thralls")

            if level == 10 and "Inured to Undeath" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Inured to Undeath")
                char_features.append("Inured to Undeath")

            if level == 14 and "Command Undead" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Command Undead")
                char_features.append("Command Undead")
        
        if self.subclass == "School of Transmutation":
            if level == 2:
                if "Transmutation Savant" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Transmutation Savant")
                    char_features.append("Transmutation Savant")

                if "Minor Alchemy" not in self.arcane_tradition_features:
                    self.arcane_tradition_features.append("Minor Alchemy")
                    char_features.append("Minor Alchemy")
            
            if level == 6 and "Transmuter's Stone" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Transmuter's Stone")
                char_features.append("Transmuter's Stone")

            if level == 10 and "Shapechanger" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Shapechanger")
                char_features.append("Shapechanger")

            if level == 14 and "Master Transmuter" not in self.arcane_tradition_features:
                self.arcane_tradition_features.append("Master Transmuter")
                char_features.append("Master Transmuter")

