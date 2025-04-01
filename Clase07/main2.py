import pygame
from enemy import Enemy
from dino import Dino



imagen_dino = pygame.image.load('C:/Users/Usuario/Desktop/creando un juego/Clase07/images/dino.jpeg')
imagen_enemigo = pygame.image.load('C:/Users/Usuario/Desktop/creando un juego/Clase07/images/cactus.jpeg')
enemy1 = Enemy(imagen_enemigo, 500, 450)
dino1 = Dino(imagen_dino, 100, 450)

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