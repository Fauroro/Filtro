import os
import funciones.corefile as cf

DATA_G = 'data/genero.json'
def crearGenero():
    genero = {}
    cf.checkFile(DATA_G,genero)
    id = cf.validar("Ingrese el ID del genero: ",str)
    nombre = cf.validar("Ingrese el nombre del genero: ",str)
    genero = {
        "id": id,
        "nombre": nombre
    }
    cf.addData(DATA_G,id,genero)
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
