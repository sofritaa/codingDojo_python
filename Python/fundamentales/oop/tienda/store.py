# store.py

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)

    def vender_producto(self, id_producto):
        for producto in self.productos:
            if producto.id == id_producto:
                self.productos.remove(producto)
                producto.imprimir_info()
                break
        else:
            print("Producto no encontrado.")

    def inflacion(self, aumento_porcentaje):
        for producto in self.productos:
            producto.actualizar_precio(aumento_porcentaje, True)

    def hacer_liquidacion(self, categoria, descuento_porcentaje):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(descuento_porcentaje, False)
