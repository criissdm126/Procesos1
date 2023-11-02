# Realizar un programa que
# Pide un texto por consola.
# Si el texto es distinto de -1
# Arranca 1 proceso (escritor) que añade el texto a un fichero y termina.
# Cuando la escritura ha terminado lanza otro proceso (lector) que lee todo el fichero, lo saca en pantalla y termina.
# Vuelve a pedir el texto y repite el ciclo hasta que el texto introducido ==  “-1”

# El nombre del fichero lo pasará el padre a los hijos como parámetro.

import multiprocessing


# Pide un texto por consola.
def escritor(texto, fichero_salida):
    with open(fichero_salida, "a") as file:
        file.write(texto + "\n")

# Crear fichero
def lector(fichero_salida):
    with open(fichero_salida, "r") as file:
        texto = file.read()
    print(texto)

# Arranca 1 proceso (escritor) que añade el texto a un fichero y termina.
if __name__ == "__main__":
    texto = input("Escribe una frase: ")
    while texto != "-1":
        p1 = multiprocessing.Process(target=escritor, args=(texto, "fichero_salida.txt"))
        p1.start()
        p1.join()
        
        # vuelve a pedir el texto y repite el ciclo hasta que el texto introducido ==  “-1”
        p2 = multiprocessing.Process(target=lector, args=("fichero_salida.txt",))
        p2.start()
        p2.join()
        
        # Si el texto es distinto de -1
        texto = input("Escribe una frase: ")
