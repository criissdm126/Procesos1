# Hacer un programa que calcula el área de la figura descomponiéndola en hilos para optimizar.

# Variables de control
i = 0
area_hilo1 = 0
area_hilo2 = 0
area_hilo3 = 0

# Bucle para generar las alturas de los hilos
while i <= 1000000000:
    area_hilo1 += i * 0.08
    area_hilo2 += i * 0.12
    area_hilo3 += i * 0.06
    i += 1

# Calcular el área total de la figura
area_total = area_hilo1 + area_hilo2 + area_hilo3

# Imprimir el resultado
print("El área total de la figura es: ", area_total)