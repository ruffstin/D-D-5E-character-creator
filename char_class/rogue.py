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
        self.roguish_features = {}
        self.expertise = set()
        # def set expertise, 2 skills your proficient in, or 1 and thieves tools

    def get_sneak_attack(self, level):    
        return SNEAK_ATTACK_DICE[level] #d6 implement more clear return?
        
    def get_languages(self):
        return self.secret_languages
        
    # def set expertise(self, current list of proficient skills, current list of expertise skills, tool list)
    


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
                        # implement expertise choice function

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
                
                # if self.level in {} call roguish_archetype feature

    def pick_roguish_archetype(self):
        prompt = "Choose a Roguish Archetype (Thief, Assassin, Arcane Trickster): "
        user_input = input(prompt).strip().lower()
        while user_input not in self.subclass_options:
            user_input = input("Invalid choice. Please choose Thief, Assassin, or Arcane Trickster: ").strip().lower()
        subclass_choice = self.subclass_options[user_input]
        self.subclass = subclass_choice
        return subclass_choice

    # roguish archetype-specific features can be added later