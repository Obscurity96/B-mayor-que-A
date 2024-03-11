import math

# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2

# Función para calcular el perímetro de un círculo
def perimetro_circulo(radio):
    return 2 * math.pi * radio

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# Función para calcular el área de un cuadrado
def area_cuadrado(lado):
    return lado ** 2

# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

# Función para calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura

# Función para mostrar el menú y obtener la opción del usuario
def obtener_opcion():
    print("1. Círculo")
    print("2. Triángulo")
    print("3. Cuadrado/Rectángulo")
    opcion = input("Seleccione la figura geométrica (1/2/3): ")
    return opcion

# Función principal
def main():
    opcion = obtener_opcion()

    if opcion == "1":  # Círculo
        radio = float(input("Ingrese el radio del círculo: "))
        print("Área del círculo:", area_circulo(radio))
        print("Perímetro del círculo:", perimetro_circulo(radio))
    elif opcion == "2":  # Triángulo
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("Área del triángulo:", area_triangulo(base, altura))
    elif opcion == "3":  # Cuadrado/Rectángulo
        lado = float(input("Ingrese el lado del cuadrado/rectángulo: "))
        print("Área del cuadrado/rectángulo:", area_cuadrado(lado))
    else:
        print("Opción no válida")

# Llamada a la función principal
main()
