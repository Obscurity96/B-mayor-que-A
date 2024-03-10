# Actividad solicitar numeros y dividir

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Realizar la división
if numero2 != 0:
    resultado = numero1 / numero2
    print("El resultado de la división es:", resultado)
else:
    print("No se puede dividir entre cero.")