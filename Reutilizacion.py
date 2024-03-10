# Actividad Reutilizacion cod

def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero positivo.")
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

numero = int(input("Ingrese un número entero positivo: "))
try:
    print(f"El factorial de {numero} es: {factorial(numero)}")
except ValueError as ve:
    print(ve)