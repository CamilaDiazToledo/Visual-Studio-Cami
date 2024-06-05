from Funciones_JSON import *

def Asignacion_cursos():
    salones = cargar_datos("Cursos.json", "d")
    personas = cargar_datos("Campers.json", "d")
    personas = cargar_datos("Trainers.json", "d")
    
    while True:
        print("Apolo\nSputnik\nArtemis\nSalir")
        Salon = input("Ingrese el nombre del salón a elegir: ").capitalize()
        print("06\n10\n14\n18")
        hora = input("Ingrese la hora en la que inicia la clase, tal cual lo indicado arriba: ")
        salon_seleccionado = Salon + hora

        if Salon.lower() == "salir":
            print("Saliendo...")
            break

        if salon_seleccionado in salones:
            if salones[salon_seleccionado].get("Cupos asignados", 0) < 33:
                with open("Trainers.json", "r") as file:
                    trainers_data = json.load(file)

                with open("Campers.json", "r") as file:
                    campers_data = json.load(file)

              
                doc_persona = input(f"Ingrese el número de documento de la persona que desea asignar al área {salon_seleccionado}: ")

                if doc_persona in trainers_data:
                    print("Lista de entrenadores disponibles: ")
                    for doc, nombre_trainer in trainers_data.items():
                        print(f"C.c: {doc}, Nombre: {nombre_trainer['Nombre y Apellidos']}")

                    if doc_persona not in trainers_data or campers_data:
                        print("Documento no reconocido, por favor reinicie el proceso: ")
                        continue
                    if doc_persona in trainers_data:
                        repetido = False
                        for salones_existentes, doctrain in salones.items():
                            if salones_existentes[-2:] == salon_seleccionado[-2:] and doctrain.get("Documento Trainer") == doc_persona:
                                repetido = True
                                break
                        
                        if doc_persona in campers_data:
                            repetido = False
                            for salones_existentes, info_salon in salones.items():
                                if doc_persona in info_salon.get("Campers Asignados", {}).keys():
                                    repetido = True
                                    break
                        if repetido:
                            print(f"Esta persona, {personas[doc_persona]['Nombre y Apellidos']} ya está asignada en un curso, por favor reinicie el proceso")
                            continue
                        else:
                            print(f"{personas[doc_persona]['Nombre y Apellidos']} será asignado al área {salon_seleccionado} a las {hora}:00")
                            validacion = int(input("¿Está seguro de la asignación?\n1.Si\n2.No"))
                            while True:
                                if validacion == 1:
                                    if doc_persona in trainers_data:
                                        personas[doc_persona]["Curso"] = salon_seleccionado
                                        personas[doc_persona]["Salones"] = Salon
                                        personas[doc_persona]["Horario"] = f"Inicia a las {hora}:00 hrs"
                                        personas[doc_persona]["Ruta"] = salones[salon_seleccionado]["Ruta"]
                                        salones[salon_seleccionado]["Documento Trainer"] = doc_persona
                                        salones[salon_seleccionado]["Nombre Trainer"] = personas[doc_persona]["Nombre y Apellidos"]
                                        salones[salon_seleccionado]["Horario"] = f"Inicia a las {hora}:00 hrs"
                                        guardar_datos(personas,"Trainers.json")
                                        guardar_datos(salones,"Cursos.json")
                                        print(f"Trainer {personas[doc_persona]['Nombre y Apellidos']} asignado correctamente a {salon_seleccionado}")
                                        print(salones[salon_seleccionado])
                                        print(personas[doc_persona])
                                        break
                                    else:
                                        if doc_persona in campers_data:
                                            if "Aprobado" in personas[doc_persona]["Estado"]:
                                                persona_asignada = {doc_persona: f"Nombre: {personas[doc_persona]['Nombre y Apellidos']}  Doc: {doc_persona}"}
                                                salones[salon_seleccionado]["Campers Asignados"].update(persona_asignada)
                                                salones[salon_seleccionado]["Cupos asignados"] += 1
                                                salones[salon_seleccionado]["Cupo disponible"] -= 1
                                                personas[doc_persona]["Curso"] = salon_seleccionado
                                                personas[doc_persona]["Salones"] = Salon
                                                personas[doc_persona]["Horario"] = f"Inicia a las {hora}:00 hrs"
                                                personas[doc_persona]["Ruta"] = salones[salon_seleccionado]["Ruta"]
                                                guardar_datos(personas,"Campers.json")
                                                guardar_datos(salones,"Cursos.json")
                                                print(f"El Camper {personas[doc_persona]['Nombre y Apellidos']} asignado correctamente ")
                                                print(salones[salon_seleccionado])
                                                print(personas[doc_persona])
                                                break
                                elif validacion == 2:
                                    print("Usted seleccionó 2.No, por favor reinicie el proceso")
                                    break
                                else:
                                    print("Opción no válida por favor seleccione 1 o 2 ")
                                    validacion = int(input(f"Entrenador {personas[doc_persona]['Nombre y Apellido']} será asignado al área {salon_seleccionado} a las {hora}:00\n¿Está seguro de la asignación?\n1.Si\n2.No"))
            else:
                print("El salón seleccionado no existe")
                continue

Asignacion_cursos()