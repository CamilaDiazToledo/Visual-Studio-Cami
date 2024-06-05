from Diccionarioss import*
from Curso import*
from Trainer2 import*
from Camper2 import*
from Ruta1 import*



from algo import*

        

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
                    registro_camper()
                elif opc2 == 2:
                    print("1. Cambio de estado a aprobado")
                    opc3 = int(input("Digite el número de la opción que desea elegir: "))
                    
                    if opc3 == 1:
                        Estado_aprobado()
                    
                elif opc2 == 3:
                    print("1. Asignación de curso")
                    print("2. Asignación de Fecha de Inicio y Finalización")
                    opc4 = int(input("Digite el número de la opción que desea elegir: "))
                    
                    if opc4 == 1:
                        Asignacion_cursos()

            elif opc1 == 2:
                print("1. Registro Trainer")
                print("2. Asignación Curso")
                opc5 = int(input("Digite el número de la opción que desea elegir: "))
                
                if opc5 == 1:
                    Registro_trainer()
                elif opc5 == 2:
                    Asignacion_cursos()
            elif opc1 == 3:
                print("1. Creacion Ruta")
                print("2. Asignación Ruta")
                opc6 = int(input("Digite el número de la opción que desea elegir: "))
                if opc6 ==1:
                    Cracion_Ruta()
                elif opc6==2:
                    Asignacion_Ruta()
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
                    print("Campers y trainers de una misma ruta de entrenamiento:", campers_trainers_ruta)
                elif opc7 == 6:
                    print("Resultados de los campers que aprobaron o no los módulos:", resultados_modulos)
                
            
            # Otras opciones para el coordinador (Gestión Trainers, Reportes) pueden añadirse aquí
        # MENU TRAINER
        elif rol == 2:
            contraseña = 122
            cont = int(input("Ingrese el código de su rol: "))
            if cont != contraseña:
                print("Código incorrecto, reinicie el proceso...")
                continue
            print("********************************")
            print("Bienvenido Trainer")
            doc = input("Digite su numero de cedula: ")
            if doc not in Trainers:
                print("Documento inexistente")
                break
            print("1. Asignacion de Notas")
            print("2. Ver grupo y su información")
            print("3. Ver Horario")
            opc1 = int(input("Digite el número de la opción que desea elegir: "))
            
            if opc1 == 1:
                Registrar_Notas(Campers)
            elif opc1 == 2:
                print("Información del grupo:", informacion_grupo)
            elif opc1 == 3:
                print("Horario:", horario)
            
            

        # MENU CAMPER
        elif rol == 3:
            contraseña = 123
            cont = int(input("Ingrese el código de su rol: "))
            if cont != contraseña:
                print("Código incorrecto, reinicie el proceso...")
                continue
            print("********************************")
            print("Bienvenido Trainer")
            doc = input("Digite su numero de cedula: ")
            with open("Campers.json", "r") as file:
                    campers_data = json.load(file)
            if doc not in campers_data:
                print("Documento inexistente")
                break
            
            print("1. Ver informacion personal")
            print("2. Ver informacion del curso")
            if opc1==1:
                print("su informacion personal es:", )
   
