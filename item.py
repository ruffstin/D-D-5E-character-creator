# item.py
# item has properties, weight, currency cost, item description
# 		Weapons(simple/martial, melee/ranged, light/heavy/finesse, two-handed, versatile)
# 		magical item -> cost, type(common, uncommon, rare, very rare, legendary), description, could be a weapon

# 	item class -> can be weapon, can be magical


class Item: 
    def __init__(self, name: str, description: str = "", weight: float = 0.0, cost: int = 0, currency: str = "gp",
                 is_weapon: bool = False, weapon_type: str = None, properties: list[str] = None, 
                 is_magical: bool = False, rarity: str = None, magic_type: str = None):
        
        self.name = name
        self.description = description
        self.weight = weight
        self.cost = cost 
        self.currency = currency # e.g., 'gp', 'sp', 'cp', 'ep', 'pp
        self.is_weapon = is_weapon
        self.weapon_type = weapon_type  # e.g., 'simple melee', 'martial ranged'
        self.properties = properties or []  # e.g., ['light', 'finesse', 'two-handed']
        self.is_magical = is_magical
        self.rarity = rarity  # e.g., 'common', 'uncommon', 'rare', 'very rare', 'legendary'
        self.magic_type = magic_type  # e.g., 'weapon', 'armor', etc.

    def __str__(self):
        s = f"{self.name} ({self.weight} lb, {self.cost} {self.currency})"
        if self.is_weapon:
            s += f" [Weapon: {self.weapon_type}, Properties: {', '.join(self.properties)}]"
        if self.is_magical:
            s += f" [Magic: {self.rarity or ''} {self.magic_type or ''}]"
        if self.description:
            s += f"\n  {self.description}"
        return s