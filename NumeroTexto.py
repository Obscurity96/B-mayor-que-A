# Actividad número como texto
numero_texto = input("Ingrese un número: ")

# Convertir el texto a entero
try:
    numero = int(numero_texto)
    print("El número ingresado es:", numero)
except ValueError:
    print("No se ingresó un número.")