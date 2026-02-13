# gnome.py

from .race import Race

class Gnome(Race):
    def __init__(self, subrace: str = "Forest Gnome"):
        super().__init__("Gnome", subrace)
        self.set_bonuses()
        self.features = ["Darkvision", "Gnome Cunning"]
        self.speed = 25
        self.languages = ["Common", "Gnomish"]
    
    def set_bonuses(self):
        # All gnomes get +2 INT
        self.bonuses = {"INT": 2}
        if self.subrace == "Forest Gnome":
            self.bonuses["DEX"] = 1
            self.features.append("Natural Illusionist")
            # you can cast the "Minor Illusion" cantrip. Intelligence is your spellcasting ability for it.
            self.features.append("Speak with Small Beasts")

        elif self.subrace == "Rock Gnome":
            self.bonuses["CON"] = 1
            self.features.append("Artificer's Lore")
            self.features.append("Tinker")
            self.tools_proficient = ["Tinker’s tools"]
        # else: no additional bonuses
