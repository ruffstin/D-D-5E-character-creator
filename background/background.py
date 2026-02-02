# background.py

# backgrounds provide skill proficiencies, items, and features

from item import Item
from languages import LANGUAGES

ALL_SKILLS = [
    "Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception",
    "History", "Insight", "Intimidation", "Investigation", "Medicine",
    "Nature", "Perception", "Performance", "Persuasion", "Religion",
    "Sleight of Hand", "Stealth", "Survival"
]

class Background:
    def __init__(self, name: str):
        self.name = name
        self.skills: set[str] = set()
        self.inventory: dict[str, tuple[Item, int]] = {}        
        self.features = []
        self.languages = list()
        self.tools_proficient = []
        self.currency = 0
        self.num_languages = 0

    def get_skills(self, known_skills: set = None) -> set:
        if known_skills is None:
            known_skills = set()
        # By default, just return the fixed skills
        return self.skills
    
    def get_inventory(self) -> dict[str, tuple[Item, int]]:
        return self.inventory
    
    def get_features(self) -> list[str]:
        return self.features if hasattr(self, 'features') else []
    
    def get_languages(self) -> list[str]: 
        return self.languages
    
    def get_tools_proficient(self) -> list[str]:
        return self.tools_proficient if hasattr(self, 'tools_proficient') else []

    def get_num_lang(self) -> int:
        return self.num_languages

    def choose_languages(self, known_languages: set, n: int) -> list:
        # Filter out already known and secret languages        
        chosen = set()
        current_known = set(known_languages)
        while len(chosen) < n:
            available = [name for name, lang in LANGUAGES.items()
                if lang.lang_type != "secret" and name not in current_known]
            standard = [name for name in available if LANGUAGES[name].lang_type == "standard"]
            exotic = [name for name in available if LANGUAGES[name].lang_type == "exotic"]
            print("\nChoose a language you do not already know:")
            print("Standard Languages:")
            for i, lang in enumerate(standard):
                print(f"  {i+1}. {lang}")
            print("Exotic Languages:")
            for i, lang in enumerate(exotic):
                print(f"  {i+1+len(standard)}. {lang}")

            choice = input(f"Enter the name of language {len(chosen)+1}/{n}: ").strip()
            # Find a matching language in available, case-insensitive
            matching_lang = next((lang for lang in available if lang.lower() == choice.lower()), None)
            if matching_lang and matching_lang not in chosen:
                chosen.add(matching_lang)
                current_known.add(matching_lang)
            else:
                print("Invalid or duplicate choice. Please try again.")
        return chosen

    def choose_skills(self, known_skills: set, n: int) -> list:
        available = [s for s in ALL_SKILLS if s not in known_skills]
        chosen = []
        print(f"Choose {n} skill proficiencies.")
        while len(chosen) < n:
            print("Available skills:", ", ".join(available))
            # Always show the correct number (len(chosen)+1)/n
            choice_input = input(f"Choose skill {len(chosen)+1}/{n}: ").strip()
            # Find matching skill in available (case-insensitive)
            choice = next((s for s in available if s.lower() == choice_input.lower()), None)
            if choice and choice not in chosen:
                chosen.append(choice)
                available.remove(choice)
            else:
                print("Invalid or duplicate choice. Please try again.")
        return chosen

    def __str__(self):
        return self.name
    
