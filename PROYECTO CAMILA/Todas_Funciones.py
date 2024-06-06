
import json

def cargar_datos(Nombre_Archivo, Tipo):
    try:
        with open(Nombre_Archivo, "r") as file:
            Diccionario = json.load(file)
        print("INFORMACION ACTUALIZADA!!")
        return Diccionario
    except FileNotFoundError:
        if Tipo == "d":
            return {}
        elif Tipo == "l":
            return []
        

def guardar_datos(Diccionario,Nombre_Archivo):
    try:
        contenido = json.dumps(Diccionario, indent=4)
        with open(Nombre_Archivo, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

#REGISTROS

#REGISTRO CAMPER
def Registro_camper(): # 
    while True:
        try:
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
        except ValueError:
            print("error")
#Registro_camper()

#REGISTRO TRAINER
def Registro_trainer():# 
    
    while True:
        try:
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
                        profesor["Horario"] = {}
                        profesor["Cursos a cargo"] = {}
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
        except ValueError:
            print("error")
        

Registro_trainer()

#NOTAS 
#CAMBIO DE ESTADO A APROBADO 
def Estado_aprobado():# 
    try:
        data=cargar_datos("Campers.json","d")
        lista=cargar_datos("Lista_Aprobados.json","l")

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
                guardar_datos(lista,"Lista_Aprobados.json")
                print("Actualizacion exitosa del estado a Aprobado")
                print(lista)
            else:
                print("Resultado no apto para modificacion de estado...")
    except ValueError:
        print("error")           

#Estado_aprobado()

#NOTAS DE MODULOS


#ASIGNACION CURSO//SALON
#ASIGNACION CAMPER
def Asignacion_cursos_camper(): # 
    with open("Cursos.json", "r") as curso_file:
        cursos = json.load(curso_file)

    with open("Campers.json", "r") as campers_file:
        campers = json.load(campers_file)

    while True:
        try:
            print("\nApolo\nSputnik\nArtemis\nSalir")
            Salon = input("Ingrese el nombre del salón a elegir o escriba salir: ").upper()
            if Salon == "SALIR":
                print("Saliendo...")
                break
            if Salon not in ["APOLO", "SPUTNIK", "ARTEMIS"]:
                print("El nombre del salón ingresado no es válido.")
                continue

            print("06\n10\n14\n18")
            hora = input("Ingrese la hora en la que inicia la clase, tal cual lo indicado arriba: ")

            nombre_curso = Salon[0:2] + hora

            if nombre_curso in cursos:
                if cursos[nombre_curso]["Cupos asignados"] < 33:
                    doc_persona = input(f"Ingrese el número de documento de la persona que desea asignar al salon {Salon}: ")
                    if doc_persona in campers:
                        repetido = False
                        for nombre_cursos in cursos.values():
                            campers_asignados = nombre_cursos.get("Campers Asignados", {})
                            if doc_persona in campers_asignados.keys():
                                repetido = True
                                break
                        if repetido:
                                print(f"Esta persona, {campers[doc_persona]['Nombre y Apellidos']} ya está asignada en un curso, por favor reinicie el proceso")
                                continue
                        else:
                            fecha_inicio=d+"/"+m+"/"+a
                            print("Ingrese la fecha de inicio:  ")
                            d=int(input("Dia: "))
                            m=int(input("Mes: "))
                            a=int(input("Año: "))
                            fecha_fin=d+"/"+m+"/"+a
                            print("Ingrese la fecha de finalizacion:  ")
                            d=int(input("Dia: "))
                            m=int(input("Mes: "))
                            a=int(input("Año: "))
                            print(f"{campers[doc_persona]['Nombre y Apellidos']} será asignado al curso {nombre_curso} al salon {Salon} en el horario de las {hora}:00, empezando el {fecha_inicio} y finalizando el {fecha_fin}")
                            validacion = int(input("¿Está seguro de la asignación?\n1.Si\n2.No"))
                            while True:
                                if validacion == 1:
                                    if campers[doc_persona]["Estado"]=="Aprobado":
                                        persona_asignada = (doc_persona, f"Nombre: {campers[doc_persona]['Nombre y Apellidos']} ")
                                        cursos[nombre_curso]["Campers Asignados"].update([persona_asignada])
                                        cursos[nombre_curso]["Cupos asignados"] += 1
                                        cursos[nombre_curso]["Cupo disponible"] -= 1
                                        campers[doc_persona]["Curso"] = nombre_curso
                                        campers[doc_persona]["Salon"] = Salon
                                        campers[doc_persona]["Horario"] = f"Inicia a las {hora}:00 hrs en el salon {Salon}"
                                        campers[doc_persona]["Ruta"] = cursos[nombre_curso]["Ruta"]
                                        campers[doc_persona]["Modulos"] = cursos[nombre_curso]["Modulos"]
                                        campers[doc_persona]["Fecha Inicio"] = fecha_inicio
                                        campers[doc_persona]["Fecha Fiinalizacion"] = fecha_fin
                                        guardar_datos(campers,"Campers.json")
                                        guardar_datos(cursos,"Cursos.json")
                                        print(f"El Camper {campers[doc_persona]['Nombre y Apellidos']} asignado correctamente ")
                                        break
                                    else:
                                        print(f"El estado de {campers[doc_persona]['Nombre y Apellidos']} es diferente a APROBADO\n NO puede ser asignado a un salon o curso")
                                        break
                                elif validacion == 2:
                                        print("Usted seleccionó 2.No, por favor reinicie el proceso")
                                        break
                                else:
                                    print("Opción no válida por favor seleccione 1 o 2 ")
                                    print(f"{campers[doc_persona]['Nombre y Apellidos']} será asignado al curso {nombre_curso} al salon {Salon} en el horario de las {hora}:00")
                                    validacion = int(input("¿Está seguro de la asignación?\n1.Si\n2.No"))
                    else:
                        print("Este documento no existe en el registro")
                else:
                    print("No hay cupos disponibles para este curso.")                    
            else:
                print("No se encontró ningún curso con el nombre y la hora especificados.")                       
                
        except ValueError:
            print("error")            
#Asignacion_cursos_camper()

#ASIGNACION TRAINER
def Asignacion_cursos_trainer():#
    with open("Cursos.json", "r") as curso_file:
        cursos = json.load(curso_file)

    with open("Trainers.json", "r") as trainers_file:
        trainers = json.load(trainers_file)

    while True:
        try:
            print("\nApolo\nSputnik\nArtemis\nSalir")
            Salon = input("Ingrese el nombre del salón a elegir o escriba salir: ").upper()
            if Salon == "SALIR":
                print("Saliendo...")
                break
            if Salon not in ["APOLO", "SPUTNIK", "ARTEMIS"]:
                print("El nombre del salón ingresado no es válido.")
                continue

            print("06\n10\n14\n18")
            hora = input("Ingrese la hora en la que inicia la clase, tal cual lo indicado arriba: ")

            nombre_curso = Salon[0:2] + hora

            if nombre_curso in cursos:
                doc_persona = input(f"Ingrese el número de documento de la persona que desea asignar al salon {Salon}: ")
                if cursos[nombre_curso]["Documento Trainer"] == "sin asignar":
                    
                    
                    if doc_persona in trainers:
                        repetido = False
                        for salones_existentes, doctrain in cursos.items():
                            if salones_existentes[-2:] == nombre_curso[-2:] and doctrain.get("Documento Trainer") == doc_persona:
                                repetido = True
                                break
                        if repetido:
                                print(f"Esta persona, {trainers[doc_persona]['Nombre y Apellidos']} ya está asignada en un curso, por favor reinicie el proceso")
                                continue
                        else:
                            print(f"{trainers[doc_persona]['Nombre y Apellidos']} será asignado al curso {nombre_curso} al salon {Salon} en el horario de las {hora}:00")
                            validacion = int(input("¿Está seguro de la asignación?\n1.Si\n2.No"))
                            while True:
                                if validacion == 1:
                                    
                                        trainers[doc_persona]["Cursos a cargo"].update({"Grupo": nombre_curso})
                                        trainers[doc_persona]["Horario"].update({"Inicio": "Inicia a las {hora}:00 hrs".format(hora=hora), "Salon": "En el salon {Salon}".format(Salon=Salon)})
                                        cursos[nombre_curso]["Documento Trainer"] = doc_persona
                                        cursos[nombre_curso]["Nombre Trainer"] = trainers[doc_persona]["Nombre y Apellidos"]
                                        guardar_datos(trainers,"Trainers.json")
                                        guardar_datos(cursos,"Cursos.json")
                                        print(f"El Trainer {trainers[doc_persona]['Nombre y Apellidos']} asignado correctamente ")
                                        break
                                elif validacion == 2:
                                        print("Usted seleccionó 2.No, por favor reinicie el proceso")
                                        break
                                else:
                                    print("Opción no válida por favor seleccione 1 o 2 ")
                                    print(f"{trainers[doc_persona]['Nombre y Apellidos']} será asignado al curso {nombre_curso} al salon {Salon} en el horario de las {hora}:00")
                                    validacion = int(input("¿Está seguro de la asignación?\n1.Si\n2.No"))
                    else:
                        print("No existe documeto en el registro.")               
                else:
                    validacion=int(input(f"Ya existe un trainer asignado a este salon desea cambiar a {cursos[nombre_curso]["Nombre Trainer"]} por {trainers[doc_persona]['Nombre y Apellidos']}\n 1.Si\n 2.No."))
                    if validacion == 1:
                        
                        
                        trainers[doc_persona]["Cursos a cargo"].update({"Grupo": nombre_curso})
                        trainers[doc_persona]["Horario"].update({"Inicio": "Inicia a las {hora}:00 hrs".format(hora=hora), "Salon": "En el salon {Salon}".format(Salon=Salon)})
                        cursos[nombre_curso]["Documento Trainer"] = doc_persona
                        cursos[nombre_curso]["Nombre Trainer"] = trainers[doc_persona]["Nombre y Apellidos"]
                        guardar_datos(trainers,"Trainers.json")
                        guardar_datos(cursos,"Cursos.json")
                        print(f"El Trainer {trainers[doc_persona]['Nombre y Apellidos']} asignado correctamente ")
                        break
                    elif validacion == 2:
                                        print("Usted seleccionó 2.No, por favor reinicie el proceso")
                                        break
                    else:
                        validacion=int(input(f"Ya existe un trainer asignado a este salon desea cambiar a {cursos[nombre_curso]["Nombre Trainer"]} por {trainers[doc_persona]['Nombre y Apellidos']}\n 1.Si\n 2.No."))


        except ValueError:
            print("error")

import json

#CREACION DE RUTA
def Creacion_ruta():#
    with open("Rutas.json", "r") as ruta_file:
        rutas = json.load(ruta_file)
    while True:
        try:
            ruta_nueva=[]
            print("**************************************************************************************")
            nombre_ruta=input("Escriba el nombre de la nueva ruta que desea agregar o enter para salir:  ").title()
            if nombre_ruta=="":
                print("Saliendo...")
                break
            if nombre_ruta not in rutas:
                ruta_nueva+=[NotImplemented]
                print("¿Esta seguro que desea agregar ",nombre_ruta," a las rutas?: ")
                validacion=int(input("1.Si\n2.No"))
                while True:
                    if validacion==1:
                        rutas["Rutas"]=ruta_nueva
                        guardar_datos(rutas,"Ruta.json")
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
        except ValueError:
            print("error")           



#ASIGNACION RUTA A GRUPO//CURSO

def Asignacion_ruta():
    with open("Cursos.json", "r") as curso_file:
        cursos = json.load(curso_file)

    with open("Rutas.json", "r") as ruta_file:
        rutas = json.load(ruta_file)
    
    while True:
        try:
            
            dicc_modulo={}


            nombre_curso = input("Ingrese el nombre del curso al que desea asignar la ruta:  ")

            if nombre_curso in cursos:
                print("Estas son las rutas existentes hasta el momento: ")
                for i in rutas["Rutas"]:
                    print(i)
                nombre_ruta=input(f"Ingrese el nombre de la ruta que desea asignar a {nombre_curso}")
                print("A continuacion los posibles modulos que se pueden agregar a la lista")
                for llave, valor in cursos["Modulos"].items():
                    print(llave,valor)
                cantidad=int(input("¿Cuantos modulos va agregar? :  "))
                for i in range(0,cantidad):
                    modulo=str(input("Escriba el modulo para agregar a la ruta :   "))
                    dicc_modulo.update({modulo:"sin asignar"})
                print("Estos son los modulos ",dicc_modulo, " de la Ruta", nombre_ruta)
                

                print(f"La ruta {nombre_ruta} y los modulos {dicc_modulo} seran asignados al curso {nombre_curso}")
                validacion = int(input("¿Está seguro de la asignación?\n1.Si\n2.No"))
                while True:
                    if validacion == 1:
                        cursos[nombre_curso]["Ruta"]=nombre_ruta
                        cursos[nombre_curso]["Modulos"]=dicc_modulo

            else:
                print("No se encontró ningún curso con el nombre y la hora especificados.") 
        except ValueError:
            print("error")           

#Asignacion_ruta()

#CREACION DE RUTA
def Creacion_ruta():
    with open("Rutas.json", "r") as ruta_file:
        rutas = json.load(ruta_file)
    while True:
        ruta_nueva=[]
        print("**************************************************************************************")
        nombre_ruta=input("Escriba el nombre de la nueva ruta que desea agregar o enter para salir:  ").title()
        if nombre_ruta=="":
            print("Saliendo...")
            break
        if nombre_ruta not in rutas:
            ruta_nueva+=[NotImplemented]
            print("¿Esta seguro que desea agregar ",nombre_ruta," a las rutas?: ")
            validacion=int(input("1.Si\n2.No"))
            while True:
                if validacion==1:
                    rutas["Rutas"]=ruta_nueva
                    guardar_datos(rutas,"Ruta.json")
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




