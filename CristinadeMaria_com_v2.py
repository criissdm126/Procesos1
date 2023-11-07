import threading

# Los hilos que escriben y leen se organizan entre ellos para que el acceso a la variable compartida sea ordenado. Usar 2 tipos distintos de primitivas (Lock y Semaphores, ...)

texto_compartido = ""
lock = threading.Lock()
semaphore = threading.Semaphore(0)

def escritor():
    global texto_compartido
    while True:
        texto = input("Introduce un texto (-1 para salir): ")
        if texto == "-1":
            break
        with lock:
            texto_compartido = texto
            semaphore.release()

def lector():
    global texto_compartido
    while True:
        semaphore.acquire()
        with lock:
            if texto_compartido == "-1":
                break
            print("Texto leído:", texto_compartido)
            texto_compartido = ""

if __name__ == "__main__":
    escritor_thread = threading.Thread(target=escritor)
    lector_thread = threading.Thread(target=lector)

    escritor_thread.start()
    lector_thread.start()

    escritor_thread.join()
    lector_thread.join()
