from typing import Optional

from hero import Hero

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        
        return cls._instances[cls]

class Game_Singleton(metaclass=SingletonMeta):
    
    def __init__(self):
        self.player = None
        self.enemy = None
        self.game_processing = False
        self.game_result = ''


    def run(self, player: Hero, enemy: Hero):
        self.player = player
        self.enemy = enemy
        self.game_processing = True


    def _check_hp(self) -> Optional[str]:
        if self.player.hp <= 0 and self.enemy.hp <= 0:
            return self._end_game(result='КО')
        if self.player.hp <= 0:
            return self._end_game(result='You lost')
        if self.enemy.hp <= 0:
            return self._end_game(result='You won')
        else:
            return None


    def _end_game(self, result: str):
        self.game_processing = False
        self.game_result = result

        return result


    def next_turn(self) -> str:
        if result := self._check_hp():
            return result

        if not self.game_processing:
            return self.game_result

        result = self.enemy_hit()

        self._stamina_regenerate()

        return result


    def _stamina_regenerate(self):
        self.player.regenerate_stamina()
        self.enemy.regenerate_stamina()

    
    def player_hit(self) -> str:
        dealt_damage: Optional[float] = self.player.hit(self.enemy)
       
        if dealt_damage is not None:
            self.enemy.take_hit(dealt_damage)
       
            return f'<p>The enemy recieved {dealt_damage} damage</p><p>{self.next_turn()}</p>'
        return f"<p>You failed to hit the enemy — you don't have enough stamina</p><p>{self.next_turn()}</p>"


    def enemy_hit(self) -> str:
        dealt_damage: Optional[float] = self.enemy.hit(self.player)
       
        if dealt_damage is not None:
            self.player.take_hit(dealt_damage)
       
            result = f'You have received {dealt_damage} damage'
        else:
            result = f"The enemy failed to hit you — they don't have enough stamina"

        return result

    
    def player_use_skill(self) -> str:
        dealt_damage: Optional[float] = self.player.use_skill()

        if dealt_damage is not None:
            self.enemy.take_hit(dealt_damage)

            return f'<p>You used the skill and dealt {dealt_damage} damage to the enemy</p><p>{self.next_turn()}</p>'
        if self.player.skill_used:
            return f'<p>You have already used the skill</p><p>{self.next_turn()}</p>'

        return f"<p>You can't use the skill — you don't have enough stamina</p><p>{self.next_turn()}</p>"
            