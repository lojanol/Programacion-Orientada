''' Tecnica de programacion'''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def dialogar(self):
        pass
# Implementaremos en la subclase el metodo abstracto
class Perro(Animal):
    def dialogar(self):
        print("Gua Gua!")

class Vaca(Animal):
    def dialogar(self):
        print("Muu Muu!")

class Pato(Animal):
    def dialogar(self):
        print("Cua Cua!")
# Creacion de nombres
Perro=Perro("Tayson")
Vaca=Vaca("Lola")
Pato=Pato("Cua")

# Llamamos al metodo dialogar() para cada nombre
Perro.dialogar()
Vaca.dialogar()
Pato.dialogar()
