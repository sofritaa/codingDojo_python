class CuentasBancarias:
    cuentas = []

    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentasBancarias.cuentas.append(self)

    def deposito(self, monto):
        self.balance += monto
        return self

    def retiro(self, monto):
        if (self.balance - monto) >= 0:
            self.balance -= monto
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_info(self):
        print(f"Balance: {self.balance}")
        return self

    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info()


# Crear cuentas bancarias
cuenta_ahorros = CuentasBancarias(0.05, 1000)
cuenta_corriente = CuentasBancarias(0.02, 5000)

# Realizar operaciones en la primera cuenta
cuenta_ahorros.deposito(10).deposito(20).deposito(40).retiro(600).mostrar_info()

# Realizar operaciones en la segunda cuenta
cuenta_corriente.deposito(100).deposito(200).deposito(400).retiro(60).mostrar_info()

# Imprimir información de todas las cuentas bancarias
CuentasBancarias.imprimir_cuentas()
