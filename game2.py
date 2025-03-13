import random
skils1= { "Здоровье": 6 , "Сила":8 , "Ловкость":2 , "Интелект":2 ,}
skils2= { 'Здоровье': 5, 'Сила':3 , 'Ловкость':3 , 'Интелект':9 ,}
skils23={ "Здоровье": 5, "Сила":3 , "Ловкость":8 , "Интелект":5, }
c = 'рыцарь'
b = 'маг'
d= 'лучник'

while True:
    print(c,b,d, sep='\n')
    a=int(input("""Если хотите играть за рыцаря выберите:1\n""" """Если хотите играть за мага нажмите:2\n""" """Если хотите играть за лучника нажмите:3\n"""))
    
    try:
            
            if a==1:
                character=c
                break
            elif a==2:
                character=b
                break
            elif a==3:
                character=d
                break
            else:
                print("Введите соответсвующее число")
    except ValueError:
            print("введите  ЧИСЛО ")
import time
for i in range(3):
     print(".",end="")
     time.sleep(1.5)
print("dadad")
print('Вы столкнулись с противником')
guess1 = input('сбежать или атаковать')
if guess1=='сбежать':
    randBox =skils2['Ловкость']+ random.randint(1,21)
    if randBox > 20:
        print('Вам удалось сбежать')
    else:
        print('Вы не смогли сбежать')
        

