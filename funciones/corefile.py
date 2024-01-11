import json
import os
DATABASE = ''

def readFile():
    with open(DATABASE,"r") as rf:
        return json.load(rf)
def newFile(*args):
    with open(DATABASE,"w") as wf:
        json.dump(args[0],wf,indent=4)

def checkFile(*args):
    data = list(args)
    if os.path.isfile(DATABASE):
        if len(args):
            data[0].update(readFile())
    else:
        if len(args):
            newFile(data[0])

def addData(*args):
    with open(DATABASE,"r+") as wrf:
        data = json.load(wrf)
        if len(args)>1:
            data.update({args[0]:args[1]})
        else:
            data.update(args[0])
        wrf.seek(0)
        json.dump(data,wrf,indent=4)
        wrf.close()

def delData(*args):
    data = list(args)
    data[1].pop(data[0])
    newFile(data[1])

def validar(txt,tipo):
    isTrue = True
    while isTrue:
        try:
            valor = tipo(input(f"{txt}"))
        except ValueError:
            print("Error en el dato de ingreso...")
            os.system("pause")
        else:
            if len(valor)==0:
                print("olvido ingresar un dato")
            else: 
                return valor