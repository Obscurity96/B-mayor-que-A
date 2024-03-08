# Actividad Aumento de salario

salario = float(input("Ingresar el sueldo del empleado: "))

# Verificar si el salario es menor que $2000
if salario < 2000:
    # Calcular el aumento del 15%
    aumento = salario * 0.15
    nuevo_salario = salario + aumento
    # Mostrar el nuevo salario
    print("Tu sueldo anterior era:", salario)
    print("Su nuevo sueldo es:", nuevo_salario)
else:
    # Mostrar el salario original si no se cumple la condición
    print("El salario del trabajador es:", salario)