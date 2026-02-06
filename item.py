# item.py
# item has properties, weight, currency cost, item description
# 		Weapons(simple/martial, melee/ranged, light/heavy/finesse, two-handed, versatile)
# 		magical item -> cost, type(common, uncommon, rare, very rare, legendary), description, could be a weapon

# 	item class -> can be weapon, can be magical


class Item: 
    def __init__(self, name: str, description: str = "", weight: float = 0.0, cost: int = 0, currency: str = "gp",
                 is_weapon: bool = False, weapon_type: str = None, properties: list[str] = None, damage_type: str = None, 
                 damage_die: int = None, versatile_damage_die: int = None,  armor_type = None, armor_class: int = 0, 
                 str_requirement: int = 0, add_dex_to_ac: bool = False, disadvantage_stealth: bool = False, 
                 is_magical: bool = False, rarity: str = None, magic_type: str = None, magic_bonus: int = 0):
        
        self.name = name
        self.description = description
        self.weight = weight
        self.cost = cost 
        self.currency = currency # e.g., 'gp', 'sp', 'cp', 'ep', 'pp
        self.is_weapon = is_weapon
        self.weapon_type = weapon_type  # e.g., 'simple melee', 'martial ranged'
        self.properties = properties or []  # e.g., ['light', 'finesse', 'two-handed']
        self.damage_type = damage_type  # e.g., 'slashing', 'piercing', 'bludgeoning' (for weapons)
        self.damage_die = damage_die # e.g., '1d6', '1d8' (for weapons)
        self.versatile_damage_die = versatile_damage_die # e.g., '1d8', '1d10' (for versatile weapons)
        self.armor_type = armor_type # e.g., 'light', 'medium', 'heavy'
        self.armor_class = armor_class # e.g., 11 for leather armor (for armor) 2 for shield
        self.str_requirement = str_requirement # e.g., 13 for heavy armor (for armor)
        self.add_dex_to_ac = add_dex_to_ac # True if armor allows adding Dexterity modifier to AC (for armor)
        self.disadvantage_stealth = disadvantage_stealth # True if armor gives disadvantage on stealth checks (for armor)
        self.is_magical = is_magical
        self.rarity = rarity  # e.g., 'common', 'uncommon', 'rare', 'very rare', 'legendary'
        self.magic_type = magic_type  # e.g., 'weapon', 'armor', etc.
        self.magic_bonus = magic_bonus # e.g., +1, +2, +3 for magical weapons/armor

    def get_armor_class(self):
        if self.armor_type:
            return self.armor_class
        return 0
    
    

    def __str__(self):
        s = f"{self.name} ({self.weight} lb, {self.cost} {self.currency})"
        if self.is_weapon:
            s += f" [Weapon: {self.weapon_type}, Properties: {', '.join(self.properties)}]"
        if self.armor_type:
            s += f" [Armor: {self.armor_type}]"
        if self.is_magical:
            s += f" [Magic: {self.rarity or ''} {self.magic_type or ''}]"
        if self.description:
            s += f"\n  {self.description}"
        return s