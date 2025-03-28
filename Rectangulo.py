from Punto import Punto

class Rectangulo:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def area(self):
        base = self.p1.distancia(self.p2)
        altura = self.p2.distancia(self.p3)
        return base * altura

    def perimetro(self):
        base = self.p1.distancia(self.p2)
        altura = self.p2.distancia(self.p3)
        return 2 * (base + altura)

    def __str__(self):
        return f"Rectángulo formado por los puntos {self.p1}, {self.p2}, {self.p3}, {self.p4}"