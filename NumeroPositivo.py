# Actividad numero positivo

# Pedir al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Verificar si el número es positivo, negativo o cero
if numero > 0:
    print("El número ingresado es positivo.")
elif numero < 0:
    print("El número ingresado es negativo.")
else:
    print("El número ingresado es cero.")