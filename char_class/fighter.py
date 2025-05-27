# fighter.py 

from .char_class import CharClass


class Fighter(CharClass):
    ABILITY_SCORE_IMPROVEMENT = {4, 6, 8, 12, 14, 16, 19}

    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Fighter"
        self.hit_die_value = 10
        self.proficient_saving_throws = ["STR", "CON"]
        self.skills_proficient = {"Athletics", "Acrobatics", "Animal Handling", "History", 
                                  "Insight", "Intimidation", "Perception", "Survival"}
        # update for choices
        self.items = ["chain mail", "shield", "longsword"] # ADD ALL ITEMS
        self.features = ["Second Wind", "Action Surge", "Fighting Style", "Extra Attack"] # implement leveling up for more features

