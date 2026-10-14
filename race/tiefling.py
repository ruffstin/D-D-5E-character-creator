# tiefling.py
from .race import Race

class Tiefling(Race):
    SUBRACES = {}

    def __init__(self, subrace: str = None):
        super().__init__("Tiefling", subrace)
        self.features = {
            "Darkvision": "You can see in dim light within 60 feet as if it were bright light.",
            "Hellish Resistance": "You have resistance to fire damage.",
            "Infernal Legacy": (
                "You know the Thaumaturgy cantrip. "
                "At 3rd level, you can cast Hellish Rebuke once per long rest. "
                "At 5th level, you can cast Darkness once per long rest. "
                "Charisma is your spellcasting ability for these spells."
            )
        }

        # -----------------------------
        # Languages
        # -----------------------------
        self.add_language("Common")
        self.add_language("Infernal")
        
        self.set_bonuses()


    def set_bonuses(self):
        # All tieflings get +2 CHA and +1 to INT
        self.bonuses = {"CHA": 2, "INT": 1}

    def level_up(self, level, features):
        if level >= 3 and "Hellish Rebuke" not in self.features:
            self.features["Hellish Rebuke"] = (
                "Once per long rest, cast Hellish Rebuke. Charisma is your spellcasting ability."
            )
        if level >= 5 and "Darkness" not in self.features:
            self.features["Darkness"] = (
                "Once per long rest, cast Darkness. Charisma is your spellcasting ability."
            )