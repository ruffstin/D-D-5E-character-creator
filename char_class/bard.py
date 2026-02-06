# bard.py 
from .char_class import CharClass
from item import Item

class Bard(CharClass):
    def __init__(self, level: int = 1, subclass: str = None):
        super().__init__(level, subclass)
        self.name = "Bard"
        self.subclass_options = {"College of Lore", "College of Valor"}
        self.hit_die_value = 8
        self.proficient_saving_throws = ["DEX", "CHA"]
        self.skills_known = 3
        self.skills_proficient = {"Acrobatics", "Animal Handling", "Arcana", "Athletics", 
                                  "Deception", "History", "Insight", "Intimidation", 
                                  "Investigation", "Medicine", "Nature", "Perception", 
                                  "Performance", "Persuasion", "Religion", 
                                  "Sleight of Hand", "Stealth", "Survival"}
        # update for choices and all items
        self.inventory = {
            "Rapier": (Item("Rapier"), 1),
            "Lute": (Item("Lute", "A musical instrument."), 1),
            "Entertainer's Pack": (Item("Entertainer's Pack", "A pack with performance gear."), 1)
        }

        # Apply level 1 features
        self.features = ["Bardic Inspiration", "Spellcasting"]
        
        # make visable to character sheet
        self.bardic_inspiration_dice = "d6" # uses is your charisma modifier per long rest
        self.college_features = {}
        self.expertise = set()

    def level_up(self, current_level, stats: list[int], char_features: list[str], char_hp) -> None:
        while self.level < current_level:
            if self.level < 20:
                self.level += 1
                self.num_hit_die += 1
                if self.level in self.ABILITY_SCORE_IMPROVEMENT:
                    self.ability_score_improve(stats, char_features, char_hp)
            
                if self.level == 2:
                    if "Jack of All Trades" not in self.features:
                        self.features.append("Jack of All Trades")
                        char_features.append("Jack of All Trades")
                
                    if "Song of Rest" not in self.features:
                        self.features.append("Song of Rest")
                        char_features.append("Song of Rest")
                
                if self.level == 3:    
                    if "Bard College" not in self.features: 
                        self.features.append("Bard College")
                        char_features.append("Bard College")
                        # call pick college function
                    
                    if "Expertise" not in self.features:
                        self.features.append("Expertise")
                        char_features.append("Expertise")
                        # implement expertise choice function
                    
                if self.level == 5:
                    if "Font of Inspiration" not in self.features:
                        self.features.append("Font of Inspiration")
                        char_features.append("Font of Inspiration")
                        self.bardic_inspiration_dice = "d8"

                if self.level == 6:
                    if "Countercharm" not in self.features:
                        self.features.append("Countercharm")
                        char_features.append("Countercharm")
                
                if self.level == 10 or self.level == 14 or self.level == 18: 
                    if "Magical Secrets" not in self.features:
                        self.features.append("Magical Secrets")
                        char_features.append("Magical Secrets") 
                        self.bardic_inspiration_dice = "d10"
                    
                    if self.level == 10: 
                        self.features.append("Additonal Expertise")
                        char_features.append("Additonal Expertise")

                    elif self.level == 14:
                        self.features.append("Additional Magical Secrets")
                        char_features.append("Additional Magical Secrets")
                    
                    elif self.level == 18:
                        self.features.append("Additional Magical Secrets x3")
                        char_features.append("Additional Magical Secrets x3")
                
                if self.level == 15: 
                    self.bardic_inspiration_dice = "d12"

                if self.level == 20: 
                    if "Superior Inspiration" not in self.features: 
                        self.features.append("Superior Inspiration")
                        char_features.append("Superior Inspiration")
            
            # if self.level in {} call college feature

        # def pick college function 
            
        # def college feature function    
            #self.college_features.append
            # char_features.append

            #which if statement will depend on sublcass chosen

                    

              
                    