from dataclasses import dataclass


@dataclass
class Skill():
    name: str = NotImplemented
    attack: float = NotImplemented
    stamina: float = NotImplemented

ferocious_kick = Skill(name = "Ferocious kick", attack = 12, stamina = 6)
powerful_sting = Skill(name = "Powerful sting", attack = 15, stamina = 5)