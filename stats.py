# stats.py

# there are three primary ways to generate a character's stats
# 1. take the default values of [15, 14, 13, 12, 10, 8] 
# 2. generate random stats via rolling 4d6 and dropping the lowest. (low stat of 3, high stat of 18)
# 3. use the point buy system, you are given a total of 27 'points' to spend to buy your stats
    # this allows for creating a more custom fitting stat spread
    # the point costs being: score: 8, point cost 0; score 9, point cost 1, etc all the way up 
    # to score 14: point cost 7, and score: 15, point cost 9. 

import random

class StatGenerator: 
    DEFAULT_STATS = [15, 14, 13, 12, 10, 8]
    POINT_BUY_TOTAL = 27
    POINT_COST = {
        8:0,
        9:1,
        10:2,
        11:3,
        12:4,
        13:5, 
        14:7,
        15:9
    }

    def __init__(self, method = "default"):
        self.method = method.lower()
        self.stats = []
    
    def generate_stats(self):
        if self.method == "default":
            self.stats = self.DEFAULT_STATS
        
        elif self.method == "roll":
            self.stats = [self.roll_4d6_drop_lowest() for _ in range(6)]
        
        elif self.method == "point buy":
            self.stats = self.point_buy()
        
        else: 
            self.stats = self.DEFAULT_STATS
            raise ValueError("Invalid stat generation method. Use 'default', 'roll', or 'point buy'.")
            
        return self.stats
    
    def roll_4d6_drop_lowest(self):
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])
    
    def point_buy(self):
        print("\n=== Point Buy System ===")
        print("You have 27 points to spend. Stat range: 8 to 15.")
        print("Point Costs: 8=0, 9=1, 10=2, 11=3, 12=4, 13=5, 14=7, 15=9")
        stats = []
        total_points = self.POINT_BUY_TOTAL
        for stat_name in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
            while True:
                try:
                    val = int(input(f"Enter score for {stat_name} (8-15): "))
                    if val < 8 or val > 15:
                        print("Invalid input. Stat must be between 8 and 15.")
                        continue
                    cost = self.POINT_COST[val]
                    if total_points - cost < 0:
                        print(f"Not enough points remaining. You have {total_points} points left.")
                        continue
                    total_points -= cost
                    stats.append(val)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer between 8 and 15.")
        print(f"Points remaining: {total_points}")
        return stats

