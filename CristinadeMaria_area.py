# Hacer un programa que calcula el área de la figura descomponiéndola en hilos para optimizar.
import threading

def area_figura(hilo1, hilo2, hilo3, num_hilos):
    area_hilo = (hilo1 + hilo2 + hilo3) * 0.01
    area_total = area_hilo * num_hilos
    return area_total

# Parámetros de la figura
hilo1 = 26
hilo2 = 8
hilo3 = 6
num_hilos = 100000 # Valor más pequeño para probar

# Calcular el área total de la figura
area_total = area_figura(hilo1, hilo2, hilo3, num_hilos)

# Imprimir el resultado
print("El área total de la figura es:", area_total)