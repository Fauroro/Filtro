import os
import ui.menu as menu



if __name__=='__main__':
    isActive = True
    head = """
++++++++++++++++++++++++++++
+    BLOCKBUSTER - MENU    +
++++++++++++++++++++++++++++
"""
    while isActive:
        os.system("cls")
        print(head)
        try:
            opMenu = menu.menuP()
        except ValueError:
            print("Error en el dato de ingreso...")
            os.system("pause")
        else:
            if opMenu == 1:
                menu.menuG()
            elif opMenu ==2:
                menu.menuA()
            elif opMenu ==3:
                menu.menuF()
            elif opMenu ==4:
                menu.menuI()
            elif opMenu ==5:
                menu.menuM()
            elif opMenu ==6:
                isActive = False
                print("Gracias por usar nuestros servicios")
            else:
                print("Opcion seleccionada inexistente... Intente nuevamenete")
                os.system("pause")