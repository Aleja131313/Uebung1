import math

class Vektor3:
    def __init__ (self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def len (self):
        resultado = math.sqrt (self._x ** 2 + self._y ** 2 + self._z ** 2)
        return resultado

Vektor = Vektor3 (20, 30, 10)

print (Vektor.len ())

