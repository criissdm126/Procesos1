#Crear la matriz identidad de n x n y presentarla en pantalla. El valor de n se pedirá por pantalla al inicio del programa.

# Solicitar el valor de n al usuario
n = int(input("Ingrese el valor de n para la matriz identidad: "))

# Crear la matriz identidad
matriz_identidad = [[1 if j == i else 0 for j in range(n)] for i in range(n)]

# Presentar la matriz en pantalla
print("Matriz Identidad de", n, "x", n, ":")
for fila in matriz_identidad:
    print(fila)
