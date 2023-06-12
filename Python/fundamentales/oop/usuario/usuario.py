class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0

    def hacer_deposito(self, cantidad):
        self.balance += cantidad

    def hacer_retiro(self, cantidad):
        self.balance -= cantidad

    def mostrar_balance(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance}")

    def transferir_dinero(self, otro_usuario, cantidad):
        self.balance -= cantidad
        otro_usuario.balance += cantidad
        self.mostrar_balance()
        otro_usuario.mostrar_balance()

# Crear instancias de la clase Usuario
usuario1 = Usuario("juan van iii")
usuario2 = Usuario("nibaldo linus")
usuario3 = Usuario("elvis tecs")

# Acciones de usuario1
usuario1.hacer_deposito(100)
usuario1.hacer_deposito(200)
usuario1.hacer_deposito(50)
usuario1.hacer_retiro(45)
usuario1.mostrar_balance()

# Acciones de usuario2
usuario2.hacer_deposito(1000)
usuario2.hacer_deposito(1000)
usuario2.hacer_retiro(500)
usuario2.hacer_retiro(300)
usuario2.mostrar_balance()

# Acciones de usuario3
usuario3.hacer_deposito(1500)
usuario3.hacer_retiro(1000)
usuario3.hacer_retiro(5000)
usuario3.hacer_retiro(3000)
usuario3.mostrar_balance()

# Transferencia de dinero de usuario1 a usuario3
usuario1.transferir_dinero(usuario3, 500)