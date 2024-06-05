from Diccionarioss import*
from Funciones_JSON import*


#REGISTRO DE LOS CAMPERS
def Registro_trainer():
    while True:
        data = cargar_datos("Trainers.json", "d")
        
        lista =cargar_datos("Trainers_Trabajando.json", "l")
        
        
        print("**************************************")
        doc = input("Ingrese el numero del documento :  ")
        if doc == "":
            print("Salio...")
            break
        else:
            if data.get(doc, None) == None:
                profesor = {}
                profesor["Nombre y Apellidos"] = input("Ingrese el nombre y apellidos completos:  ")
                profesor["Cedula"] = doc
                profesor["Direccion"] = input("Ingrese la direccion:  ")
                profesor["Telefono"] = input("Ingrese el Telefono de contacto :  ")
                nombre_trainer = doc + " " + profesor["Nombre y Apellidos"]
                print("Cedula: ", doc, profesor)
                print("***********************************************************************************")
                print(f"¿Esta seguro que desea inscribir a {profesor['Nombre y Apellidos']} ?: ")
                validacion = int(input("1.Si\n2.No"))
                if validacion == 1:
                    lista.append(nombre_trainer)
                    profesor["Estado"] = "Inscrito"
                    profesor["Area"] = "Salon"
                    profesor["Horario"] = "Horas"
                    data[doc] = profesor
                    guardar_datos(data, "Trainers.json")
                    guardar_datos(lista, "Trainers_Trabajando.json")
                    print("*********************************")
                    print("Camper registrado exitosamente...")
                    print(data[doc])
                    print(lista)
                elif validacion == 2:
                    print("Usted selecciono 2.No, por favor reinicie el proceso")
                    break
                else:
                    if validacion != 1 or 2:
                        print("Opción no valida por favor seleccione 1 o 2 ")
                        print(f"¿Esta seguro que desea inscribir a {profesor['Nombre y Apellidos']} ?: ")
                        validacion = int(input("1.Si\n2.No"))
            else:
                print("Camper ya registrado...")

Registro_trainer()

def Registrar_Notas(camper):
    while True:
        doc=input("Ingrese el numero del documento del camper o enter para salir:   ")
        if doc=="":
            print("Saliendo...")
            break
        if doc in camper:
            clave_ruta = Campers[doc]["Ruta"].keys()
            print(f"Ruta del camper: {Campers[doc]["Ruta"].keys()}\n Modulos: {camper[doc]["Ruta"][clave_ruta]["Modulos"]}")
            nombre_modulo=input("Ingrese el nombre del modulo a calificar")
            
            if nombre_modulo not in camper[doc]["Ruta"][clave_ruta]["Modulos"]:
                print("Este modulo no se encuentra dentro de la ruta del camper")
                continue
            info_camper=f"{nombre_modulo} {doc} {camper[doc]['Nombre y Apellidos']}"
            nombre_camper=f"{doc} {camper[doc]['Nombre y Apellidos']}"
            try:
                #npt=nota prueba teorica//npp= nota prueba practica//no=nota otros
                npt=int(input("Ingrese la nota de la prueba teorica:  "))
                npp=int(input("Ingrese la nota de la prueba practica:  "))
                cantidad_no=int(input("Ingrese la cantidad de las notas que desea registrar en otros:  "))
                cont=0
                for i in range (0,cantidad_no,1):
                    nota=int(input("Ingrese nota:  "))
                    cont=cont+nota
                no=cont/cantidad_no
            except ValueError:
                print("Solo se aceptan numeros...")
                continue
            Nota_final= (npt*0.30)+(npp*0.60)+(no*0.10)
            camper[doc]["Notas"][nombre_modulo] = Nota_final
            print("¿Esta seguro de las notas ingresadadas al camper?  ")
            validacion=int(input("1.Si\n2.No"))
            while True:
                if validacion==1:
                    if Nota_final>=60:
                        info=f"{doc} {camper[doc]['Nombre y Apellidos']}"
                        camper[doc]["Notas"][nombre_modulo]=f"Aprobado Nota: {Nota_final}" 
                        print(f"Nota final: {Nota_final} Aprobado, Registrado exitosamente")
                        break
                    else:
                        camper[doc][nombre_modulo]=f"Reprobado Nota: {Nota_final}"
                        camper[doc]["Riesgo"]="Alto"
                        print(f"Nota final: {Nota_final} Reprobado, Registrado exitosamente")
                        print(camper)
                        break
                elif validacion==2:
                        print("Usted selecciono 2.No, por favor reinicie el proceso")
                        break
                else:
                    print(f"¿Esta seguro de las notas ingresadadas al camper?  ")
                    validacion=int(input("1.Si\n2.No  "))
        else:
            print("Camper no encontrado")
