import os
import funciones.corefile as cf
import funciones.generos as g
import funciones.actores as a
import funciones.formatos as f
import funciones.movie as m
import funciones.informe as i

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
    head = """
+++++++++++++++++++++++++++
+    GESTOR DE GENEROS    +
+++++++++++++++++++++++++++
"""
    isTrue = True
    while isTrue:
        os.system("cls")
        print(head)
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

def menuA():
    head = """
+++++++++++++++++++++++++++
+    GESTOR DE ACTORES    +
+++++++++++++++++++++++++++
"""
    isTrue = True
    while isTrue:
        os.system("cls")
        print(head)
        for i,item in enumerate(menuActor):
            print(f"{i+1} - {item}")
        try:
            opSA = cf.validar(":) ",int)
        except ValueError:
            print("Error en el dato de ingreso...")
            os.system("pause")
        else:
            if opSA==1:
                a.crearActor()
            elif opSA==2:
                a.listarActor()
            elif opSA==3:
                isTrue = False
            else:
                print("Opcion seleccionada inexistente... Intente nuevamenete")
                os.system("pause")

def menuF():
    head = """
++++++++++++++++++++++++++++
+    GESTOR DE FORMATOS    +
++++++++++++++++++++++++++++
"""
    isTrue = True
    while isTrue:
        os.system("cls")
        print(head)
        for i,item in enumerate(menuFormat):
            print(f"{i+1} - {item}")
        try:
            opSF = cf.validar(":) ",int)
        except ValueError:
            print("Error en el dato de ingreso...")
            os.system("pause")
        else:
            if opSF==1:
                f.crearFormato()
            elif opSF==2:
                f.listarFormato()
            elif opSF==3:
                isTrue = False
            else:
                print("Opcion seleccionada inexistente... Intente nuevamenete")
                os.system("pause")

def menuM():
    head = """
+++++++++++++++++++++++++++++
+    GESTOR DE PELICULAS    +
+++++++++++++++++++++++++++++
"""
    isTrue = True
    while isTrue:
        os.system("cls")
        print(head)
        for i,item in enumerate(menuMovie):
            print(f"{i+1} - {item}")
        try:
            opSF = cf.validar(":) ",int)
        except ValueError:
            print("Error en el dato de ingreso...")
            os.system("pause")
        else:
            if opSF==1:
                m.crearMovie()
            elif opSF==2:
                pass
            elif opSF==3:
                m.delMovie()
            elif opSF==4:
                pass
            elif opSF==5:
                pass
            elif opSF==6:
                pass
            elif opSF==7:
                isTrue = False
            else:
                print("Opcion seleccionada inexistente... Intente nuevamenete")
                os.system("pause")

def menuI():
    head = """
++++++++++++++++++++++++++++
+    GESTOR DE INFORMES    +
++++++++++++++++++++++++++++
"""
    isTrue = True
    while isTrue:
        os.system("cls")
        print(head)
        for i,item in enumerate(menuInforme):
            print(f"{i+1} - {item}")
        try:
            opSF = cf.validar(":) ",int)
        except ValueError:
            print("Error en el dato de ingreso...")
            os.system("pause")
        else:
            if opSF==1:
                pass
            elif opSF==2:
                pass
            elif opSF==3:
                pass
            elif opSF==4:
                isTrue = False
            else:
                print("Opcion seleccionada inexistente... Intente nuevamenete")
                os.system("pause")