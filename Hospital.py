def calcular_costo_total(servicio, dias, edad):
    costos = {"parto": 25, "urgencias": 17, "Hospitalizacion general": 12, "Cirujia": 21}
    
    costo_base = costos.get(servicio, 0) * dias
    
    if edad >= 20 and edad <= 25 and servicio != "parto":
        costo_base *= 1.04
    
    if edad > 65:
        costo_base *= 0.95
    
    return costo_base

def main():
    servicio = input("Ingrese el tipo de servicio (parto, urgencias, Hospitalizacion general, Cirujia): ").lower()
    dias = int(input("Ingrese la cantidad de días de hospitalización: "))
    edad = int(input("Ingrese la edad del paciente: "))
    
    costo_total = calcular_costo_total(servicio, dias, edad)
    
    print(f"El costo total a pagar es: {costo_total}")

if __name__ == "__main__":
    main()
