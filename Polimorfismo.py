# creamos una clase
class Tomate:
    def tipo(self): #creamos el metodo
        print("carnes") #print para visualizar

# creamos otro metodo
    def color(self):
        print("azul")

#creamos una segunda clase
#tomamos en cuenta algo que tengan en comun
#pero a la vez distintos

class Mango:
    def tipo(self):
        print("fruta")

    def color(self):
        print("morado")
#creamos una funcion externa
#Esta funcion trabaja de manera directa con los diferentes metodos que tiene cada clase
def funcion(objeto):
#creamos los propios elementos
    objeto.tipo()
#creamos los atributos a cada accion
    objeto.color()

#creamos un objeto

nuevo_tomate = Tomate()
funcion(nuevo_tomate)

nueva_Mango= Mango()
funcion(nueva_Mango)