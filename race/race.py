# parent - race.py
# A race may have a subrace, and will provide a bonus to stats
from languages import LANGUAGES, Language
STAT_INDEX = {"STR": 0, "DEX": 1, "CON": 2, "INT": 3, "WIS": 4, "CHA": 5}

class Race:
    def __init__(self, name: str, subrace: str = None):
        self.name = name
        self.subrace = subrace
        self.bonuses = {}  # e.g., {"DEX": +2, "WIS": +1}
        self.languages = set()
        self.speed = 30
        self.features: dict[str, str] = {}
        self.fixed_skills = set()
        self.choice_skills = set()
        self.spells_known: set[str] = set()
        self.size = "Medium"
        self.other_proficiencies = set()
        self.tools_proficient = set()
        self.description_text = ""
        self.choice_options: dict[str, dict] = {}
        self.choices_made: dict[str, list[str]] = {}        

    # -----------------------------
    # Core Mechanics
    # -----------------------------
    def apply_racial_bonuses(self, stats: list[int]) -> list[int]:
        updated_stats = stats.copy()
        for stat, bonus in self.bonuses.items():
            updated_stats[STAT_INDEX[stat]] += bonus
        return updated_stats
    
    # -----------------------------
    # Language Handling
    # -----------------------------
    def add_language(self, language):
        if isinstance(language, str):
            language = LANGUAGES[language]

        self.languages.add(language)
    
    def get_languages(self) -> list[str]:
        return [lang.name for lang in self.languages]

    def get_available_languages(self):
        known = set(self.languages)
        return [
            name for name, lang in LANGUAGES.items()
            if lang.lang_type != "secret" and name not in known
        ]
    
    # -----------------------------
    # Data Access
    # -----------------------------
    def get_speed(self) -> int:
        return self.speed 
    
    def get_features(self) -> dict[str, str]:
        return self.features

    def get_skills(self) -> set[str]:
        return self.fixed_skills | self.choice_skills
    
    def get_skill_proficiencies(self) -> set[str]:
        return (self.fixed_skills | self.choice_skills).copy()
    
    def get_skill_choice_count(self) -> int: 
        for choice in self.choice_options.values():
            if choice.get("type") == "skill":
                return choice.get("choose", 0)
        return 0
    
    def get_skill_choice_options(self) -> list[str]:
        for choice in self.choice_options.values():
            if choice.get("type") == "skill":
                return choice.get("options", [])
        return []
    
    def reset_choices(self):
        self.choices_made.clear()
        self.choice_skills.clear()
        self.tools_proficient = set()
        self.spells_known = set()

        self._initialize_fixed_traits()
    
    def level_up(self, char_level: int, char_features: list[str]):
        return None
    

    def _initialize_fixed_traits(self):
        """Children override this to reapply fixed proficiencies"""
        pass   

    # -----------------------------
    # User input
    # -----------------------------
    def set_choice(self, choice_key: str, selections: list[str]):
        """
        Stores validated user selections for a choice category.
        """
        if choice_key not in self.choice_options:
            return False
    
        choice_info = self.choice_options[choice_key]
        max_allowed = choice_info.get("choose", 1)
        options = choice_info.get("options")

        # Enforce exact number required
        if len(selections) != max_allowed:
            return False

        # Prevent duplicates
        if len(selections) != len(set(selections)):
            return False

        # If options are explicitly defined, validate against them
        if options:
            for sel in selections:
                if sel not in options:
                    return False

        self.choices_made[choice_key] = selections
        return True
    
    def get_choice_definitions(self):
        return self.choice_options

    def apply_choices(self):
        """
        Applies stored choices to the race's data.
        """
        for choice_key, selections in self.choices_made.items():
            choice_info = self.choice_options.get(choice_key, {})
            choice_type = choice_info.get("type")

            for selection in selections:

                if choice_type == "tool":
                    self.tools_proficient.add(selection)

                elif choice_type == "skill":
                    self.choice_skills.add(selection)

                elif choice_type == "language":
                    self.add_language(selection)

                elif choice_type == "stat bonus":
                    # Add +1 to selected stat
                    if selection in STAT_INDEX:
                        self.bonuses[selection] = self.bonuses.get(selection, 0) + 1

                elif choice_type == "spell":
                    self.spells_known.add(selection)

    # -----------------------------
    # Display Information
    # -----------------------------

    def description(self) -> str:
        return self.description_text
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "subrace": self.subrace,
            "speed": self.speed,
            "size": self.size,
            "languages": self.get_languages(),
            "features": self.get_features(),
            "skills": list(self.get_skills()),
            "tools": list(self.tools_proficient),
            "spells": list(self.spells_known),
            "bonuses": self.bonuses
        } 
    