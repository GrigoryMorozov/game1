
class Hero:
    def __init__(self, name, level, health, strength, agility):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.agility = agility

    def attack(self, enemy):
        print(f"{self.name} аттакует {enemy}")

    def heal(self):
        print(f"{self.name} восстанавливает здоровье")

    def move(self, direction):
        print(f'{self.name} двигается в направлении {direction}')
