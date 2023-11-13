import psutil

# Nombre del proceso que estamos buscando
nombre_proceso = "notepad.exe"

# Itera a través de todos los procesos en ejecución
for proceso in psutil.process_iter(['pid', 'name']):
    try:
        proceso_info = proceso.info
        # Verifica si el nombre del proceso coincide
        if proceso_info['name'] == nombre_proceso:
            # Termina el proceso
            psutil.Process(proceso_info['pid']).terminate()
            print(f"Proceso {nombre_proceso} terminado.")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Si no se encontró ningún proceso
if not any(p.info['name'] == nombre_proceso for p in psutil.process_iter(['name'])):
    print(f"No se encontró ningún proceso {nombre_proceso}.")
