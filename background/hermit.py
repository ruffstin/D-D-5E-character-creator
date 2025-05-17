# Hermit.py
from .background import Background

class Hermit(Background):
    def __init__(self):
        super().__init__("Hermit")
        self.skills = {"Medicine", "Religion"}
        self.items = [
            "Scroll case stuffed full of notes",
            "Winter blanket",
            "Common clothes",
            "Herbalism kit",
            "Belt pouch with 5 gp"
        ]