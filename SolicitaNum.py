# Actividad solicitar numero
numero = int(input("Ingrese un número: "))

while numero <= 100:
    print("El número ingresado es menor o igual a 100. Por favor, ingrese un número mayor a 100.")
    numero = int(input("Ingrese un número: "))

print("Has ingresado un número mayor a 100.")