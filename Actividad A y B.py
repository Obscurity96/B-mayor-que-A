#Actividad A y B 
# Pedir que ingrese los números A y B

A = float(input("Ingrese el número A: "))
B = float(input("Ingrese el número B: "))

# Comparar los números A y B

if A > B:
    print("A es mayor que B.")
elif B > A:
    print("B es mayor que A.")
else:
    print("A y B son iguales.")