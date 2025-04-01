from personaje import Personaje

class Enemy(Personaje):
    def __init__(self, imagen, x, y):
        super().__init__(imagen, x, y)


    def avanzar(self, speed):
        self.ubicacion_x = self.ubicacion_x - speed

    def esta_fuera(self):
        if self.ubicacion_x < -100:
            return True


