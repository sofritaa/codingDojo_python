# product.py

class Producto:
    contador_ids = 0

    def __init__(self, nombre, precio, categoria):
        self.id = Producto.contador_ids
        Producto.contador_ids += 1
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100
        else:
            self.precio -= self.precio * cambio_porcentaje / 100

    def imprimir_info(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}")
