# stats_gui.py

import random


class StatGenerator:
    """
    Pure stat generation engine.
    No user interaction. No prints. No input().
    Designed to be controlled entirely by GUI.
    """

    DEFAULT_STATS = [15, 14, 13, 12, 10, 8]
    POINT_BUY_TOTAL = 27

    POINT_COST = {
        8: 0,
        9: 1,
        10: 2,
        11: 3,
        12: 4,
        13: 5,
        14: 7,
        15: 9
    }

    STAT_ORDER = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

    CLASS_STAT_PRIORITY = {
        "artificer": ["INT", "CON", "DEX", "STR", "WIS", "CHA"],
        "barbarian": ["STR", "CON", "DEX", "WIS", "CHA", "INT"],
        "bard": ["CHA", "CON", "DEX", "STR", "WIS", "INT"],
        "cleric": ["WIS", "CON", "STR", "DEX", "INT", "CHA"],
        "druid": ["WIS", "CON", "DEX", "STR", "INT", "CHA"],
        "fighter": ["STR", "CON", "DEX", "WIS", "INT", "CHA"],
        "monk": ["DEX", "CON", "WIS", "INT", "CHA", "STR"],
        "paladin": ["STR", "CON", "CHA", "WIS", "INT", "DEX"],
        "ranger": ["DEX", "CON", "WIS", "STR", "INT", "CHA"],
        "rogue": ["DEX", "CHA", "CON", "INT", "WIS", "STR"],
        "sorcerer": ["CHA", "CON", "DEX", "WIS", "INT", "STR"],
        "warlock": ["CHA", "CON", "DEX", "INT", "WIS", "STR"],
        "wizard": ["INT", "CON", "DEX", "WIS", "CHA", "STR"]
    }

    def __init__(self, char_class: str | None = None):
        self.char_class = char_class.lower() if char_class else None

    # ==========================================================
    # BASIC GENERATION METHODS
    # ==========================================================

    def get_default(self) -> list[int]:
        """Return default 5e stat array."""
        return self.DEFAULT_STATS.copy()

    def roll_stats(self) -> list[int]:
        """Roll 4d6 drop lowest six times."""
        return [self._roll_4d6_drop_lowest() for _ in range(6)]

    def _roll_4d6_drop_lowest(self) -> int:
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort()
        return sum(rolls[1:])

    # ==========================================================
    # ASSIGNMENT METHODS
    # ==========================================================

    def auto_assign(self, stat_values: list[int]) -> list[int]:
        """
        Auto-assign highest stats to class priorities.
        Returns stats in STR, DEX, CON, INT, WIS, CHA order.
        """
        if not self.char_class or self.char_class not in self.CLASS_STAT_PRIORITY:
            raise ValueError("Invalid or missing class for auto assignment.")

        priority = self.CLASS_STAT_PRIORITY[self.char_class]
        sorted_values = sorted(stat_values, reverse=True)

        assigned = {}
        for i, stat in enumerate(priority):
            assigned[stat] = sorted_values[i]

        return [assigned[stat] for stat in self.STAT_ORDER]

    def validate_manual_assignment(
        self,
        assignment: dict[str, int],
        available_values: list[int]
    ) -> list[int]:
        """
        Validate manual stat placement.
        Ensures the assigned values exactly match the available values.
        """
        if sorted(assignment.values()) != sorted(available_values):
            raise ValueError("Assigned values do not match available stat values.")

        return [assignment[stat] for stat in self.STAT_ORDER]

    # ==========================================================
    # POINT BUY
    # ==========================================================

    def validate_point_buy(self, assignment: dict[str, int]) -> list[int]:
        """
        Validate point buy assignment.
        Ensures total cost does not exceed 27 and values are between 8–15.
        """
        total_cost = 0

        for stat, value in assignment.items():
            if value not in self.POINT_COST:
                raise ValueError(f"{value} is not a valid point-buy stat value (8–15).")

            total_cost += self.POINT_COST[value]

        if total_cost > self.POINT_BUY_TOTAL:
            raise ValueError(
                f"Point buy total exceeded. Used {total_cost}/{self.POINT_BUY_TOTAL}."
            )

        return [assignment[stat] for stat in self.STAT_ORDER]

    # ==========================================================
    # UTILITIES
    # ==========================================================

    @staticmethod
    def calculate_modifier(score: int) -> int:
        """Return D&D 5e ability modifier."""
        return (score - 10) // 2
