local_val = "tarea"

def square(x):
    return x * x

class Usuario:
    def __init__(self, name):
        self.name = name

    def di_hola(self):
        return "hola"

print(square(5))
usuario = Usuario("Anna")
print(usuario.name)
print(usuario.di_hola())

print(__name__)
