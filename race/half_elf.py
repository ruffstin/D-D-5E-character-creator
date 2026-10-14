# half_elf.py
from .race import Race
from languages import LANGUAGES

ALL_SKILLS = [
    "Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception",
    "History", "Insight", "Intimidation", "Investigation", "Medicine",
    "Nature", "Perception", "Performance", "Persuasion", "Religion",
    "Sleight of Hand", "Stealth", "Survival"
]

class HalfElf(Race):

    SUBRACES = {}

    def __init__(self, subrace: str = None):
        super().__init__("Half-Elf", subrace)

        # All half-elves get +2 CHA and +1 to two other stats
        self.base_bonuses = {"CHA": 2}

        self.features = {
            "Darkvision": "You can see in dim light within 60 feet as if it were bright light.",
            "Fey Ancestry": "You have advantage on saving throws against being charmed.",
            "Skill Versatility": "You gain proficiency in two skills of your choice."
        }

        # -----------------------------
        # Languages
        # -----------------------------
        self.add_language("Common")
        self.add_language("Elvish")

        # -----------------------------
        # All choices handled in Wizard
        # -----------------------------

        # +1 to two ability scores (not CHA)
        STAT_NAMES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

        self.choice_options["stat bonus"] = {
            "type": "stat bonus",
            "options": [stat for stat in STAT_NAMES if stat != "CHA"],
            "choose": 2
        }

        # One extra language
        self.choice_options["language"] = {
            "type": "language",
            "options": list(LANGUAGES.keys()),
            "choose": 1
        }

        # Two skills
        self.choice_options["skill_proficiency"] = {
            "type": "skill",
            "options": ALL_SKILLS,
            "choose": 2,
        }

        self._initialize_fixed_traits()

    def _initialize_fixed_traits(self):
        self.bonuses = self.base_bonuses.copy()
