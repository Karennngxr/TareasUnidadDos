from typing import List
from estudiantes.estudiante import Estudiante
from random import randint
from datetime import datetime
from maestros.maestro import Maestro 
from materias.materia import Materia

class Escuela:
    lista_Estudiantes: List[Estudiante] = []
    lista_Maestros: List[Maestro] = []
    lista_Materias: List[Materia] = []
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_Estudiantes.append(estudiante)
        
    def numero_control_est(self):
        numero_controlest = f"1{datetime.now().year}{datetime.now().month}{len(self.lista_Estudiantes)+1}{randint(0,1000)}"
        return numero_controlest
    
    def registrar_maestros(self, maestro:Maestro):
        self.lista_Maestros.append(maestro)
        
    def numero_control_maest(self):
        numero_controlmaest = f"1{datetime.now().year}{datetime.now().month}{len(self.lista_Maestros)+1}{randint(0,1000)}"
        return numero_controlmaest

    def agregar_materia(self, materia: Materia):
        self.lista_Materias.append(materia)

    def numero_control_materias(self):
        numero_control_materias = f"1{len(self.lista_Materias)}{randint(0,1000)}"
        return numero_control_materias
    
    def mostrar_materias(self):
        if not self.lista_Materias:
            print("No hay materias registradas.")
        else:
            for materia in self.lista_Materias:
                print(materia)























#1. from typing import List*
#   - Esto importa List del módulo typing, que permite declarar que ciertos atributos o métodos trabajarán con listas. En este caso, estamos utilizando List para decir que lista_Estudiantes será una lista de objetos de tipo Estudiante.
#
#*2. from estudiantes.estudiante import Estudiante*
#   - Aquí estamos importando la clase Estudiante desde el archivo estudiante.py que está en la carpeta estudiantes. Esto es necesario para poder usar la clase Estudiante dentro de la clase Escuela.
#
#*3. from random import randint*
#   - Esto importa la función randint del módulo random. La función randint(a, b) genera un número entero aleatorio entre a y b, incluyendo ambos valores. Es muy útil para crear datos aleatorios, como en este caso el número de control del estudiante.
#
#*4. from datetime import datetime*
#   - Esto importa la clase datetime del módulo datetime. Esta clase nos permite trabajar con fechas y horas en Python, algo que usaremos para generar un número de control basado en la fecha actual.
#
#*5. class Escuela:*
#   - Aquí defines la clase Escuela. Esta clase representará la entidad escuela, que tiene métodos para registrar estudiantes y generar números de control.
#
#*6. lista_Estudiantes: List[Estudiante] = []*
#   - Definimos un atributo de clase llamado lista_Estudiantes, que es una lista vacía. Este atributo almacenará todos los objetos Estudiante que sean registrados en la escuela.
#
#*7. def registrar_estudiante(self, estudiante: Estudiante):*
#   - Este es un método dentro de la clase Escuela. Recibe un objeto de tipo Estudiante como parámetro y lo agrega a la lista de estudiantes. 
#   - self.lista_Estudiantes.append(estudiante) añade el estudiante a la lista de estudiantes de la escuela.
#
#*8. def numero_control_est(self):*
#   - Este es otro método que genera el número de control para un estudiante. No recibe ningún parámetro externo, pero utiliza la lista de estudiantes registrada en la escuela.
#
#*9. numero_controlest = f"1{datetime.now().year}{datetime.now().month}{len(self.lista_Estudiantes)+1}{randint(0,1000)}"*
#   - Esta línea crea una variable numero_controlest que contiene un número de control.
#     - f"...": Este es un f-string, una manera en Python de hacer cadenas de texto con variables embebidas en ellas.
#     - datetime.now().year: Obtiene el año actual.
#     - datetime.now().month: Obtiene el mes actual.
#     - len(self.lista_Estudiantes)+1: Obtiene el número de estudiantes que hay actualmente y le suma 1, para dar el nuevo número de control.
#     - randint(0,1000): Genera un número aleatorio entre 0 y 1000, para añadir aleatoriedad al número de control.
#
#*10. return numero_controlest*
#   - Finalmente, esta línea retorna el número de control generado, que podrá ser asignado a un estudiante.
#