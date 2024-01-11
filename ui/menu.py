import os
import funciones.corefile as cf
import funciones.generos as g

menuPpal = ["Administrador de generos","Administrador de actores","Administrar de formatos","Gestor de informes","Gestor de peliculas","Salir"]
menuGenre = ["Crear Genero","Listar generos","Ir a menu principal"]
menuActor = ["Crear actor","Listar Actor","Ir a menu principal"]
menuFormat = ["Crear formato","Listar formato","Ir a menu principal"]
menuMovie = ["Agregar Pelicula","Editar pelicula","Eliminar pelicula","Eliminar actor","Buscar pelicula","Listar todas las peliculas","Ir a menu principal"]
menuInforme = ["Listar las peliculas de un genero especifico","Listar las peliculas donde el protagonista sea Silvester Stallone","Buscar pelicula y mostrar la sinopsis y los actores","Ir a menu principal"]

def menuP():
    for i,item in enumerate(menuPpal):
        print(f"{i+1} - {item}")
    return cf.validar(":) ",int)

def menuG():
    isTrue = True
    while isTrue:
        os.system("cls")
        for i,item in enumerate(menuGenre):
            print(f"{i+1} - {item}")
        try:
            opSG = cf.validar(":) ",int)
        except ValueError:
            print("Error en el dato de ingreso...")
            os.system("pause")
        else:
            if opSG==1:
                g.crearGenero()
            elif opSG==2:
                g.listarGenero()
            elif opSG==3:
                isTrue = False
            else:
                print("Opcion seleccionada inexistente... Intente nuevamenete")
                os.system("pause")