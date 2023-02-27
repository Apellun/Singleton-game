from dataclasses import dataclass
from typing import List
from random import uniform

@dataclass
class Weapon:
    id: int = NotImplemented
    name: str = NotImplemented
    min_damage: float = NotImplemented
    max_damage: float = NotImplemented
    stamina_per_hit: float = NotImplemented

    @property
    def damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)



@dataclass
class Armor:
    id: int = NotImplemented
    name: str = NotImplemented
    defence: float = NotImplemented
    stamina_per_turn: float = NotImplemented



@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]


    def get_weapon(self, weapon_name: str) -> Weapon:
        for weapon in self.weapons:
            if weapon.name == weapon_name:
                return weapon
        return RuntimeError

    def get_armor(self, armor_name: str) -> Armor:
        for armor in self.armors:
            if armor.name == armor_name:
                return armor
        return RuntimeError

    @property
    def weapon_names(self) -> List[str]:
        return [item.name for item in self.weapons]

    @property
    def armor_names(self) -> List[str]:
        return [item.name for item in self.armors]