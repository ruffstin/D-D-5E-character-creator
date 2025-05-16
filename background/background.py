# background.py

# backgrounds provide skill proficiencies, items, and features
class Background:
    def __init__(self, name: str):
        self.name = name
        self.skills: set[str] = set()
        self.items: list[str] = []

    def get_skills(self) -> set[str]:
        return self.skills

    def get_items(self) -> list[str]:
        return self.items

    def __str__(self):
        return self.name
