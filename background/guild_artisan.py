# guild_artisan.py
from .background import Background

class Guild_Artisan(Background):
    def __init__(self):
        super().__init__("Guild Artisan")
        self.skills = {"Insight", "Persuasion"}
        self.items = [
            "Set of artisan's tools",
            "Letter of introduction from your guild",
            "Traveler's clothes",
            "Belt pouch with 15 gp"
        ]
        self.features = ["Guild Business", "Guild Membership"]
        self.tools_proficient = {"One type of artisan's tools"}
        self.languages = {"One of your choice"}