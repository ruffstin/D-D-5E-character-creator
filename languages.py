# language.py

class Language: 
    def __init__(self, name, lang_type, script = "", typical_speakers = ""):
        self.name = name
        self.lang_type = lang_type  # e.g., "standard", "exotic", "secret"
        self.script = script
        self.speakers = typical_speakers

LANGUAGES = {
    "Common": Language("Common", "standard", "Common", "Humans"),
    "Dwarvish": Language("Dwarvish", "standard", "Dwarvish", "Dwarves"),
    "Elvish" : Language("Elvish", "standard", "Elvish", "Elves"),
    "Giant": Language("Giant", "standard", "Dwarvish", "Ogres and Giants"),
    "Gnomish": Language("Gnomish", "standard", "Dwarvish", "Gnomes"),
    "Goblin": Language("Goblin", "standard", "Dwarvish", "Goblinoids"),
    "Halfling": Language("Halfling", "standard", "Common", "Halflings"),
    "Orc": Language("Orc", "standard", "Dwarvish", "Orcs"),
    "Abyssal": Language("Abyssal", "exotic", "Infernal", "Demons"),
    "Celestial": Language("Celestial", "exotic", "Celestial", "Celestials"),
    "Draconic": Language("Draconic", "exotic", "Draconic", "Dragons and Dragonborn"),
    "Deep Speech": Language("Deep Speech", "exotic", "", "Aboleths and Cloakers"),
    "Infernal": Language("Infernal", "exotic", "Infernal", "Devils"),
    "Primordial": Language("Primordial", "exotic", "Dwarvish", "Elementals"),
    "Sylvan": Language("Sylvan", "exotic", "Elvish", "Fey creatures"),
    "Undercommon": Language("Undercommon", "exotic", "Elvish", "Underworld traders"),
    "Druidic": Language("Druidic", "secret", "Druidic", "Druids"),
    "Thieves' Cant": Language("Thieves' Cant", "secret", "Thieves' Cant", "Rogues and Criminals")
}