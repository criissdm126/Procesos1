class Cuenta:
    
    def __init__(self, nombre, fecha):
        self.nombre_cliente = nombre
        self.numero_cuenta = str(hash(nombre))[-10:]
        self.saldo = 0.0
        self.movimientos = []
        self.registrar_movimiento(fecha, "apertura", 0.0)

    def ingreso(self, cantidad, fecha):
        if cantidad > 0:
            self.saldo += cantidad
            self.registrar_movimiento(fecha, "ingreso", cantidad)

    def reintegro(self, cantidad, fecha):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            self.registrar_movimiento(fecha, "reintegro", cantidad)

    def verSaldo(self):
        return self.saldo

    def verCliente(self):
        return self.nombre_cliente

    def registrar_movimiento(self, fecha, tipo_movimiento, cantidad):
        movimiento = {
            "fecha": fecha,
            "tipo de movimiento": tipo_movimiento,
            "cantidad": cantidad
        }
        self.movimientos.append(movimiento)
