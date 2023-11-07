import threading

# Los hilos que escriben y leen se organizan entre ellos para que el acceso a la variable compartida sea ordenado. Usar 2 tipos distintos de primitivas (Lock y Semaphores, ...)

texto_compartido = ""
semaphore_escritor = threading.Semaphore(1)
semaphore_lector = threading.Semaphore(0)

def escritor():
    global texto_compartido
    while True:
        texto = input("Introduce un texto (-1 para salir): ")
        if texto == "-1":
            break
        semaphore_escritor.acquire()
        texto_compartido = texto
        semaphore_lector.release()

def lector():
    global texto_compartido
    while True:
        semaphore_lector.acquire()
        if texto_compartido == "-1":
            break
        print("Texto leído:", texto_compartido)
        semaphore_escritor.release()

if __name__ == "__main__":
    escritor_thread = threading.Thread(target=escritor)
    lector_thread = threading.Thread(target=lector)

    escritor_thread.start()
    lector_thread.start()

    escritor_thread.join()
    lector_thread.join()
