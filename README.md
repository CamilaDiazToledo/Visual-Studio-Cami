# 🚀 CampusLands Progrma de Gestion Academica 🚀

Este proyecto es una aplicación en Python diseñada para gestionar y seguir el progreso académico de los campers inscritos en el programa intensivo de programación de CampusLands. La aplicación permite registrar y administrar información de los campers, gestionar rutas de entrenamiento, asignar roles y evaluar el rendimiento académico.

## Tabla de contenidos 📋
| Índice | Título                                |
|--------|---------------------------------------|
| 1      | Instalación                           |
| 2      | Cómo usar                             |
| 3      | Estructura del Proyecto                |
| 4      | Funcionalidades                        |
| 5      | Reportes                               |

### Instalación 🔧
Para instalar y ejecutar el proyecto, asegúrate de tener Python 3.x y pip instalados. Luego, ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### Cómo usar :point_down:

1. Clona este repositorio: [Presiona aqui](https://github.com/CamilaDiazToledo/Visual-Studio-Cami)
2. Abre el proyecto con Visual Studio Code desgarga python y sus diversas extenciones para poder ejecutar el programa

Una vez instaladas las dependencias, puedes ejecutar el programa con el siguiente comando:
```bash
python main.py
```
Este comando iniciará la aplicación y te permitirá interactuar con la interfaz de usuario para gestionar la información de los campers y las rutas de entrenamiento.

### Estructura del Proyecto🏗️

-menu.py: Archivo principal para ejecutar el programa.
-camper2.py: Módulo que define la clase Camper y sus métodos.
-trainer2.py: Módulo que define la clase Trainer y sus métodos.
-ruta1.py: Módulo que define las rutas de entrenamiento y sus módulos.
-cusos.py: Módulo que define las áreas de entrenamiento y módulos. y se anexa y liga la informacion de otros archivos (es el mas robusto)
-funciones_json.py: Módulo con funciones auxiliares.

### Funcionalidades :dart:
1. Registro de Campers 📝: Permite ingresar y modificar la información de los campers, incluyendo identificación, nombres, apellidos, dirección, acudiente, teléfonos, estado y riesgo.

2. Gestión de Rutas de Entrenamiento 🏫: Administra diferentes rutas de entrenamiento como NodeJS, Java y NetCore. Puedes crear nuevas rutas y asignar módulos específicos.

3. Roles y Evaluación 👩‍🏫: Maneja tres roles: Camper, Trainer y Coordinador. Los Coordinadores pueden registrar notas, cambiar estados a "Aprobado" y asignar rutas de entrenamiento. Los Trainers evalúan a los campers con pruebas teóricas y prácticas.

4. Asignación de Módulos y Evaluación 📚: Permite asignar módulos de formación y evaluar a los campers al final de cada módulo. Se calcula la nota final considerando pruebas teóricas, prácticas y quizes.

5. Consultas y Reportes 📊: Genera reportes detallados sobre el estado de los campers, los que aprobaron o perdieron módulos, y el desempeño de los trainers.

### Reportes :memo:
- Listar los campers en estado de inscrito.
- Listar los campers que aprobaron el examen inicial.
- Listar los trainers trabajando con CampusLands.
- Listar los campers con bajo rendimiento.
- Listar campers y trainers asociados a una ruta de entrenamiento.
- Mostrar estadísticas de módulos aprobados y perdidos.

Hecho por [Maria Camila Dìaz Toledo](https://github.com/CamilaDiazToledo) ✒️

> [!NOTE]
>Asegúrate de tener los permisos adecuados para acceder a las funcionalidades de administrador.

>[!TIP]
>Usa venv para crear un entorno virtual y mantener las dependencias del proyecto aisladas.

>[!IMPORTANT]
>Guarda regularmente el progreso para evitar pérdida de datos.

>[!WARNING]
>Verifica que todas las rutas y módulos estén correctamente asignados para evitar conflictos.

>[!CAUTION]
>No excedas la capacidad máxima de los módulos para asegurar una formación óptima.
