def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")

def seleccionar_opcion():
    opcion = input("Seleccione una opción: ")
    if opcion not in ['1', '2', '3']:
        raise ReferenceError("Opción no válida")

def main():
    mostrar_menu()
    try:
        seleccionar_opcion()
        print("Opción válida seleccionada.")
    except ReferenceError as re:
        print(re)

if __name__ == "__main__":
    main()
