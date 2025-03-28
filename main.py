from Punto import Punto

def crear_punto(nombre):
    x = float(input(f"Dime la coordenada X de {nombre}: "))
    y = float(input(f"Dimee la coordenada Y de {nombre}: "))
    return Punto(x, y)

def main():
    puntos = {}
    
    while True:
        nombre = input("Dime el nombre del punto (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        puntos[nombre] = crear_punto(nombre)

    for nombre, punto in puntos.items():
        print(f"{nombre}: {punto}, {punto.cuadrante()}")

    if len(puntos) > 1:
        nombres = list(puntos.keys())
        for i in range(len(nombres) - 1):
            for j in range(i + 1, len(nombres)):
                punto1 = puntos[nombres[i]]
                punto2 = puntos[nombres[j]]
                print(f"Vector de {nombres[i]} a {nombres[j]}: {punto1.vector(punto2)}")
                print(f"Distancia entre {nombres[i]} y {nombres[j]}: {punto1.distancia(punto2)}")


