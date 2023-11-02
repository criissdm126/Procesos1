import random

# Crear una lista con 20 números aleatorios entre 1 y 100
lista_numeros = [random.randint(1, 100) for _ in range(20)]

# Hallar el máximo de números
maximo = max(lista_numeros)

# Calcular la media de los números
media = sum(lista_numeros) / len(lista_numeros)

# Insertar la palabra "hola" en la posición 5
lista_numeros.insert(5, "hola")

# Imprimir la lista en pantalla
print("Lista con 'hola' en la posición 5:", lista_numeros)

# Hacer una sublista de las posiciones 6 a 12
sublista1 = lista_numeros[6:13]

# Hacer una sublista con los 4 últimos elementos
sublista2 = lista_numeros[-4:]

# Imprimir los resultados
print("Máximo:", maximo)
print("Media:", media)
print("Sublista de las posiciones 6 a 12:", sublista1)
print("Sublista con los 4 últimos elementos:", sublista2)
