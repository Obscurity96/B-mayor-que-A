# Actividad Comun multiplo

def calcular_mcm(num1, num2):
    # Encuentra el máximo de los dos números
    maximo = max(num1, num2)

    # Inicializa el MCM
    mcm = maximo

    # Repite hasta encontrar el MCM
    while True:
        if mcm % num1 == 0 and mcm % num2 == 0:
            return mcm
        mcm += maximo

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
mcm = calcular_mcm(numero1, numero2)
print(f"El mínimo común múltiplo (MCM) de {numero1} y {numero2} es: {mcm}")