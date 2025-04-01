import pygame
from dino import Dino
from enemy import Enemy

dino1 = Dino()
enemys = []
speed = 1

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()

pygame.font.init()
font = pygame.font.Font(None, 36)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dino1.saltar()

    SCREEN.fill((247, 247, 247))
    #ACA COLOCAR CODIGO

    score_text = font.render(f"Puntaje: {dino1.score}", True, (0,0,0))
    SCREEN.blit(score_text, (300, 150))


    if len(enemys) == 0:
        enemy1 = Enemy()
        enemys.append(enemy1)
    
    if len(enemys) != 0 and dino1.esta_vivo:
        for i in enemys:
            i.dibujar(SCREEN)
            i.avanzar(speed)
            dino1.si_colisiono(i)
            if i.esta_fuera():
                enemys.remove(i)


    dino1.update(SCREEN, speed)
    speed += 0.001

    pygame.display.flip()
    pygame.time.Clock().tick(100)