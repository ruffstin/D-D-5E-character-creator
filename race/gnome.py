# gnome.py

from .race import Race

class Gnome(Race):

    SUBRACES = {
        "Forest Gnome": "",
        "Rock Gnome": ""
    }

    def __init__(self, subrace: str = "Forest Gnome"):
        super().__init__("Gnome", subrace)

        self.size = "Small"
        self.speed = 25

        self.features = {
            "Darkvision": "", 
            "Gnome Cunning": ""
        }

        # -----------------------------
        # Languages
        # -----------------------------
        self.add_language("Common")
        self.add_language("Gnomish")

        self.set_bonuses()
    
    def set_bonuses(self):
        # All gnomes get +2 INT
        self.bonuses = {"INT": 2}
        if self.subrace == "Forest Gnome":
            self.bonuses["DEX"] = 1
            self.features.update({
                "Natural Illusionist": "", 
                "Minor Illusion": "", 
                "Speak with Small Beasts": ""
            })
            # you can cast the "Minor Illusion" cantrip. Intelligence is your spellcasting ability for it.

        elif self.subrace == "Rock Gnome":
            self.bonuses["CON"] = 1
            self.features.update({
                "Artificer's Lore": "", 
                "Tinker": ""
            })
            self.tools_proficient = ["Tinker's tools"]
        # else: no additional bonuses
