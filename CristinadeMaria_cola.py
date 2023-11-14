import threading
import queue

# Crear una cola compartida entre hilos
cola = queue.Queue()

# Función para el hilo escritor
def escritor():
    while True:
        texto = input("Ingrese un texto (o escriba -1 para finalizar): ")
        if texto == "-1":
            # Colocar el código de finalización en la cola
            cola.put("0x01")
            break
        else:
            # Poner el texto en la cola
            cola.put(texto)

# Función para el hilo lector
def lector():
    while True:
        # Obtener un elemento de la cola
        elemento = cola.get()
        if elemento == "0x01":
            # Si es el código de finalización, terminar el hilo
            print("Hilo finalizando.")
            break
        else:
            # Mostrar el elemento en pantalla
            print("Hilo recibido: ", elemento)

# Crear e iniciar los hilos
hilo_escritor = threading.Thread(target=escritor)
hilo_lector = threading.Thread(target=lector)

hilo_escritor.start()
hilo_lector.start()

# Esperar a que ambos hilos terminen
hilo_escritor.join()
hilo_lector.join()
