# human.py
from .race import Race
from languages import LANGUAGES

class Human(Race): 
    def __init__(self):
        super().__init__("Human", None)
        self.set_bonuses()
        self.languages = ["Common"]
        extra_lang = self.choose_languages(set(self.languages), 1)
        if extra_lang:
            for lang in extra_lang:
                self.languages.append(lang)
    
    def set_bonuses(self):
         self.bonuses = {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}  # +1 to all six stats

    def choose_languages(self, known_languages: set, n: int) -> list:
        # Filter out already known and secret languages        
        chosen = []
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

            all_options = standard + exotic
            choice = input(f"Enter the name or number of language {len(chosen)+1}/{n}: ").strip()
            selected_lang = None
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(all_options):
                    selected_lang = all_options[idx]
            else:
                selected_lang = next((lang for lang in available if lang.lower() == choice.lower()), None)
            if selected_lang and selected_lang not in chosen:
                chosen.append(selected_lang)
                current_known.add(selected_lang)
            else:
                print("Invalid or duplicate choice. Please try again.")
        return chosen
