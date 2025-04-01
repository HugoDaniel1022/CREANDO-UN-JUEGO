import pygame

class Enemy():
    def __init__(self):
        self.ancho = 113
        self.alto = 113
        self.ubicacion_x = 800
        self.ubicacion_y = 450
        self.image = pygame.image.load("C:/Users/Usuario/Desktop/creando un juego/Clase04/cactus.jpeg")
        
    def dibujar(self, pantalla):
        pantalla.blit(self.image, (self.ubicacion_x, self.ubicacion_y))

    def avanzar(self):
        self.ubicacion_x = self.ubicacion_x - 1