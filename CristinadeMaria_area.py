# Enunciado: Hacer un programa que calcula el área de la figura descomponiéndola en hilos para optimizar.
import threading

# Definir los valores de a, b y h
a = 10  # en cm
b = 8   # en cm
h = 12  # en cm

# Función para calcular el área
def calcular_area(a, b, h):
    area = (a + b) * h / 2
    return area

# Calcular el área
area = calcular_area(a, b, h)

# Imprimir el resultado
print("El área de la figura es", area, "cm²")
