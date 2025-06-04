# acolyte.py
from .background import Background
from item import Item
from languages import LANGUAGES

class Acolyte(Background):
    def __init__(self):
        super().__init__("Acolyte")
 
        self.skills = {"Insight", "Religion"}
        self.inventory = {
            "Holy Symbol": (Item("Holy Symbol", "A symbol of your faith."), 1),
            "Prayer Book": (Item("Prayer Book", "A book or wheel for prayers."), 1),
            "Incense": (Item("Incense", "Stick of incense."), 5),
            "Vestments": (Item("Vestments", "Religious clothing."), 1),
            "Common Clothes": (Item("Common Clothes", "Simple everyday clothing."), 1),
            "Pouch": (Item("Pouch", "A small belt pouch for coins or trinkets."), 1)

        }
        self.currency = 15
        self.features = ["Shelter of the Faithful"]
        self.languages = list()
    
    def choose_languages(self, known_languages: set, n: int) -> list:
        # Filter out already known and secret languages        
        chosen = set()
        current_known = set(known_languages)
        while len(chosen) < n:
            available = [name for name, lang in LANGUAGES.items()
                if lang.lang_type != "secret" and name not in current_known]
            standard = [name for name in available if LANGUAGES[name].lang_type == "standard"]
            exotic = [name for name in available if LANGUAGES[name].lang_type == "exotic"]
            print("\nChoose a language you do not already know:")
            print("Standard Languages:")
            for i, lang in enumerate(standard):
                print(f"  {i+1}. {lang}")
            print("Exotic Languages:")
            for i, lang in enumerate(exotic):
                print(f"  {i+1+len(standard)}. {lang}")

            choice = input(f"Enter the name of language {len(chosen)+1}/{n}: ").strip()
            # Find a matching language in available, case-insensitive
            matching_lang = next((lang for lang in available if lang.lower() == choice.lower()), None)
            if matching_lang and matching_lang not in chosen:
                chosen.add(matching_lang)
                current_known.add(matching_lang)
            else:
                print("Invalid or duplicate choice. Please try again.")
        return chosen

