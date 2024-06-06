
from Todas_Funciones import*




        

def menu():
    while True:
        print("************************************************")
        print("¿Qué rol tienes? Selecciona un número: ")
        print("1. Coordinador")
        print("2. Trainer")
        print("3. Camper")
        rol = int(input())

        # MENU COORDINADOR
        if rol == 1:
            contraseña = 121
            cont = int(input("Ingrese el código de su rol: "))
            if cont != contraseña:
                print("Código incorrecto, reinicie el proceso...")
                continue
            print("********************************")
            print("Bienvenido Coordinador")
            print("1. Gestión Campers")
            print("2. Gestión Trainers")
            print("3. Gestion Ruta")
            print("4. Reportes")
            opc1 = int(input("Digite el número de la opción que desea elegir: "))
            
            # 1GESTIÓN CAMPERS
            if opc1 == 1:
                print("1. Inscripción Campers")
                print("2. Cambio de Estado")
                print("3. Módulo Matrícula")
                opc2 = int(input("Digite el número de la opción que desea elegir: "))
                
                if opc2 == 1:
                    Registro_camper()
                elif opc2 == 2:
                    print("1. CambIar estado a aprobado")
                    print("2. CambIar estado a otro")
                    opc3 = int(input("Digite el número de la opción que desea elegir: "))
                    
                    if opc3 == 1:
                        Estado_aprobado()
                    elif opc3 == 1:
                        #FALTA
                        pass
                    
                elif opc2 == 3:
                    print("1. Asignación de salon, curso, asignacion fechas, y ruta")
                    opc4 = int(input("Digite el número de la opción que desea elegir: "))
                    
                    if opc4 == 1:
                        Asignacion_cursos_camper()
                    else:
                        print("no valido")

            elif opc1 == 2:
                print("1. Registro Trainer")
                print("2. Asignación Curso")
                opc5 = int(input("Digite el número de la opción que desea elegir: "))
                
                if opc5 == 1:
                    Registro_trainer()
                elif opc5 == 2:
                    Asignacion_cursos_trainer()
            elif opc1 == 3:
                print("1. Creacion Ruta")
                print("2. Asignación Ruta")
                opc6 = int(input("Digite el número de la opción que desea elegir: "))
                if opc6 ==1:
                    Creacion_ruta()
                elif opc6==2:
                    Asignacion_ruta()
            elif opc1 == 4:
                print("1. Ver campers en estado de inscrito.")
                print("2. Ver campers que aprobaron el examen inicial.")
                print("3. Ver trainers de CampusLands.")
                print("4. Ver campers con bajo rendimiento.")
                print("5. Ver campers y trainers de una misma ruta de entrenamiento.")
                print("6. Ver resultados de los campers que aprobaron o no los módulos.")
                opc7 = int(input("Digite el número de la opción que desea elegir: "))

                if opc7 == 1:
                    with open("Estado_Inscrito.json", "r") as file:
                        Estado_Inscrito = json.load(file)
                    print("Campers en estado de inscrito:", Estado_Inscrito)
                elif opc7 == 2:
                    with open("Campers_Aprobados.json", "r") as file:
                            Campers_Aprobados = json.load(file)
                    print("Campers que aprobaron el examen inicial:", Campers_Aprobados)
                elif opc7 == 3:
                    with open("Trainers_Trabajando.json", "r") as file:
                            Trainers_Trabajando = json.load(file)
                    print("Trainers de CampusLands:", Trainers_Trabajando)
                elif opc7 == 4:
                    with open("Trainers_Trabajando.json", "r") as file:
                            Trainers_Trabajando = json.load(file)
                    print("Campers con bajo rendimiento:", Aprobaron_modulo)
                elif opc7 == 5:
                   #
                   pass
                elif opc7 == 6:
                    #
                    pass
                
            
            # Otras opciones para el coordinador (Gestión Trainers, Reportes) pueden añadirse aquí
        # MENU TRAINER
        elif rol == 2:
            with open("Cursos.json", "r") as curso_file:
                cursos = json.load(curso_file)
            with open("Trainers.json", "r") as trainers_file:
                trainers = json.load(trainers_file)
            contraseña = 122
            cont = int(input("Ingrese el código de su rol: "))
            if cont != contraseña:
                print("Código incorrecto, reinicie el proceso...")
                continue
            doc_persona = input(f"Ingrese el número de documento")
            print("********************************")
            print("Bienvenido Trainer")
            doc = input("Digite su numero de cedula: ")
            if doc not in trainers:
                print("Documento inexistente")
                break
            print("1. Asignacion de Notas")
            print("2. Ver grupo y su información")
            print("3. Ver Horario")
            opc1 = int(input("Digite el número de la opción que desea elegir: "))
            
            if opc1 == 1:
                #
                pass
            elif opc1 == 2:
                nombre_grupo=input("Ingrese el grupo")
                print(cursos[nombre_grupo])
            elif opc1 == 3:
                print(trainers[doc_persona]["Horario"])
            
            

        # MENU CAMPER
        elif rol == 3:
            contraseña = 123
            with open("Campers.json", "r") as campers_file:
                campers = json.load(campers_file)
            cont = int(input("Ingrese el código de su rol: "))
            if cont != contraseña:
                print("Código incorrecto, reinicie el proceso...")
                continue
            doc_persona = input(f"Ingrese el número de documento : ")
            if doc_persona in campers:
                print("********************************")
                print("Bienvenido Camper")
                with open("Campers.json", "r") as file:
                    campers_data = json.load(file)
            if doc not in campers_data:
                print("Documento inexistente")
                break
            
            print("1. Ver informacion personal")
            print("2. Ver informacion del curso")
            if opc1==1:
                print(f"su informacion personal es: {campers[doc_persona]}", )
            elif opc1==2:
                print(campers[doc_persona]["Curso"])
                print(campers[doc_persona]["Horario"])
                print(campers[doc_persona]["Ruta"])
                print(campers[doc_persona]["Modulos"])
                print(campers[doc_persona]["Fecha Inicio"])
                print(cursos[nombre_curso]["Nombre Trainer"])

   
