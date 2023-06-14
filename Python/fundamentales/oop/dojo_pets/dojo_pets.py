class Mascota:
    def __init__(self, nombre, tipo, trucos, sonido):
        self.nombre = nombre
        self.tipo = tipo
        self.trucos = trucos
        self.salud = 100
        self.energia = 50
        self.sonido = sonido

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    def jugar(self):
        self.salud += 5
        self.energia -= 15
        return self

    def hacer_sonido(self):
        print(self.sonido)


class Ninja:
    def __init__(self, nombre, apellido, golosinas, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.golosinas = golosinas
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self):
        if len(self.comida_mascota) > 0:
            comida = self.comida_mascota.pop()
            print(f"¡Alimentando a {self.mascota.nombre} con {comida}!")
            self.mascota.comer()
        else:
            print("¡Oh no! ¡Necesitas más comida para tu mascota!")
        return self

    def bañar(self):
        self.mascota.hacer_sonido()


mis_golosinas = ['Salchicha', 'Tocino', 'Bolsa de basura']
mi_comida_mascota = ['Pizza', 'Hamburguesa']

pancho = Mascota("Sr. pancho", "Caballo", ['mordisquea cosas', 'es invisible'], "¡Hey, hey!")

juan = Ninja("juan", "Dion", mis_golosinas, mi_comida_mascota, pancho)

juan.alimentar()
juan.alimentar()
juan.alimentar()
