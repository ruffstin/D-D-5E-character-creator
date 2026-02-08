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
                 dex_modifier_max: int = None, is_magical: bool = False, rarity: str = None, magic_type: str = None, 
                 magic_bonus: int = 0):
        
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
        self.dex_modifier_max = dex_modifier_max # e.g., 2 for medium armor (max +2 Dex), None for no cap, 0 for no Dex (shields/heavy armor)
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
import json
from pathlib import Path
from typing import Any, Dict, Optional

# Template support
TEMPLATES: Dict[str, Dict[str, Any]] = {}

def _flatten_templates(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Recursively flatten nested template dict into single-level lookup."""
    flat = {}
    for key, value in data.items():
        if isinstance(value, dict):
            if "name" in value or "contents" in value:
                # It's a template (has name or is a pack with contents)
                flat[key] = value
            else:
                # It's a category dict, recurse
                flat.update(_flatten_templates(value))
    return flat

def load_item_templates(path: str = "item_data/item_templates.json") -> None:
    p = Path(path)
    if not p.exists():
        return
    with p.open("r", encoding="utf-8") as f:
        data = json.load(f)
    TEMPLATES.clear()
    flat = _flatten_templates(data)
    TEMPLATES.update(flat)

def _resolve_template(name: str, seen: Optional[set] = None) -> Dict[str, Any]:
    seen = seen or set()
    if name in seen:
        raise ValueError(f"Circular template inheritance for '{name}'")
    seen.add(name)
    tpl = TEMPLATES.get(name)
    if not tpl:
        raise KeyError(f"Template '{name}' not found")
    base_name = tpl.get("base")
    if base_name:
        base = _resolve_template(base_name, seen)
        merged = dict(base)
        merged.update({k: v for k, v in tpl.items() if k != "base"})
        return merged
    return dict(tpl)

def create_item_from_template(template_name: str, overrides: Optional[Dict[str, Any]] = None) -> Item:
    if not TEMPLATES:
        # try default load path
        load_item_templates()
    tpl = _resolve_template(template_name)
    if overrides:
        tpl.update(overrides)
    # Map template keys to Item constructor args (ignore unknown keys)
    kwargs = {
        "name": tpl.get("name", template_name),
        "description": tpl.get("description", ""),
        "weight": tpl.get("weight", 0.0),
        "cost": tpl.get("cost", 0),
        "currency": tpl.get("currency", "gp"),
        "is_weapon": tpl.get("is_weapon", False),
        "weapon_type": tpl.get("weapon_type"),
        "properties": tpl.get("properties"),
        "damage_type": tpl.get("damage_type"),
        "damage_die": tpl.get("damage_die"),
        "versatile_damage_die": tpl.get("versatile_damage_die"),
        "armor_type": tpl.get("armor_type"),
        "armor_class": tpl.get("armor_class", 0),
        "str_requirement": tpl.get("str_requirement", 0),
        "add_dex_to_ac": tpl.get("add_dex_to_ac", False),
        "disadvantage_stealth": tpl.get("disadvantage_stealth", False),
        "dex_modifier_max": tpl.get("dex_modifier_max"),
        "is_magical": tpl.get("is_magical", False),
        "rarity": tpl.get("rarity"),
        "magic_type": tpl.get("magic_type"),
        "magic_bonus": tpl.get("magic_bonus", 0),
    }
    return Item(**kwargs)

def add_pack_to_character(character, pack_name: str) -> None:
    """Add a pack item and all its contents to a character's inventory.
    
    Args:
        character: Character object with add_item(item, quantity) method
        pack_name: Template key of the pack (e.g., 'explorers_pack')
    
    Raises:
        KeyError: If pack template not found
        ValueError: If template is not a pack
    """
    if not TEMPLATES:
        load_item_templates()
    
    pack_template = _resolve_template(pack_name)
    
    if not pack_template.get("is_pack"):
        raise ValueError(f"'{pack_name}' is not a pack template (missing 'is_pack': true)")
    
    # Add the pack item itself
    pack_item = create_item_from_template(pack_name)
    character.add_item(pack_item, 1)
    
    # Add all contents
    for item_key, quantity in pack_template.get("contents", {}).items():
        item = create_item_from_template(item_key)
        character.add_item(item, quantity)