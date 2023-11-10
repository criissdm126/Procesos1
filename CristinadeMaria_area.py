# Enunciado: Hacer un programa que calcula el área de la figura descomponiéndola en hilos para optimizar.
import threading

# Triángulo grande
base_triangulo_grande = 10
altura_triangulo_grande = 12
area_triangulo_grande = 0.5 * base_triangulo_grande * altura_triangulo_grande


# Rectángulo grande
base_rectangulo_grande = 8
altura_rectangulo_grande = 12
area_rectangulo_grande = base_rectangulo_grande * altura_rectangulo_grande


# Rectángulo pequeño
base_rectangulo_pequeño = 6
altura_rectangulo_pequeño = 5
area_rectangulo_pequeño = base_rectangulo_pequeño * altura_rectangulo_pequeño

# Triángulo pequeño
base_triangulo_pequeño = 2
altura_triangulo_pequeño = 5
area_triangulo_pequeño = 0.5 * base_triangulo_pequeño * altura_triangulo_pequeño

# Base de la figura principal
base_figura_principal = 26

# Área de la figura principal, suma de las áreas de las figuras anteriores
area_figura_principal = area_triangulo_grande + area_rectangulo_grande + area_rectangulo_pequeño + area_triangulo_pequeño

print(f"El área de la figura principal es: {area_figura_principal}")