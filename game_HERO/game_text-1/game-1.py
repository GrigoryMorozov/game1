import time
import pygame
import threading


#  функция для плавного появления текста
def pd(text, delay = 0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# функция для музыки
    
def play_music(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1)  # -1 означает бесконечное повторение

def stop_music():
    pygame.mixer.music.stop()

 
def main():
    play_music('assets/music/01 - Opening.ogg')
    pd('''----------------------------------------
--------------Подземелье дракона--------
----------------------------------------''')
    stop_music()
    
    play_music('assets/music/09 - Z 339 - Here the Deities approve.ogg')
    pd('''В дни, когда земля помнила гул древних битв,
а магия жила в трещинах скал, рыцарь в сверкающих
доспехах шагнул к замку-исполину.
Тучи сплелись над его башнями, словно сама тьма выткала саван.
Руны на клинке вспыхивали синевой — клятва, выжженная в стали: «Спасти короля любой ценой".
Полный решимости и мужества, рыцарь направился на миссию,
мечтая о славе и героических подвигах.
Однако, по дороге к замку, он не заметил,
как свернул на узкую тропинку, завуалированную туманом.
Вскоре вокруг него начали расти густые деревья,
а звук его доспехов стал заглушаться шёпотом ветра.
Он понял, что попал в страшный лес, о котором ходили жуткие слухи. 
''')
    stop_music()
    

    play_music('assets/music/13 - Danger.ogg')
    pd('''Темнота сгущалась, а шорохи вокруг
становились всё настойчивее.
Вдруг из-за деревьев вышел старик
с длинной белой бородой и загадочным взглядом.
Он был одет в рваную одежду, и его лицо было испещрено морщинами.
Старик (слабый, хриплый голос, опираясь на посох). 
"О, доблестный рыцарь... Вижу, судьба привела тебя сюда неспроста.
Помоги старцу... Мой амулет, древний оберег, потерян среди корней
вековых деревьев.
Найди его — и я дам тебе то,
что спасёт тебя тогда, когда ты сам не будешь ожидать".
Старик кашляет, в его глазах отражается вековая мудрость. 
"Время бежит... но без оберега я обречён..."  
''')

   
    
    answer = int(input('Вариант 1: помочь старику. Вариант 2: Отказаться'))
    stop_music()
    if answer == 1:
        play_music('assets/music/14 - Barbarian King.ogg')
        pd('''Рыцарь:
"Укажи, где искать и я постараюсь сделать всё возможное.
Не оставлю тебя в беде,но у меня мало времени,старче.
Надеюсь, ваш амулет действительно вам так дорог."  
Старик (благодарно):
"Ищи у старого дуба...
Там, где большие корни уходят глубоко в землю, а рядом бьёт небольшой ключ..."  
Артур сделал, как и сказал старик: отправился искать могучий дуб.
После некоторых скитаний он увидел его:
раскидистое древо закрывало собой солнце, а из под земли бил ключ.
Артур внимательно оглядел дерево и увидел спрятанное ветвями дупло.
Не долго думая, рыцарь начал карабкаться по коре и вскоре он увидел
небольшой амулет с цепочкой.
Забрав его, Артур вернулся той же дорогой к старцу,
который  с благодарностью принял потерянное.

Старик (вручает сияющий амулет): 
"Возьми этот артефакт...Мне он больше не понадобится. Амулет выбрал тебя своим свечением. Он впитал силу древних. Когда тьма сомкнёт кольцо — сожми его в ладони, и свет прорвётся сквозь мрак."  
Рыцарь: "Благодарю. Теперь и вы сможете уйти отсюда?"  
Старик (таинственно): "Мой путь иной... Иди, спаси короля. Твой час близок." 
''')
        stop_music()

    elif answer == 2:
        play_music('assets/music/11 - Ostrich!.ogg')
        pd('''Рыцарь (сурово,но с уважением):
"Прости, старик. Мой король ждёт меня.
Мне доверили важную миссию и я не могу её провалить. "  
Старик (грустно и с упрёком ):
"Судьба накажет твоё безразличие..."  
Артур, немного плутая выходит к замку и сурово толкает тяжёлые двери.  
''')
        stop_music()        
        
    



if __name__ == "__main__":
    main()
