# rogue.py

from .char_class import CharClass
from item import Item
SNEAK_ATTACK_DICE = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

class Rogue(CharClass):
    ABILITY_SCORE_IMPROVEMENT = {4, 8, 10, 12, 16, 19}

    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Rogue"
        self.subclass_options = {
            "thief": "Thief",
            "assassin": "Assassin",
            "arcane trickster": "Arcane Trickster",
            "arcane tricker": "Arcane Trickster",
            "arcane": "Arcane Trickster",
            "arcanetrickster": "Arcane Trickster"
        }

        self.hit_die_value = 8
        self.proficient_saving_throws = ["DEX", "INT"]
        self.skills_known = 4
        self.skills_proficient = {"Acrobatics", "Athletics", "Deception", "Insight", 
                                  "Intimidation", "Investigation", "Perception", 
                                  "Performance", "Persuasion", "Sleight of Hand", 
                                  "Stealth"}
        self.expertise1 = True

        self.armor_proficient = ["light armor"]
        self.weapons_proficient = ["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"]
        self.tools_proficient = ["Thieves' Tools"]
        
        # Equipment choices and static items
        self.equipment_choices = [
            {
                "description": "Choose (a) a rapier or (b) a shortsword:",
                "options": [
                    {"choice": "a", "items": ["rapier"]},
                    {"choice": "b", "items": ["shortsword"]}
                ]
            },
            {
                "description": "Choose (a) a shortbow and quiver of 20 arrows, or (b) a shortsword:",
                "options": [
                    {"choice": "a", "items": ["shortbow"]},
                    {"choice": "b", "items": ["shortsword"]}
                ]
            },
            {
                "description": "Choose (a) a burglar's pack, (b) a dungeoneer's pack, or (c) an explorer's pack:",
                "options": [
                    {"choice": "a", "items": ["burglars_pack"]},
                    {"choice": "b", "items": ["dungeoneers_pack"]},
                    {"choice": "c", "items": ["explorers_pack"]}
                ]
            }
        ]

        # Static items: leather armor, one dagger, and thieves' tools
        self.static_items = ["leather", "dagger", "thieves_tools"]

        # Build inventory from templates
        self.inventory = {}
        self._setup_inventory()

        # Post-setup handling for combos
        from item import create_item_from_template
        # Add a second dagger (rogue gets 2 daggers total)
        if "Dagger" in self.inventory:
            item, qty = self.inventory["Dagger"]
            self.inventory["Dagger"] = (item, 2)
        # If shortbow chosen (option 2a), add 20 arrows
        if "Shortbow" in self.inventory:
            arrow = create_item_from_template("arrow")
            self.inventory[arrow.name] = (arrow, 20)

        # Apply level 1 features
        self.features = ["Sneak Attack", "Thieves' Cant", "Expertise"]
        self.sneak_attack_die = 6
        self.secret_languages = ["Thieves' Cant"]
        self.roguish_features = []

    def get_sneak_attack(self, level):    
        return SNEAK_ATTACK_DICE[level] #d6 implement more clear return?
        
    def get_languages(self):
        return self.secret_languages 

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Cunning Action" not in self.features:
                        self.features.append("Cunning Action")
                        char_features.append("Cunning Action")
                
                if self.level == 3:
                    if "Roguish Archetype" not in self.features: 
                        self.features.append("Roguish Archetype")
                        archetype = self.pick_roguish_archetype()
                        if archetype:
                            char_features.append("Roguish Archetype: " + archetype)

                if self.level == 5: 
                    if "Uncanny Dodge" not in self.features: 
                        self.features.append("Uncanny Dodge")
                        char_features.append("Uncanny Dodge")

                if self.level == 6:
                    if "Additional Expertise" not in self.features:
                        self.features.append("Additional Expertise")
                        char_features.append("Additional Expertise")

                if self.level == 7: 
                    if "Evasion" not in self.features: 
                        self.features.append("Evasion")
                        char_features.append("Evasion")

                if self.level == 11: 
                    if "Reliable Talent" not in self.features: 
                        self.features.append("Reliable Talent")
                        char_features.append("Reliable Talent")

                if self.level == 14:
                    if "Blindsense" not in self.features: 
                        self.features.append("Blindsense")
                        char_features.append("Blindsense")

                if self.level == 15: 
                    if "Slippery Mind" not in self.features:
                        self.features.append("Slippery Mind")
                        char_features.append("Slippery Mind")

                if self.level == 18: 
                    if "Elusive" not in self.features: 
                        self.features.append("Elusive")
                        char_features.append("Elusive")

                if self.level == 20: 
                    if "Stroke of Luck" not in self.features: 
                        self.features.append("Stroke of Luck")
                        char_features.append("Stroke of Luck")
                
                if self.level in {3, 9, 13, 17}:
                    self.apply_roguish_archetype_features(self.level, char_features)

    def pick_roguish_archetype(self):
        prompt = "Choose a Roguish Archetype (Thief, Assassin, Arcane Trickster): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose Thief, Assassin, or Arcane Trickster: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice

    def apply_roguish_archetype_features(self, level, char_features):
        if self.subclass == "Thief":
            if level == 3:
                if "Fast Hands" not in self.roguish_features:
                    self.roguish_features.append("Fast Hands")
                    char_features.append("Fast Hands")

                if "Second-Story Work" not in self.roguish_features:
                    self.roguish_features.append("Second-Story Work")
                    char_features.append("Second-Story Work")

            if level == 9 and "Supreme Sneak" not in self.roguish_features:
                self.roguish_features.append("Supreme Sneak")
                char_features.append("Supreme Sneak")

            if level == 13 and "Use Magic Device" not in self.roguish_features:
                self.roguish_features.append("Use Magic Device")
                char_features.append("Use Magic Device")

            if level == 17 and "Thief's Reflexes" not in self.roguish_features:
                self.roguish_features.append("Thief's Reflexes")
                char_features.append("Thief's Reflexes")

        if self.subclass == "Assassin":
            if level == 3:
                if "Bonus Proficiencies" not in self.roguish_features:
                    self.roguish_features.append("Bonus Proficiencies")
                    char_features.append("Bonus Proficiencies: Disguise Kit, Poisoner's Kit")

                if "Assassinate" not in self.roguish_features:
                    self.roguish_features.append("Assassinate")
                    char_features.append("Assassinate")

            if level == 9 and "Infiltration Expertise" not in self.roguish_features:
                self.roguish_features.append("Infiltration Expertise")
                char_features.append("Infiltration Expertise")

            if level == 13 and "Impostor" not in self.roguish_features:
                self.roguish_features.append("Impostor")
                char_features.append("Impostor")
                
            if level == 17 and "Death Strike" not in self.roguish_features:
                self.roguish_features.append("Death Strike")
                char_features.append("Death Strike")

        if self.subclass == "Arcane Trickster":
            if level == 3:
                if "Spellcasting" not in self.features:
                    self.features.append("Spellcasting")
                    char_features.append("Spellcasting")

                if "Mage Hand Legerdemain" not in self.roguish_features:
                    self.roguish_features.append("Mage Hand Legerdemain")
                    char_features.append("Mage Hand Legerdemain")


            if level == 9 and "Magical Ambush" not in self.roguish_features:
                self.roguish_features.append("Magical Ambush")
                char_features.append("Magical Ambush")

            if level == 13 and "Versatile Trickster" not in self.roguish_features:
                self.roguish_features.append("Versatile Trickster")
                char_features.append("Versatile Trickster")
            
            if level == 17 and "Spell Thief" not in self.roguish_features:
                self.roguish_features.append("Spell Thief")
                char_features.append("Spell Thief")