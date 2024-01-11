import os
import json
import funciones.corefile as cf

DATAG = 'data/genero.json'
def crearGenero():
    genero = {}
    cf.checkFile(DATAG,genero)
    id = cf.validar("Ingrese el ID del genero: ",str)
    nombre = cf.validar("Ingrese el nombre del genero: ",str)
    genero = {
        "id": id,
        "nombre": nombre
    }
    cf.addData(DATAG,id,genero)
def listarGenero():
    genero = {}
    cf.checkFile(DATAG,genero)
    dataTemp = cf.readFile(DATAG)
    if len(dataTemp)==0:
        print("No se tienen generos registrados.")
        os.system("pause")
    else:
        for i,item in dataTemp.items():
            print(f"{i} - {item.get('nombre')}")
            # for key,valor in item.items():
            #     print(f"{key} - {valor}")
        os.system("pause")
