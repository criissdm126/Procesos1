import random
import time
import sys

def main():
    while True: # bucle principal
        a = random.randint(0,20); # generar un número aleatorio entre 0 y 20
        time.sleep(1) # esperar antes de generar el siguiente número
        sys.stdout.write(str(a)) # mostrar el número generado en la consola
        sys.stdout.write('\n') # agregar un salto de línea después del número
        sys.stdout.flush() # forzar la impresión del número en la consola
        if a == 7: # verificar si el número generado es igual a 7
            break # si es 7, sale del bucle principal y el programa termina

if __name__ == "__main__":
    main()