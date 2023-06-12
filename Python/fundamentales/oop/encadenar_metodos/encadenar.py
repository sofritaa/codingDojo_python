class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0

    def hacer_deposito(self, cantidad):    
        self.balance += cantidad
        return self 
    
    def hacer_retiro(self, cantidad):
        self.balance -= cantidad
        return self

    def mostrar_balance(self):
        print(f"Usuario: {self.nombre}, Balance: {self.balance}")
        return self

    def transferir_dinero(self, cantidad, usuario):
        self.balance -= cantidad
        usuario.balance += cantidad
        self.mostrar_balance()
        usuario.mostrar_balance()
        return self


adrien = Usuario("Adriesn")
nibbles = Usuario("Mr. Nibbles")
benny_bob = Usuario("Benny Bob")

adrien.hacer_deposito(100).hacer_deposito(200).hacer_deposito(50).hacer_retiro(45).mostrar_balance()

nibbles.hacer_deposito(1000).hacer_deposito(1000).hacer_retiro(500).hacer_retiro(300).mostrar_balance()

benny_bob.hacer_deposito(1500).hacer_retiro(1000).hacer_retiro(5000).hacer_retiro(3000).mostrar_balance()

nibbles.transferir_dinero(400, adrien)