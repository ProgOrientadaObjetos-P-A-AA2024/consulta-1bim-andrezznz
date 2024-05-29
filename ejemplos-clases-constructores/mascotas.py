class mascota:    
    def __init__(self, nombre="", especie="", edad=0):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")

# Ejemplo de uso
mascota1 = mascota("Toby", "Perro", 3)
mascota1.mostrar_informacion()

mascota2 = mascota(especie="Gato", edad=2)
mascota2.nombre = "Luna"
mascota2.mostrar_informacion()