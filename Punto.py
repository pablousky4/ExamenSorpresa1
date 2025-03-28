import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"X={self.x}, Y={self.y}"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Esta en el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Esta en el eje X"
        else:
            return "esta en origen"
        
    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)
    
    