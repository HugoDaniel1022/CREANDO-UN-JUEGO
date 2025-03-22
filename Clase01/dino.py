import pygame

class Dino():
    def __init__(self):
        self.ubicacion_y = 450
        self.ubicacion_x = 500
        self.image = pygame.image.load('C:/Users/Usuario/Desktop/creando un juego/Clase01/dino2.jpeg')

    def dibujar(self, screen):
        screen.blit(self.image, (self.ubicacion_x, self.ubicacion_y))