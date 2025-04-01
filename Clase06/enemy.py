import pygame

class Enemy():
    def __init__(self):
        self.ancho = 113
        self.alto = 113
        self.ubicacion_x = 750
        self.ubicacion_y = 450
        self.image = pygame.image.load("C:/Users/Usuario/Desktop/creando un juego/Clase06/images/cactus.jpeg")
        
    def dibujar(self, pantalla):
        pantalla.blit(self.image, (self.ubicacion_x, self.ubicacion_y))

    def avanzar(self, speed):
        self.ubicacion_x = self.ubicacion_x - speed

    def esta_fuera(self):
        if self.ubicacion_x < -100:
            return True