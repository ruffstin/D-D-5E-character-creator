# half_elf.py
from .race import Race
from languages import LANGUAGES

ALL_SKILLS = [
    "Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception",
    "History", "Insight", "Intimidation", "Investigation", "Medicine",
    "Nature", "Perception", "Performance", "Persuasion", "Religion",
    "Sleight of Hand", "Stealth", "Survival"
]

class HalfElf(Race):
    def __init__(self):
        super().__init__("Half-Elf", None)
        self.set_bonuses()
        self.features = ["Darkvision", "Fey Ancestry", "Skill Versatility"]
        self.languages = ["Common", "Elvish"]
        extra_lang = self.choose_languages(set(self.languages), 1)
        for lang in extra_lang: 
            self.languages.append(lang)
    
        self.skills = set()
        chosen_skills = self.choose_skills(set(), 2)
        for skill in chosen_skills:
            self.skills.add(skill)

    def set_bonuses(self):
        # All half-elves get +2 CHA and +1 to two other stats
        self.bonuses = {"CHA": 2}
        available_stats = ["STR", "DEX", "CON", "INT", "WIS"]
        chosen = 0
        print("As a Half-Elf, you get +1 to two different ability scores (other than CHA).")
        while chosen < 2:
            print("Available stats:", ", ".join(available_stats))
            choice = input(f"Choose stat {chosen+1}/2 to receive +1: ").strip().upper()
            if choice in available_stats:
                self.bonuses[choice] = 1
                available_stats.remove(choice)
                chosen += 1
            else:
                print("Invalid or duplicate choice. Please try again.")

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

    def get_skills(self, known_skills: set = None) -> set:
        return set(self.skills)

    def choose_skills(self, known_skills: set, n: int = 2) -> list:
        available = [s for s in ALL_SKILLS if s not in known_skills]
        chosen = []
        print(f"As a Half-Elf, you gain proficiency in {n} skills of your choice.")
        while len(chosen) < n:
            print("Available skills:", ", ".join(available))
            choice = input(f"Choose skill {len(chosen)+1}/{n}: ").strip().title()
            if choice in available and choice not in chosen:
                chosen.append(choice)
                available.remove(choice)
            else:
                print("Invalid or duplicate choice. Please try again.")
        return chosen