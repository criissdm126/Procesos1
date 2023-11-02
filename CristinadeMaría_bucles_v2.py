# Inicializamos contadores y variables para la suma y el producto
contador_pares = 0
contador_impares = 0
suma_pares = 0
producto_impares = 1

# Pedimos números enteros hasta que se ingrese -1
print("Cuando ponga el número negativo -1, el programa finalizará.")
while True:
    numero = int(input("Ingrese un número entero: "))
    
    if numero == -1:
        break
    
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

