#Actividad ValueError

try:
    numero = float(input("Ingrese un número: "))
    if numero < 0:
        raise ValueError("El número ingresado es menor que cero.")
    else:
        print("Número válido ingresado:", numero)
except ValueError as ve:
    print(ve)
