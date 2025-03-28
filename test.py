import pygame as pg
import sys
import time

pg.init()

sc = pg.display.set_mode((800, 400))

# тут рисуем
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


def title_game():
    font = pg.font.Font(None, 72)
    title_game = 'Рыцарь и спасение короля'
    text = font.render(title_game, True, YELLOW)
    pg.draw.line(sc, WHITE, [200, 100], [600, 100], 3)
    pg.draw.line(sc, WHITE, [200, 300], [600, 300], 3)


def scene_1():
    font = pg.font.Font(None, 30)
    text_scene = '''На фоне гремящих боевых звуков и криков сражающихся армий,
    мы видим рыцаря, стоящего на холме. Его доспехи сверкают
    подсолнечными лучами, а в его сердце горит решимость спасти короля,
    похищенного в таинственном замке, окутанном мрачными легендами'''
    text = font.render(text_scene, True, WHITE)


while True:
    for i in pg.event.get():
        if i:.type == pg.QUIT:
            pg.quit()
            sys.exit()
    place =
    sc.blint(title_game(), place)
    pg.display.flip()
