# gnome.py

from .race import Race

class Gnome(Race):
    def __init__(self, subrace: str = "Forest Gnome"):
        super().__init__("Gnome", subrace)
        self.set_bonuses()
    
    def set_bonuses(self):
        # All gnomes get +2 INT
        self.bonuses = {"INT": 2}
        if self.subrace == "Forest Gnome":
            self.bonuses["DEX"] = 1
        elif self.subrace == "Rock Gnome":
            self.bonuses["CON"] = 1
        # else: no additional bonuses
