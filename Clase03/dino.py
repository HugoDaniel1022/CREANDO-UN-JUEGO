import pygame

class Dino():
    def __init__(self):
        self.ancho = 113
        self.alto = 113
        self.ubicacion_y = 450
        self.ubicacion_x = 100
        self.image = pygame.image.load('C:/Users/Usuario/Desktop/creando un juego/Clase03/dino.jpeg')

    def dibujar(self, screen):
        screen.blit(self.image, (self.ubicacion_x, self.ubicacion_y))

    def saltar(self):
        self.ubicacion_y = 350
    
    def bajar(self):
        self.ubicacion_y = 450