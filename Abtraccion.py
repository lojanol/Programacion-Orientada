# El siguiente ejemplo muestra un sistema que controlará electrodomésticos

# Definimos una clase abstracta

from abc import  ABC,abstractmethod
# Creamos la clase base
class Electrodomestico(ABC):

# Definimos el metodo bastracto 1
    def enceder(self):
        pass

# Definimos el metodo abstracto 2
    def apagar (self):
        pass

# Creacion de clases concretas
class Nevera (Electrodomestico):
    def enceder(self):
        print('Nevera está prendida')

class cocina(Electrodomestico):
    def apagar(self):
        print("cocina està apagado")

#cada una de estas clases define especificamente un comportamiento

# Usos de las clases
def controlar_electrodomestico(electrodomestico,accion):
    if accion == "prendida":
        electrodomestico.prendida()

    elif accion == "apagar":
        electrodomestico.apagar()

#Creamos los objetos electrodomesticos

nevera = Nevera()
cocina = cocina()

controlar_electrodomestico(cocina,"apagar")
controlar_electrodomestico(Nevera,"encender")