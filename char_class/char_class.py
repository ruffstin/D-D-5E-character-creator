# char_class.py 

# A class has a subclass, will provide features for a character, 
# and will provide items

class CharClass:
    def __init__(self, char_class: str, level: int = 1, subclass: str = None):
        if level < 1:
            raise ValueError("Level must be at least 1")
        if level > 20:
            raise ValueError("Level must be at most 20")
        self.name = char_class
        self.subclass = subclass
        self.level = level
        self.num_hit_die = level
        self.hit_die_value = 0
        self.items = []
        self.features = []
        self.skills_proficient = set()

    def get_subclass(self) -> str:
        return self.subclass or "None"
        
    def get_items(self) -> list[str]:
        return self.items
    
    def get_proficient_saving_throws(self) -> list[str]:
        return []
    
    def description(self) -> str:
        desc = f"{self.name}"
        if self.subclass:
            desc += f" ({self.subclass})"
        return desc