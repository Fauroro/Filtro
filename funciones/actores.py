import os
import funciones.corefile as cf

DATA_A = 'data/actor.json'
def crearActor():
    genero = {}
    id = 0
    cf.checkFile(DATA_A,genero)
    dataTemp = cf.readFile(DATA_A)
    if len(dataTemp)==0:
        id += 1
    else:
        id = len(dataTemp) + 1
    idA = "A0"+str(id)
    nombre = cf.validar("Ingrese el nombre del actor: ",str)
    genero = {
        "id": idA,
        "nombre": nombre
    }
    cf.addData(DATA_A,idA,genero)
def listarActor():
    genero = {}
    cf.checkFile(DATA_A,genero)
    dataTemp = cf.readFile(DATA_A)
    if len(dataTemp)==0:
        print("No se tienen actores registrados.")
        os.system("pause")
    else:
        for i,item in dataTemp.items():
            print(f"{i} - {item.get('nombre')}")
        os.system("pause")
