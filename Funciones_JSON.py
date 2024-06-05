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


