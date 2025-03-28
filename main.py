import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"X={self.x}, Y={self.y}"