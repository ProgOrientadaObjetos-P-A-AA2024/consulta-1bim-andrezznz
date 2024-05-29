class ejemplo:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} anios")
        # pritn("Hola mi nombre es " %self.nombre " y tengo " %self.edad " anios")
        # pritn("Hola mi nombre es " + self.nombre + " y tengo " + self.edad + " anios")

ejemplo1 = ejemplo("Andres", 19) # Objeto de la Clase ejemplo
ejemplo1.saludar()            
