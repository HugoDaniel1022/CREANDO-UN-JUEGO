import pygame

class Dino():
    def __init__(self):
        self.ancho = 113
        self.alto = 113
        self.ubicacion_y = 450
        self.ubicacion_x = 500
        self.image = pygame.image.load('C:/Users/Usuario/Desktop/creando un juego/dino2.jpeg')

    def dibujar(self, screen):
        screen.blit(self.image, (self.ubicacion_x, self.ubicacion_y))

    def si_colisiono(self, elmalo):
        if elmalo.ubicacion_x + elmalo.ancho > self.ubicacion_x and self.ubicacion_y + self.alto > elmalo.ubicacion_y:
            print('colisionó')


    def saltar(self):
        self.ubicacion_y = 337
    
    def bajar(self):
        self.ubicacion_y = 450