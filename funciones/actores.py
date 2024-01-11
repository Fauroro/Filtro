import os
import funciones.corefile as cf

DATA_A = 'data/actor.json'
def crearActor():
    genero = {}
    cf.checkFile(DATA_A,genero)
    id = cf.validar("Ingrese el ID del actor: ",str)
    nombre = cf.validar("Ingrese el nombre del actor: ",str)
    genero = {
        "id": id,
        "nombre": nombre
    }
    cf.addData(DATA_A,id,genero)
def listarActor():
    genero = {}
    cf.checkFile(DATA_A,genero)
    dataTemp = cf.readFile(DATA_A)
    if len(dataTemp)==0:
        print("No se tienen generos registrados.")
        os.system("pause")
    else:
        for i,item in dataTemp.items():
            print(f"{i} - {item.get('nombre')}")
        os.system("pause")
