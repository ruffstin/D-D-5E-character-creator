# background.py

# backgrounds provide skill proficiencies, items, and features

from item import Item

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
        self.languages = []
        self.tools_proficient = []
        self.currency = 0

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
        return self.languages if hasattr(self, 'languages') else []
    
    def get_tools_proficient(self) -> list[str]:
        return self.tools_proficient if hasattr(self, 'tools_proficient') else []

    def choose_languages(self, known_languages: set, n: int) -> list:
        """
        Default: No language choices. Override in subclasses that grant language choices.
        """
        return None

    def choose_skills(self, known_skills: set, n: int) -> list:
        available = [s for s in ALL_SKILLS if s not in known_skills]
        chosen = []
        print(f"Choose {n} skill proficiencies.")
        while len(chosen) < n:
            print("Available skills:", ", ".join(available))
            # Always show the correct number (len(chosen)+1)/n
            choice = input(f"Choose skill {len(chosen)+1}/{n}: ").strip().title()
            if choice in available and choice not in chosen:
                chosen.append(choice)
                available.remove(choice)
            else:
                print("Invalid or duplicate choice. Please try again.")
        return chosen

    def __str__(self):
        return self.name
    
