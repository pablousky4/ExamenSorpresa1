from Punto import Punto

def crear_punto(nombre):
    x = float(input(f"Dime la coordenada X de {nombre}: "))
    y = float(input(f"Dimee la coordenada Y de {nombre}: "))
    return Punto(x, y)

