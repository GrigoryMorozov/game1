from hero import Hero


def main():
    name = input('Как зовут тебя, воин?')
    level = 1
    strength = 5
    agility = 3
    health = 5

    hero = Hero(name, level, health, strength, agility)

    print(f'{hero.name}, здравствуй!')
    print(f'{hero.health} это твое здоровье')
    hero.health = 2

    print(f'{hero.health} теперь вот такое твоё здоровье')

main()
