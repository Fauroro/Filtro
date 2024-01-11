import os
import funciones.corefile as cf

DATA_F = 'data/formato.json'
def crearFormato():
    genero = {}
    cf.checkFile(DATA_F,genero)
    dataTemp = cf.readFile(DATA_F)
    if len(dataTemp)==0:
        id += 1
    else:
        id = len(dataTemp) + 1
    idF = "A0"+str(id)
    nombre = cf.validar("Ingrese el nombre del formato: ",str)
    genero = {
        "id": idF,
        "nombre": nombre
    }
    cf.addData(DATA_F,idF,genero)
def listarFormato():
    genero = {}
    cf.checkFile(DATA_F,genero)
    dataTemp = cf.readFile(DATA_F)
    if len(dataTemp)==0:
        print("No se tienen formatos registrados.")
        os.system("pause")
    else:
        for i,item in dataTemp.items():
            print(f"{i} - {item.get('nombre')}")
        os.system("pause")
