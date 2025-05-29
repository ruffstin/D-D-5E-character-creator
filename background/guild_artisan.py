# guild_artisan.py
from .background import Background
from item import Item

class Guild_Artisan(Background):
    def __init__(self):
        super().__init__("Guild Artisan")
        self.skills = {"Insight", "Persuasion"}
        self.inventory = {
            "Artisan's Tools": (Item("Artisan's Tools", "A set of artisan's tools (one of your choice)."), 1),
            "Letter of Introduction": (Item("Letter of Introduction", "Letter from your guild."), 1),
            "Traveler's Clothes": (Item("Traveler's Clothes", "A set of traveler's clothes."), 1),
            "Pouch": (Item("Pouch", "A belt pouch for coins or trinkets."), 1)
        }
        self.currency = 15
        self.features = ["Guild Business", "Guild Membership"]
        self.tools_proficient = {"One type of artisan's tools"}
        self.languages = {"One of your choice"}