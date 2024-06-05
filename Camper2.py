from Diccionarioss import*
from Funciones_JSON import*


#REGISTRO DE LOS CAMPERS
def registro_camper():
    while True:
        data = cargar_datos("Campers.json", "d")
        
        
        lista =cargar_datos("Estado_Inscrito.json", "l")
        
        
        print("**************************************")
        doc = input("Ingrese el numero del documento :  ")
        if doc == "":
            print("Salio...")
            break
        else:
            if data.get(doc, None) == None:
                estudiante = {}
                estudiante["Nombre y Apellidos"] = input("Ingrese el nombre y apellidos completos:  ")
                estudiante["Documento"] = doc
                estudiante["Direccion"] = input("Ingrese la direccion:  ")
                estudiante["Acudiente"] = input("Ingrese el nombre completo del acudiente:  ")
                estudiante["Telefono"] = input("Ingrese el Telefono de contacto :  ")
                estudiante["Estado"] = "En proceso"
                nombre_camper = doc + " " + estudiante["Nombre y Apellidos"]
                print("Cedula: ", doc, estudiante)
                print("***********************************************************************************")
                print(f"¿Esta seguro que desea inscribir a {estudiante['Nombre y Apellidos']} ?: ")
                validacion = int(input("1.Si\n2.No"))
                if validacion == 1:
                    lista.append(nombre_camper)
                    estudiante["Estado"] = "Inscrito"
                    estudiante["Area"] = "Salon"
                    estudiante["Horario"] = "Horas"
                    estudiante["Riesgo"] = False
                    data[doc] = estudiante
                    guardar_datos(data, "Campers.json")
                    guardar_datos(lista, "Estado_Inscrito.json")
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
                        print(f"¿Esta seguro que desea inscribir a {estudiante['Nombre y Apellidos']} ?: ")
                        validacion = int(input("1.Si\n2.No"))
            else:
                print("Camper ya registrado...")

#registro_camper()
#COPIAR EL CAMBIO DE ESTADO


#registro_camper(Camper)

#CAMBIO DE ESTADO A APROBADO

def Estado_aprobado():
    data=cargar_datos("Campers.json","d")
    lista=cargar_datos("Campers_Aprobados.json","l")

    doc=input("Ingrese el numero del documento:  ")
    nombre_camper=doc+" "+data[doc]["Nombre y Apellidos"]
    if data.get(doc,None) != None:
        nt=int(input("Ingrese la nota del examen teorico de admision:  "))
        np=int(input("Ingrese la nota del examen practico de admision:  "))
        nota= (nt+np)/2
        print(nota)
        if nota>=60:
            lista.append(nombre_camper)
            data[doc]["Estado"]="Aprobado"
            guardar_datos(data,"Campers.json")
            guardar_datos(lista,"Campers_Aprobados.json")
            print("Actualizacion exitosa del estado a Aprobado")
            print(lista)
        else:
            print("Resultado no apto para modificacion de estado...")

        

    
Estado_aprobado()
    
