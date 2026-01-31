# warlock.py
from .char_class import CharClass
from item import Item
INVOCATIONS_KNOWN = {0, 0, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8}

class Warlock(CharClass): 
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Warlock"
        self.subclass_options = {"The Archfey", "The Fiend", "The Great Old One"}
        self.pact_boon_options = {"Pact of the Chain", "Pact of the Blade", "Pact of the Tome"}
        self.hit_die_value = 8
        self.proficient_saving_throws = ["WIS", "CHA"]
        # choose 2 
        self.skills_proficient = {"Arcana", "Deception", "History", "Intimidation", 
                                  "Investigation", "Nature", "Religion"}
        # update for choices and all items
        self.inventory = {
            "Arcane Focus": (Item("Arcane Focus", "A focus for casting spells"), 1),
            "Light Crossbow": (Item("Light Crossbow"), 1)
        }

        # Apply level 1 features
        self.features = ["Otherworldly Patron", "Pact Magic"]
        #call otherworldly patron function since subclass is chosen at level 1
        

    def get_invocations_known(self, level):
        if "Invocations" in self.features:
            return INVOCATIONS_KNOWN[level]
        else: 
            return 0

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None: 
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
        
                if self.level == 2:
                    if "Invocations" not in self.features:
                        self.features.append("Invocations")
                        char_features.append("Invocations")
                # Add eldritch invocations based on level 
            
                if self.level == 3: 
                    if "Pact Boon" not in self.features: 
                        self.features.append("Pact Boon")
                        char_features.append("Pact Boon")
                        # call pick pact boon function

                if self.level == 11 or self.level == 13 or self.level == 15 or self.level == 17: 
                    if "Mystic Arcanum (6th level)" not in self.features:
                        self.features.append("Mystic Arcanum (6th level)")
                        char_features.append("Mystic Arcanum (6th level)")

                    if self.level == 13:
                        if "Mystic Arcanum (7th level)" not in self.features:
                            self.features.append("Mystic Arcanum (7th level)")
                            char_features.append("Mystic Arcanum (7th level)")
                
                    if self.level == 15:
                        if "Mystic Arcanum (8th level)" not in self.features:
                            self.features.append("Mystic Arcanum (8th level)")
                            char_features.append("Mystic Arcanum (8th level)")
                
                    if self.level == 17: 
                        if "Mystic Arcanum (9th level)" not in self.features:
                            self.features.append("Mystic Arcanum (9th level)")
                            char_features.append("Mystic Arcanum (9th level)")
                
                    
                if self.level == 20: 
                    if "Eldritch Master" not in self.features:
                        self.features.append("Eldritch Master")
                        char_features.append("Eldritch Master")


        # if self.level in {} call otherworldly patron feature
        # def pick pact boon function
        # def pick otherworldly patron function 
            
        # def otherworldly patron feature function    
            #self.otherworldly_patron_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen