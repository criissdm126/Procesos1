import threading

def calcular_area_triangulo(base, altura, resultado):
    # Función para calcular el área de un triángulo y agregarla a la lista de resultados
    area = 0.5 * base * altura
    resultado.append(area)

def calcular_area_rectangulo(base, altura, resultado):
    # Función para calcular el área de un rectángulo y agregarla a la lista de resultados
    area = base * altura
    resultado.append(area)

def main():
    resultado = []  # Lista para almacenar los resultados de las áreas calculadas

    # Triángulo grande
    hilo1 = threading.Thread(target=calcular_area_triangulo, args=(10, 12, resultado))
    
    # Rectángulo grande
    hilo2 = threading.Thread(target=calcular_area_rectangulo, args=(8, 12, resultado))
    
    # Rectángulo pequeño
    hilo3 = threading.Thread(target=calcular_area_rectangulo, args=(6, 5, resultado))
    
    # Triángulo pequeño
    hilo4 = threading.Thread(target=calcular_area_triangulo, args=(2, 5, resultado))
    
    # Iniciar los hilos
    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()

    # Esperar a que todos los hilos terminen
    hilo1.join()
    hilo2.join()
    hilo3.join()
    hilo4.join()

    # Calcular el área de la figura principal sumando todas las áreas calculadas
    area_figura_principal = sum(resultado)

    print(f"El área de la figura principal es: {area_figura_principal}")

if __name__ == "__main__":
    main()