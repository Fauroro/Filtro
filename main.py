import os
import ui.menu as menu



if __name__=='__main__':
    isActive = True
    while isActive:
        try:
            opMenu = menu.menuP()
        except ValueError:
            print("Error en el dato de ingreso...")
            os.system("pause")
        else:
            if opMenu == 1:
                pass
            elif opMenu ==2:
                pass
            elif opMenu ==3:
                pass
            elif opMenu ==4:
                pass
            elif opMenu ==5:
                pass
            elif opMenu ==6:
                isActive = False
                print("Gracias por usar nuestros servicios")
            else:
                print("Opcion seleccionada inexistente... Intente nuevamenete")
                os.system("pause")