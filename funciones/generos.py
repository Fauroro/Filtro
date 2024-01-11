import os
import funciones.corefile as cf

DATA_G = 'data/genero.json'
def crearGenero():
    genero = {}
    id = 0
    cf.checkFile(DATA_G,genero)
    dataTemp = cf.readFile(DATA_G)
    if len(dataTemp)==0:
        id += 1
    else:
        id = len(dataTemp) + 1
    idG = "G0"+str(id)
    nombre = cf.validar("Ingrese el nombre del genero: ",str)
    genero = {
        "id": idG,
        "nombre": nombre
    }
    cf.addData(DATA_G,idG,genero)
def listarGenero():
    genero = {}
    cf.checkFile(DATA_G,genero)
    dataTemp = cf.readFile(DATA_G)
    if len(dataTemp)==0:
        print("No se tienen generos registrados.")
        os.system("pause")
    else:
        for i,item in dataTemp.items():
            print(f"{i} - {item.get('nombre')}")
        os.system("pause")
