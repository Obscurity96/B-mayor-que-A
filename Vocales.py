#Actividad de vocales

def contar_vocales(texto):
    
    texto = texto.lower()
    
    vocales = 'aeiou'
    
    contador_vocales = 0
    
    
    for caracter in texto:
        #Si es una vocal incrementar el contador
        if caracter in vocales:
            contador_vocales += 1
    
    return contador_vocales

# Inicio del proceso
print("Bienvenido al contador de vocales.")
print("-----------------------------------")

# Solicitar al usuario que ingrese un texto
texto_usuario = input("Por favor, ingrese un texto: ")


# Contar el número de vocales en el texto ingresado
numero_vocales = contar_vocales(texto_usuario)

# Mostrar el resultado
print(f"El número de vocales en el texto es: {numero_vocales}")

