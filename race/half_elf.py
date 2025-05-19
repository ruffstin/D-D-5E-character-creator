# half_elf.py
from .race import Race

class HalfElf(Race):
    def __init__(self):
        super().__init__("Half-Elf", None)
        self.set_bonuses()

    def set_bonuses(self):
        # All half-elves get +2 CHA and +1 to two other stats
        self.bonuses = {"CHA": 2}

        # we are not prompting the user yet so we will not set any other bonuses yet

