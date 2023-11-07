import threading

# El hilo principal "Mainthread" controlará que la escritura-lectura se realice ordenadamente.

texto_compartido = ""
lock = threading.Lock()

def escritor():
    global texto_compartido
    while True:
        texto = input("Introduce un texto (-1 para salir): ")
        if texto == "-1":
            break
        texto_compartido = texto

def lector():
    global texto_compartido
    while True:
        if texto_compartido != "":
            with lock:
                print("Texto leído:", texto_compartido)
                texto_compartido = ""
            if texto_compartido == "-1":
                break

if __name__ == "__main__":
    escritor_thread = threading.Thread(target=escritor)
    lector_thread = threading.Thread(target=lector)

    escritor_thread.start()
    lector_thread.start()

    escritor_thread.join()
    lector_thread.join()
