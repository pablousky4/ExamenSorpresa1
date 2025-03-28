from Punto import Punto
from Rectangulo import Rectangulo

def crear_punto(nombre):
    x = float(input(f"Dime la coordenada X de {nombre}: "))
    y = float(input(f"Dime la coordenada Y de {nombre}: "))
    return Punto(x, y)

def main():
    puntos = {}
    rectangulos = []
    nombres = []
    
    while True:
        nombre = input("Dime el nombre del punto (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        puntos[nombre] = crear_punto(nombre)
        nombres.append(nombre)
        
        if len(nombres) % 4 == 0:
            rectangulos.append(Rectangulo(puntos[nombres[-4]], puntos[nombres[-3]], puntos[nombres[-2]], puntos[nombres[-1]]))
            print(f"Se ha creado un rectángulo con los puntos: {nombres[-4:]}")
    
    for nombre, punto in puntos.items():
        print(f"{nombre}: {punto}, {punto.cuadrante()}")
    
    if len(puntos) > 1:
        for i in range(len(nombres) - 1):
            for j in range(i + 1, len(nombres)):
                punto1 = puntos[nombres[i]]
                punto2 = puntos[nombres[j]]
                print(f"Vector de {nombres[i]} a {nombres[j]}: {punto1.vector(punto2)}")
                print(f"Distancia entre {nombres[i]} y {nombres[j]}: {punto1.distancia(punto2)}")
    
    for i, rect in enumerate(rectangulos, 1):
        print(f"Rectángulo {i}: {rect}")
        print(f"Área: {rect.area()}")
        print(f"Perímetro: {rect.perimetro()}")
        print("-")

if __name__ == "__main__":
    main()
