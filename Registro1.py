registros = []

def solicitar_registro():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    nacionalidad = input("Ingrese la nacionalidad: ")
    return {'nombre': nombre, 'edad': edad, 'nacionalidad': nacionalidad}

# 10 registros
for _ in range(10):
    registro = solicitar_registro()
    registros.append(registro)

print("Registros almacenados:")
for i, registro in enumerate(registros, 1):
    print(f"Registro {i}: {registro}")
# Función para buscar un nombre en los registros
def buscar_nombre(nombre):
    for registro in registros:
        if registro['nombre'] == nombre:
            return registro
    return None

# Buscar nombre
nombre_buscar = input("Ingrese el nombre a buscar: ")

# Buscar el nombre en los registros
registro_encontrado = buscar_nombre(nombre_buscar)

# Mostrar los datos encontrados en el formato pedido
if registro_encontrado:
    print(f"{registro_encontrado['nombre']} tiene {registro_encontrado['edad']} años y es {registro_encontrado['nacionalidad']}.")
else:
    print("El nombre no fue encontrado en los registros.")
