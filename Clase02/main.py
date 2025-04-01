import pygame
from dino import Dino
from enemy import Enemy

dino1 = Dino()
enemy1 = Enemy()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill((247, 247, 247))
    #ACA COLOCAR CODIGO

    dino1.dibujar(SCREEN)
    enemy1.dibujar(SCREEN)


    pygame.display.flip()
    pygame.time.Clock().tick(100)