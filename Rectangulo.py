from Punto import Punto

class Rectangulo:
    def __init__(self, p1, p2, p3, p4):
        """
        Inicializa un rectángulo con cuatro puntos.
        Se asume que los puntos están dados en orden y forman un rectángulo.
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def area(self):
        """
        Calcula el área del rectángulo.
        Se asume que los lados opuestos son paralelos y perpendiculares.
        """
        base = self.p1.distancia(self.p2)
        altura = self.p2.distancia(self.p3)
        return base * altura

    def perimetro(self):
        """
        Calcula el perímetro del rectángulo.
        """
        base = self.p1.distancia(self.p2)
        altura = self.p2.distancia(self.p3)
        return 2 * (base + altura)

    def __str__(self):
        """
        Representación en cadena del rectángulo.
        """
        return f"Rectángulo formado por los puntos {self.p1}, {self.p2}, {self.p3}, {self.p4}"