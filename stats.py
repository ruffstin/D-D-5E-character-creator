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
         
        if self.method == "default" or self.method == "d":
            print("\n=== Default Stat Generation ===")
            print("Default stat values: [15, 14, 13, 12, 10, 8]")
            self.stats = self.assign_stats(self.DEFAULT_STATS)

        elif self.method == "roll" or self.method == "r":
            print("\n=== Rolling Stats ===")
            print("Rolling 4d6 and dropping the lowest for each stat.")
            rolled = [self.roll_4d6_drop_lowest() for _ in range(6)]
            print(f"Rolled values: {rolled}")
            while True:
                assign = input("Do you want to assign these values to stats yourself? (y/n): ").lower()
                
                if assign == 'y' or assign == 'yes':
                    self.stats = self.assign_stats(rolled)
                    break

                elif assign == 'n' or assign == 'no':
                    self.stats = rolled
                    break
        
        elif self.method == "point buy" or self.method == "pb":
            self.stats = self.point_buy()
            
        return self.stats
    
    def roll_4d6_drop_lowest(self):
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])
    
    def point_buy(self):
        stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        print("\n=== Point Buy System ===")
        print("You have 27 points to spend. Stat range: 8 to 15.")
        print("Point Costs: 8=0, 9=1, 10=2, 11=3, 12=4, 13=5, 14=7, 15=9")
        stats = []
        total_points = self.POINT_BUY_TOTAL
        for stat_name in stat_names:
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
                    print(f"Points remaining: {total_points}")

                    break
                except ValueError:
                    print("Invalid input. Please enter an integer between 8 and 15.")
        
        if total_points > 0:
            print(f"You have {total_points} points remaining.")
            while True: 
                use_extra = input("Do you want to use your remaining points to improve your stats? (y/n): ").strip().lower()
                if use_extra in ['y', 'yes', 'n', 'no']:
                    break
                print("Invalid input. Please enter 'y' or 'n'.")
            while (use_extra == 'y' or use_extra == 'yes') and total_points > 0:
                improvable = []
                for i, val in enumerate(stats):
                    # Can only improve up to 15, and must be able to afford the next point
                    if val < 15 and (self.POINT_COST[val + 1] - self.POINT_COST[val]) <= total_points:
                        improvable.append((i, val))
                    
                if not improvable:
                    print("No stats can be improved with your remaining points.")
                    break
                
                print("Stats you can improve:")
                for idx, (i, val) in enumerate(improvable):
                    print(f"{idx+1}: {['STR','DEX','CON','INT','WIS','CHA'][i]} ({val} → {val+1}) for {self.POINT_COST[val+1] - self.POINT_COST[val]} points")

                try: 
                    choice_input = input("Select a stat to improve (number or stat name): ").strip()
                    # Accept both number and stat name
                    if choice_input.isdigit(): 
                        choice = int(choice_input) - 1
                        stat_idx, val = improvable[choice]
                    else: 
                        # Try to match stat name
                        stat_name = choice_input.strip().upper()
                        stat_idx = next((i for i, (idx, _) in enumerate(improvable) if stat_names[idx] == stat_name), None)
                        if stat_idx is None:
                            raise ValueError("Invalid stat name.")
                        
                        stat_idx, val = improvable[stat_idx]

                    cost = self.POINT_COST[val+1] - self.POINT_COST[val]
                    if total_points >= cost: 
                        stats[stat_idx] += 1
                        total_points -= cost
                        print(f"Upgraded! Points remaining: {total_points}")
                    
                    else:
                        print("Not enough points for that upgrade.")
                except (ValueError, IndexError):
                    print("Invalid choice.")
                
            if total_points > 0:
                while True:
                    use_extra = input("Use more points? (y/n): ").strip().lower()
                    if use_extra in ['y', 'yes', 'n', 'no']:
                        break
                    print("Invalid input. Please enter 'y' or 'n'.")     
        return stats

    def assign_stats(self, stat_values):
        assigned_stats = {}
        available_stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        available_values = stat_values.copy()
        print(f"Available values: {available_values}")
        for stat in available_stats:
            while True:
                try:
                    val = int(input(f"Assign a value from {available_values} to {stat}: "))
                    if val not in available_values:
                        print("Value not available. Choose from the remaining values.")
                        continue
                    assigned_stats[stat] = val
                    available_values.remove(val)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number from the available values.")
        # Return stats in STR, DEX, CON, INT, WIS, CHA order
        return [assigned_stats[stat] for stat in available_stats]