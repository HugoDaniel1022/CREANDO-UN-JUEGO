import pygame

class Dino():
    def __init__(self):
        self.ancho = 113
        self.alto = 113
        self.ubicacion_y = 450
        self.ubicacion_x = 100
        self.image = pygame.image.load('C:/Users/Usuario/Desktop/creando un juego/Clase06/images/dino.jpeg')
        self.dino_jump = False
        self.score = 0
        self.esta_vivo = True


    def dibujar(self, screen):
        screen.blit(self.image, (self.ubicacion_x, self.ubicacion_y))

    def si_colisiono(self, elmalo):
        if (elmalo.ubicacion_x + elmalo.ancho > self.ubicacion_x and elmalo.ubicacion_x < self.ubicacion_x + self.ancho) and (self.ubicacion_y + self.alto > elmalo.ubicacion_y):
            self.esta_vivo = False
                
    def saltar(self):
        self.dino_jump = True
        

    def update(self, pantalla, speed):
        if self.esta_vivo == True:
            self.dibujar(pantalla)
            self.score += 1 
            if self.dino_jump == True and self.ubicacion_y > 150:
                self.ubicacion_y -= speed
                if self.ubicacion_y < 151:
                    self.dino_jump = False
            if self.dino_jump == False and self.ubicacion_y < 450 :
                self.ubicacion_y += speed
        else:
            pantalla.blit(pygame.image.load("C:/Users/Usuario/Desktop/creando un juego/Clase06/images/GameOver.png"), (200,200))