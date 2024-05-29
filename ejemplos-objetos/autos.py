class autos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def saludar(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}")

ejemplo1 = autos("Lexxs","CT 200") # Objeto de la Clase autos
ejemplo1.saludar()   

