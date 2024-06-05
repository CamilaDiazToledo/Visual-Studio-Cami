#DICCIONARIO TRAINERS
Trainers = {
    "12": {
        "Nombre y Apellidos": "Fulano De tal",
        "Cedula": "12",
        "Salones": {"Salon": "Horario"},
        "Ruta": {},
        "Campers a cargo": {}
    },
    "13": {
        "Nombre y Apellidos": "Fulano",
        "Cedula": "13",
        "Salones": {"Salon": "Horario"},
        "Ruta": {},
        "Campers a cargo": {}
    }
}



#DICCIONARIO CAMPERS
Campers = {
    "1": {
        "Nombre y Apellidos": "Juan Mora",
        "Documento": "1",
        "Direccion": "Calle 13 #34-70",
        "Telefono": 3163449500,
        "Estado": "Aprobado",
        "Riesgo": False,
        "Horario": "Horas",
        "Ruta": {
            "Backend": {
                "Modulos": {"NetCore", "Spring Boot", "NodeJS", "Express"}
            }
        }
    }
}






#DICCIONARIO SALONES
Salones = {
    "Apolo06": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Ruta":"Funcionaaaa",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Apolo10": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Apolo14": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Apolo18": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Artemis06": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Artemis10": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Artemis14": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Artemis18": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Sputnik06": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Sputnik10": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Sputnik14": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    },
    "Sputnik18": {
        "Documento Trainer": "sin asignar",
        "Nombre Trainer": "sin asignar",
        "Cupo disponible": 33,
        "Cupos asignados": 0,
        "Campers Asignados": {}
    }
}

#DICCIONARIO RUTAS
Ruta = {
    "Fundamentos Programacion": {
        "Modulos": {"Introducción a la algoritmia", "PSeInt", "Python"}
    },
    "Programación Web": {
        "Modulos": {"HTML", "CSS", "Bootstrap"}
    },
    "Programación Formal": {
        "Modulos": {"Java", "JavaScript", "C#"}
    },
    "Bases Datos": {
        "Modulos": {"Principal": "Mysql", "Alternativo": None}
    },
    "Backend": {
        "Modulos": {"NetCore", "Spring Boot", "NodeJS", "Express"}
    }
}
#LISTA RIESGO ALTO
Riesgo_Alto=[]
#LISTA CAMPERS ESTADO INSCRITO
Estado_Inscrito=[]
#LISTA CAMPER ESTADO APROBADO
Campers_Aprobados=[]
#LISTA TRAINERS QUE SE ENCENTRAN TRABAJANDO EN CAMPUS
Trainers_Trabajando=[]
#LISTA CAMPERS APROBARON EL MODULO
Aprobaron_modulo=[]
#LISTA CAMPERS REPROBARON EL MODULO
Reprobaron_MODULO=[]
