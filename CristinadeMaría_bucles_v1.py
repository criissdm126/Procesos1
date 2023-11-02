# Inicializamos contadores y variables para la suma y el producto
contador_pares = 0
contador_impares = 0
suma_pares = 0
producto_impares = 1

# Pedimos 6 números enteros
print("Se le pedirán 6 números, se le mostrará por pantalla cuantos nº impares y pares hay, y sumará los pares y hallar el producto de los impares.")
for i in range(6):
    numero = int(input("Ingrese un número entero: "))
    
    # Verificamos si el número es par o impar
    if numero % 2 == 0:
        contador_pares += 1
        suma_pares += numero
    else:
        contador_impares += 1
        producto_impares *= numero

# Mostramos los resultados por pantalla
print("Número de elementos pares:", contador_pares)
print("Suma pares: ", suma_pares)
print("Número de elementos impares:", contador_impares)
print("Producto:", producto_impares)


