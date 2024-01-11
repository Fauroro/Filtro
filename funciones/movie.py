import os
import funciones.corefile as cf
import funciones.generos as g

DATA_M = 'data/movie.json'
def crearMovie():
    blockbuster = {}
    id=0
    cf.checkFile(DATA_M,blockbuster)
    dataTemp = cf.readFile(DATA_M)
    if len(dataTemp)==0:
        id += 1
    else:
        id = len(dataTemp) + 1
    idM = "P0"+str(id)
    nombre = cf.validar("Ingrese el nombre de la pelicula: ",str)
    duracion = cf.validar("Ingrese la duracion de la pelicula (minutos): ",str)
    sinopsis = cf.validar("Ingrese la sinospis de la pelicula: ",str)
    movie = {
        "id": idM,
        "nombre": nombre,
        "duracion":duracion,
        "sinopsis":sinopsis
    }
    peliculas={}
    dataGenre = cf.readFile(g.DATA_G)
    if len(dataGenre)==0:
        print("No se tienen generos registrados. Registre un genero para continuar ...")
        isActive = True
        while isActive:
            g.crearGenero()
            isActive = bool(input("Desea registrar otro genero? Cualquier tecla para continuar ... Enter para finalizar"))
    print("Generos existentes: ")
    dataGenre = cf.readFile(g.DATA_G)
    for i,item in dataGenre.items():
        print(f"{i} - {item.get('nombre')}")
    isActive = True
    while isActive:
        isTrue = True
        while isTrue:
            opG = cf.validar("Ingrese la opcion el genero seleccionado ",str)
            try:
                temp = dataGenre[opG]
            except KeyError:
                print("Opcion de genero inexistente.")
            else:
                movie.update({opG:temp})
                isTrue = False
        isActive = bool(input("Desea ingresar un genero adicional? Cualquier tecla para continuar ... Enter para finalizar"))
    peliculas.update({idM:movie})
    blockbuster.update({"peliculas":peliculas})
    cf.addData(DATA_M,"blockbuster",blockbuster)


def delMovie():
    dataMovie = cf.readFile(DATA_M)
    for i,item in dataMovie.items():
        print(f"{i} - {item.get('nombre')}")
    opDM = cf.validar("Ingrese el numero de la opcion el genero seleccionado",int)
    cf.delData(DATA_M,opDM,dataMovie)    
