import pygame
from dino import Dino

dino1 = Dino()

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
    
    SCREEN.blit(dino1.image, (dino1.ubicacion_x, dino1.ubicacion_y))

    pygame.display.flip()
    pygame.time.Clock().tick(100)