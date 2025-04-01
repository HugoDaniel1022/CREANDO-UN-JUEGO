import pygame

class Dino():
    def __init__(self):
        self.ancho = 113
        self.alto = 113
        self.ubicacion_y = 450
        self.ubicacion_x = 100
        self.image = pygame.image.load('C:/Users/Usuario/Desktop/creando un juego/Clase05/dino.jpeg')
        self.dino_jump = False


    def dibujar(self, screen):
        screen.blit(self.image, (self.ubicacion_x, self.ubicacion_y))

    def si_colisiono(self, elmalo):
        if (elmalo.ubicacion_x + elmalo.ancho > self.ubicacion_x and elmalo.ubicacion_x < self.ubicacion_x + self.ancho) and (self.ubicacion_y + self.alto > elmalo.ubicacion_y):
            print('colisionó')

                
    def saltar(self):
        self.dino_jump = True
        

    def update(self):
        if self.dino_jump == True and self.ubicacion_y > 200:
            self.ubicacion_y -= 1
            if self.ubicacion_y == 200:
                self.dino_jump = False
        if self.dino_jump == False and self.ubicacion_y < 450 :
            self.ubicacion_y += 1