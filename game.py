import time
import random
import pygame

class Hero:
    def __init__(self, name, strong,intell):
        self.name=name
        self.strong=strong
        self.intell=intell


hero_name = input('Добро пожаловать герой. Как тебя зовут?')
hero=Hero(hero_name, 10, 5)
print(f'{hero.name}, твой уровень силы {hero.strong}')
time.sleep(3)
print(f'{hero.name} ты встретил опасность и тебе нужно сразиться, ты сделаешь это? да или нет?')
answ=input('Да или нет? Неприятель очень опасен, я бы подумал дважды... ')
if answ == 'да':
    form=hero.strong*random.randint(1,3)
    if form>18:
        print('Вы победили')
    else:
        print('Вы проиграли')
        hero.strong=0
    


