# char_class.py 

# A class has a subclass, will provide features for a character, 
# and will provide items

class CharClass:
    def __init__(self, level: int = 1, subclass: str = None):
        if level < 1:
            raise ValueError("Level must be at least 1")
        if level > 20:
            raise ValueError("Level must be at most 20")
        self.name = "char_class"
        self.subclass = subclass
        self.level = level
        self.num_hit_die = level
        self.hit_die_value = 0
        self.items = []
        self.features = []
        self.skills_known = 2
        self.skills_proficient = set()
        self.proficient_saving_throws = []
        self.features = []

    def get_subclass(self) -> str:
        return self.subclass or "None"
        
    def get_items(self) -> list[str]:
        return self.items
    
    def get_proficient_saving_throws(self) -> list[str]:
        return self.proficient_saving_throws
    
    def get_features (self) -> list[str]:
        return self.features
    
    def level_up(self, stats: list[int], hp, features) -> None:
        if self.level < 20:
            self.level += 1
            self.num_hit_die += 1
            # Add features based on level

    def description(self) -> str:
        if self.subclass:
            desc = f" ({self.subclass} {self.name})"
            return desc
        return f"{self.name}"