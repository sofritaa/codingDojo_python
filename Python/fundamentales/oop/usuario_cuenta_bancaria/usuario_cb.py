class CuentaBancaria:
    cuentas = []

    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, monto):
        self.balance += monto
        return self

    def retiro(self, monto):
        if (self.balance - monto) >= 0:
            self.balance -= monto
        else:
            print("Fondos insuficientes: Se cobrará una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_balance(self):
        return f"Balance de la cuenta: {self.balance}"

    def calcular_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self

    @classmethod
    def mostrar_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            print(cuenta.mostrar_balance())


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = {
            "corriente": CuentaBancaria(0.02, 1000),
            "ahorros": CuentaBancaria(0.05, 3000)
        }

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance de cuenta corriente: {self.cuentas['corriente'].mostrar_balance()}")
        print(f"Usuario: {self.nombre}, Balance de cuenta de ahorros: {self.cuentas['ahorros'].mostrar_balance()}")
        return self

    def transferir_dinero(self, monto, usuario_destino, cuenta_origen, cuenta_destino):
        cuenta_origen = self.cuentas[cuenta_origen]
        cuenta_destino = usuario_destino.cuentas[cuenta_destino]
        
        cuenta_origen.retiro(monto)
        cuenta_destino.deposito(monto)

        self.mostrar_balance_usuario()
        usuario_destino.mostrar_balance_usuario()
        return self


elvis = Usuario("Elvis teck")

elvis.cuentas['corriente'].deposito(100)
elvis.mostrar_balance_usuario()
