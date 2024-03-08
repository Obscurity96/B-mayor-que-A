# Actividad Calificaciones
calificaciones = []
for i in range(5):
    calificacion = float(input("Ingrese la calificación {}: ".format(i+1)))
    while calificacion < 0 or calificacion > 10:
        calificacion = float(input("La calificación debe estar entre 0 y 10. Ingrese la calificación {}: ".format(i+1)))
    calificaciones.append(calificacion)

# Calcular el promedio

promedio = sum(calificaciones) / len(calificaciones)

# Si el alumno aprobó o reprobó
if promedio >= 7:
    print("El alumno aprobó con un promedio de", promedio)
else:
    print("El alumno reprobó con un promedio de", promedio)