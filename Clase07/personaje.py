class Personaje():
        def __init__(self, imagen, x, y):
            self.ancho = 113
            self.alto = 113
            self.ubicacion_y = y
            self.ubicacion_x = x
            self.image = imagen

        def dibujar(self, screen):
            screen.blit(self.image, (self.ubicacion_x, self.ubicacion_y))