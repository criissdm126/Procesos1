import os
import time
import multiprocessing

def lectura(fichero_salida):
    while True:
        try:
            with open(fichero_salida, 'r') as file:
                content = file.read()
                if content.strip().lower() == 'fin':
                    print("Proceso de lectura finalizado.")
                    break
                print("Contenido del archivo:", content)
        except FileNotFoundError:
            pass
        time.sleep(5)

def escritura(fichero_salida):
    while True:
        user_input = input("Escribe un texto o 'fin' para terminar: ")
        with open(file_path, 'w') as file:
            file.write(user_input + "\n")
        if user_input.strip().lower() == 'fin':
            print("Proceso de escritura finalizado.")
            break

if __name__ == '__main__':
    file_path = input("Introduce el nombre del archivo: ")

    # Iniciar el proceso lector
    reader_process = multiprocessing.Process(target=lectura, args=(file_path,))
    reader_process.start()

    # Iniciar el proceso escritor
    writer_process = multiprocessing.Process(target=escritura, args=(file_path,))
    writer_process.start()

    # Esperar a que los procesos terminen
    reader_process.join()
    writer_process.join()

    print("Todos los procesos han terminado.")
