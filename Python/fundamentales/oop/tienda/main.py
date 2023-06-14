# main.py

from store import Tienda
from product import Producto

# Crea instancias de la clase Producto
producto1 = Producto("Camisa", 20, "Ropa")
producto2 = Producto("Libro", 10, "Libros")
producto3 = Producto("Zapatos", 50, "Calzado")

# Crea una instancia de la clase Tienda
tienda = Tienda("Mi Tienda")

# Agrega productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Vende un producto de la tienda
tienda.vender_producto(1)

# Realiza una inflación en todos los productos de la tienda
tienda.inflacion(10)

# Reduce el precio de los productos en la categoría "Ropa" en un 20%
tienda.hacer_liquidacion("Ropa", 20)
