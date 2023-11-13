from banco import Cuenta

def transferencia(cuenta_origen, cuenta_destino, monto, fecha):
    # Realizar una transferencia de dinero entre cuentas
    if cuenta_origen.verSaldo() >= monto:
        cuenta_origen.reintegro(monto, fecha)
        cuenta_destino.ingreso(monto, fecha)
        return True
    else:
        return False

if __name__ == "__main__":
    # Crear dos clientes con nombres y apellidos ficticios
    cliente1 = Cuenta("Juan Pérez", "2023-10-03")
    cliente2 = Cuenta("María López", "2023-10-03")

    # Ingresar 10,000 € a cada cuenta
    cliente1.ingreso(10000.0, "2023-10-04")
    cliente2.ingreso(10000.0, "2023-10-04")

    # Imprimir los nombres y saldos iniciales
    print(f"Cliente 1: {cliente1.verCliente()}, Saldo: {cliente1.verSaldo()} €")
    print(f"Cliente 2: {cliente2.verCliente()}, Saldo: {cliente2.verSaldo()} €")

    # Transferir 4,500 € de cliente1 a cliente2
    if transferencia(cliente1, cliente2, 4500.0, "2023-10-05"):
        print("Transferencia exitosa")
    else:
        print("Fondos insuficientes para la transferencia")

    # Imprimir los nombres y saldos después de la transferencia
    print(f"Cliente 1: {cliente1.verCliente()}, Saldo: {cliente1.verSaldo()} €")
    print(f"Cliente 2: {cliente2.verCliente()}, Saldo: {cliente2.verSaldo()} €")
