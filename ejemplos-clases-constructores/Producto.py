class Producto: 
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(nombre, precio):
        print(f"Producto: {nombre}")
        print(f"Precio: ${precio:.2f}")

# Ejemplo de uso
Producto.mostrar_informacion("Pantalon", 20)  # Llamada del método 

producto_nombre = "Zapatos"
producto_precio = 105
Producto.mostrar_informacion(producto_nombre, producto_precio)