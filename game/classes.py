from abc import ABC
from typing import Dict, Type
import skills as skills


class Unit(ABC):
   name: str = NotImplemented
   max_health: float = NotImplemented
   max_stamina: float = NotImplemented
   attack: float = NotImplemented
   stamina: float = NotImplemented
   armor: float = NotImplemented
   skill: skills.Skill = NotImplemented

class Warrior(Unit):
    name: str = "Warrior"
    max_health: float = 60.0
    max_stamina: float = 30.0
    attack: float = 0.8
    stamina: float = 0.9
    armor: float = 1.2
    skill: skills.Skill = skills.ferocious_kick

class Thief(Unit):
    name: str = "Thief"
    max_health: float = 50.0
    max_stamina: float = 25.0
    attack: float = 1.5
    stamina: float = 1.2
    armor: float = 1.0
    skill: skills.Skill = skills.powerful_sting


classes: Dict[str, Type[Unit]] = {
    Warrior.name: Warrior,
    Thief.name: Thief,
}