from Diccionarioss import*
from Funciones_JSON2 import*

def Cracion_Ruta():
    ruta=cargar_datos("Rutas.json","d")
    while True:
        print("**************************************************************************************")
        nombre_ruta=input("Escriba el nombre de la nueva ruta que desea agregar o enter para salir:  ").title()
        if nombre_ruta=="":
            print("Saliendo...")
            break
        if ruta.get(nombre_ruta,None)==None:
            cantidad_modulos=int(input("¿Cuantos modulos desea agregar a la ruta?:  "))
            modulos=set()
            for i in range (0,cantidad_modulos,1):
                nombre_modulo=input("Ingrese el nombre del modulo a agegar:  ").capitalize()
                modulos.add(nombre_modulo)
            print("***********************************************************************************")
            print("¿Esta seguro que desea agregar en ",nombre_ruta," los siguentes modulos?: ", modulos)
            validacion=int(input("1.Si\n2.No"))
            while True:
                if validacion==1:
                    ruta[nombre_ruta]={"Modulo":modulos}
                    guardar_datos(ruta,"Ruta.json")
                    print("Ruta añadida exitosamente...")
                    print(ruta[nombre_ruta])
                    break
                elif validacion==2:
                    print("Usted selecciono 2.No, por favor reinicie el proceso")
                    break
                else:
                    if validacion!=1 or 2:
                        print("Opción no valida por favor selecione 1 o 2 ")
                        print("¿Esta seguro que desea agregar en ",nombre_ruta," los siguentes modulos?: ", modulos)
                        validacion=int(input("1.Si\n2.No"))
        else:
            print("Ruta ya existente....")
            continue

Cracion_Ruta()


def Asignacion_Ruta(salones,ruta):
    while True:
        print("**********************************************************************")
        print("Asignacion de rutas. Estas son las rutas existentes en este momento o enter para salir:  ")
        nombre_rutas=ruta.keys()
        n=1
        for i in nombre_rutas:
            print(n,i)
            n=n+1
        ruta_asignar=input("Ingrese el nombre de la ruta de la lista que desea asignar o enter para salir:  ").title()
        if ruta_asignar=="":
            print("Saliendo...")
            break
        if ruta_asignar not in ruta:
            print(f"No existe la ruta indicada {ruta_asignar}...")
            continue
        print("Estos son los nombres de los cursos existentes:  ")
        nombre_cursos=salones.keys()
        for i in nombre_cursos:
            print(n,i)
            n=n+1
        curso_seleccionado = input("Ingrese el nombre del curso: ").strip().capitalize()
        if curso_seleccionado not in salones:
            print("El curso no existe...")
            continue
        print("******************************************************************")
        print(f"¿Esta seguro que desea asignar {ruta_asignar} a {curso_seleccionado}?")
        validacion=int(input("1.Si\n2.No"))
        while True:
            if validacion==1:
                if "Ruta" in salones[curso_seleccionado]:
                    print(f"{curso_seleccionado} ya tiene asignada una ruta, por favor reinicie el proceso...")
                    break
                salones[curso_seleccionado]["Ruta"]=ruta_asignar
                print("Ruta añadida exitosamente...")
                print(salones[curso_seleccionado])
                break
            elif validacion==2:
                    print("Usted selecciono 2.No, por favor reinicie el proceso")
                    break
            else:
                    print("Opción no valida por favor selecione 1 o 2 ")
                    print(f"¿Esta seguro que desea asignar {ruta_asignar} a {curso_seleccionado}? o presione enter para salir:  ")
                    validacion=int(input("1.Si\n2.No"))
                

#Asignacion_Ruta(Salones,Ruta)
        