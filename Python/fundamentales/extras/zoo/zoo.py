class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100
    
    def mostrar_info(self):
        print("Nombre:", self.name)
        print("Salud:", self.health)
        print("Felicidad:", self.happiness)
    
    def alimentar(self):
        self.health += 10
        self.happiness += 10


class Leon(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.mane_length = 30


class Tigre(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.stripes_count = 50


class Oso(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.hibernating = False


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def agregar_animal(self, animal):
        self.animals.append(animal)
    
    def imprimir_toda_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.mostrar_info()


zoo1 = Zoo("El zoo")
zoo1.agregar_animal(Leon("Nal", 5))
zoo1.agregar_animal(Leon("wolo", 3))
zoo1.agregar_animal(Tigre("lemiwinks", 4))
zoo1.agregar_animal(Tigre("juan", 6))
zoo1.agregar_animal(Oso("shunshun", 8))
zoo1.imprimir_toda_info()
