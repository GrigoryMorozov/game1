import time


class Hero:
    def __init__(self, name, health=100, mana=100, level=1):
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level

    def attack(self, damage):
        self.health -= damage


startGame = True

while startGame:
    print('Добро пожаловать в игру')
    time.sleep(2)

