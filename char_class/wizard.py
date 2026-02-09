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
        self.arcane_tradition_features = {}

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

    def pick_arcane_tradition(self):
        prompt = "Choose an Arcane Tradition (Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose a valid Arcane Tradition: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice