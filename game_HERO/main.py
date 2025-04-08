import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((800, 400))
font = pygame.font.Font(None, 20)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        rep = 'hello'
        text1 = font.render(rep, True, (0, 100, 0))
        place1 = text1.get_rect(center=(200, 150))
        screen.blit(text1, place1)
        pygame.display.update()
        time.sleep(2)
        rep = 'Me'
        screen.blit(text1, place1)
        pygame.display.update()
        pygame.display.flip()
