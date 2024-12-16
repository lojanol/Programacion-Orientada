# Definimos los datos mediante la creacion de una
#variable

ciudades  = [ "CUENCA", "AMBATO","QUITO","MANTA"]
# Creamos otra variable donde almacenaremos las temperaturas
temp_ciudades = [[25,30,40,38,25,39,28], #CUENCA
                 [25,26,28,29,35,25,23], #AMBATO
                 [36,36,38,39,38,40,42], #QUITO
                 [28,25,29,29,28,28,30]] #MANTA

#CREAMOS UNA VARIABLE DONDE SE ALMACENE EL PROMEDIO  POR SEMANA Y SE DIVIDA PARA 7
# POR CADA SEMANA

promedios = {
    ciudad: sum(temp_ciudades[i][:7])/7 for i, ciudad in enumerate (ciudades ) }

#IMPRIMIMOS EL RESULTADO EN PANTALLA

print(promedios)