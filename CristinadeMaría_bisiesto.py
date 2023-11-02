#Realizar un programa que acepte 2 números enteros que representan años, identifique los años bisiestos en el intervalo y los añada a una lista. Posteriormente, imprime toda la lista en pantalla.
#El programa volverá a pedir años y repetirá el proceso. Solo terminará cuando se introduzca la palabra "end" o "fin" en lugar de un número.
#Nota: Un año bisiesto es el que es múltiplo de 4 pero no múltiplo de 100.

# Función para verificar si un año es bisiesto
def bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Lista para almacenar los años bisiestos
listabisiestos = []

# Mensaje inicial 
print("Este programa encuentra y muestra los años bisiestos en una lista.")

# Bucle principal
while True:
    
    # Solicitar el año de inicio o la palabra "end" o "fin" para terminar
    entrada_inicio = input("Introduzca el año de inicio o escriba 'end' o 'fin': ")
    
    # Comprobar si quiere terminar el programa
    if entrada_inicio.lower() == "end" or entrada_inicio.lower() == "fin":
        break
    
    # En caso de no ser ni 'end' ni 'fin', preguntar por el segundo año
    entrada_fin = input("Introduzca el año de fin: ")
    
    try:
        # Convertir las entradas a números enteros
        año_inicio = int(entrada_inicio)
        año_fin = int(entrada_fin)
        
        # Verificar que el año de inicio sea menor que el año de fin
        if año_inicio > año_fin:
            print("El año de inicio debe ser menor que el año de fin.")
            continue
        
        # Leer los años e imprimir los bisisestos en el intervalo
        for año in range(año_inicio, año_fin + 1):
            if bisiesto(año):
                listabisiestos.append(año)
    except ValueError:
        # Si añade algo que no debe
        print("No es correcto, vuelva a introducir los números o añada la palabra 'end' o 'fin'")
    
    # Mostrar los años bisiestos 
    print("Años bisiestos en el intervalo:")
    if not listabisiestos:
        print("No se encontraron años bisiestos en el intervalo especificado.")
    else:
        for año in listabisiestos:
            print(año)
    
    # Resetea la lista para añadir los nuevos años bisiesto del nuevo intervalo
    listabisiestos = []

