'''La encapsulación permite ocultar los detalles internos del objeto
utilizando modificadores de acceso'''

class Carro:
    def __init__(self , nombre, diseño):
        self.__nombre=nombre # cualidad encapsulado (exclusivo)
        self.__diseño=diseño # cualidad encapsulado (exclusivo)
        self.__distancia =2 # cualidad encapsulado (exclusivo)
    def get_nombre(self):
        return self.__nombre

    def get_diseño(self):
        return self.__diseño

    def get_distancia(self):
        return self.__distancia

    def manejar (self,kilometro):
        self.__distancia+=kilometro
        print(f" el carro ha recorrido {kilometro} km .distancia total:´{self.__distancia} km")

# creacion de un objeto carro
mi_carro = Carro("mazda","cedan")

# acceder a la cualidad de manera segura
print(mi_carro.get_nombre()) # imprimir: mazda
print(mi_carro.get_diseño()) # imprimir: cedan

# modificar el estado del objeto atravez de un metodo
mi_carro.manejar(200)

