import json
import os
DATABASE = ''

def readFile(*args):
    with open(args[0],"r") as rf:
        return json.load(rf)
    
def newFile(*args):
    with open(args[0],"w") as wf:
        json.dump(args[1],wf,indent=4)

def checkFile(*args):
    data = list(args)
    if os.path.isfile(args[0]):
        if len(args):
            data[1].update(readFile(data[0]))
    else:
        if len(args):
            newFile(data[0],data[1])

def addData(*args):
    with open(args[0],"r+") as wrf:
        data = json.load(wrf)
        if len(args)>1:
            data.update({args[1]:args[2]})
        else:
            data.update(args[1])
        wrf.seek(0)
        json.dump(data,wrf,indent=4)
        wrf.close()

def delData(*args):
    data = list(args)
    data[2].pop(data[1])
    newFile(data[0],data[2])

def validar(txt,tipo):
    isTrue = True
    while isTrue:
        try:
            valor = tipo(input(f"{txt}"))
        except ValueError:
            print("Error en el dato de ingreso...")
            os.system("pause")
        else:
            if tipo==str:
                if len(valor)==0:
                    print("Error en el dato de ingreso...")
            else: 
                return valor
            return valor