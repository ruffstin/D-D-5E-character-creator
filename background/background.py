# background.py

# backgrounds provide skill proficiencies, items, and features

from item import Item

class Background:
    def __init__(self, name: str):
        self.name = name
        self.skills: set[str] = set()
        self.items: list[str] = []
        self.features = []
        self.languages = []
        self.tools_proficient = []

    def get_skills(self) -> set[str]:
        return self.skills

    def get_items(self) -> list[str]:
        return self.items
    
    def get_features(self) -> list[str]:
        return self.features if hasattr(self, 'features') else []
    
    def get_languages(self) -> list[str]: 
        return self.languages if hasattr(self, 'languages') else []
    
    def get_tools_proficient(self) -> list[str]:
        return self.tools_proficient if hasattr(self, 'tools_proficient') else []

    def __str__(self):
        return self.name
