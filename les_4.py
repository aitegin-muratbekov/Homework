from enum import Enum
import random

class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HILL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage, public__field):
        self.__name =name
        self.__health = health
        self.__damage = damage
        self.public__field

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health : {self.__health} damage: {self.__damage}'

class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)
        self.__defence = None
    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        self.__defence = value

    def hit(self, heroes):
        pass

    def __str__(self):
        return f'Boss {GameEntity.__str__()} defence: ' \
               f'{self.__defence}'

class Hero(GameEntity):
        def __init__(self, name, health, damage, super_ability):
            GameEntity.__init__(self, name, health, damage)
            if not isinstance(super_ability, SuperAbility):
                self.__super_ability = None
                raise AttributeError('Wrong data type for super_ability')
            else:
                self.__super_ability = super_ability

        @property
        def super_ability(self):
            return self.__super_ability

        @super_ability.setter
        def super_ability(self, value):
            self.__super_ability = value

        def hit(self, boss):
            boss.health -= self.damage

        def apply_super_ability(self, boss, heroes):
            pass

class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)

class Healer(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, SuperAbility.HILL)
        self.__heal_points = heal_points

class Magic(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, health, damage, name, SuperAbility.BOOST)
        pass

class Berserk(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, health, damage, name, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0
round_counter = 0

def start():
    boss = Boss("Alex", 1000, 50)
    warrior = Warrior('Егор', 280, 10)
    doc = Medic('Aibolot', 250, 5, 15)
    magic = Magic('Merlin', 260, 20)
    berserk = Berserk('Viking', 270, 15)
    assistant = Medic('Watson', 290, 10, 5)
    heroes_list = [boss, warrior, doc, magic, berserk, assistant]

def print_statistics(boss, heroes):
    print(f'Round{round_counter}.........')
    print(boss)
    for hero in heroes:
        print(hero)

def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        return('Boss won!!')



