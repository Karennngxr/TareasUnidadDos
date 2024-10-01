from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from random import randint

class Grupo:
    def __init__(self, tipo: chr, id_Semestre: str, id: int = None):
        # Asignamos primero el tipo antes de generar el ID
        self.tipo = tipo
        self.id_Semestre = id_Semestre
        self.id = id if id else self.generar_id()
        self.estudiantes: List[Estudiante] = []
        self.maestros: List[Maestro] = []
        self.materias: List[Materia] = []

    # Generar ID basado en el tipo de grupo
    def generar_id(self) -> str:
        return f"{self.tipo}-{randint(0, 100000)}-{randint(0, 100000)}"

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def agregar_maestro(self, maestro: Maestro):
        self.maestros.append(maestro)

    def agregar_materia(self, materia: Materia):
        self.materias.append(materia)

    def mostrar_info_grupo(self):
        return f"Grupo ID: {self.id}, Tipo: {self.tipo}, Semestre: {self.id_Semestre}, Total de estudiantes: {len(self.estudiantes)}"

#from typing import List
#from estudiantes.estudiante import Estudiante
#from maestros.maestro import Maestro
#from materias.materia import Materia
#from random import randint
#
#class Grupo:
#    def __init__(self, id: int, tipo: chr, id_Semestre: str):
#        # Usamos el id pasado como argumento en lugar de generar uno nuevo
#        self.id = id  
#        self.tipo = tipo
#        self.id_Semestre = id_Semestre
#        self.estudiantes: List[Estudiante] = []
#        self.maestros: List[Maestro] = []
#        self.materias: List[Materia] = []
#
#    def agregar_estudiante(self, estudiante: Estudiante):
#        self.estudiantes.append(estudiante)
#
#    def agregar_maestro(self, maestro: Maestro):
#        self.maestros.append(maestro)
#
#    def agregar_materia(self, materia: Materia):
#        self.materias.append(materia)
#
#    # Generar ID basado en el tipo de grupo
#    def generar_id(self) -> str:
#        return f"{self.tipo}-{randint(0, 100000)}-{randint(0, 100000)}"
#
#    def mostrar_info_grupo(self):
#        return f"Grupo ID: {self.id}, Tipo: {self.tipo}, Semestre: {self.id_Semestre}, Total de estudiantes: {len(self.estudiantes)}"



#from typing import List
#from estudiantes.estudiante import Estudiante
#from maestros.maestro import Maestro
#from materias.materia import Materia
#
#class Grupo:
#    def __init__(self, id: int, tipo: str):
#        self.id = id
#        self.tipo = tipo
#        self.estudiantes: List[Estudiante] = []
#        self.maestros: List[Maestro] = []
#        self.materias: List[Materia] = []
#
#    def agregar_estudiante(self, estudiante: Estudiante):
#        self.estudiantes.append(estudiante)
#
#    def agregar_maestro(self, maestro: Maestro):
#        self.maestros.append(maestro)
#
#    def agregar_materia(self, materia: Materia):
#        self.materias.append(materia)


#from typing import List
#from estudiantes.estudiante import Estudiante
#from maestros.maestro import Maestro
#from materias.materia import Materia
#
#class Grupo:
#    def __init__(self, id: int, tipo: str):
#        self.id = id
#        self.estudiantes: List[Estudiante] = []
#        self.maestros: List[Maestro] = []
#        self.materias: List[Materia] = []
#        self.tipo = tipo
#
#    def agregar_estudiante(self, estudiante: Estudiante):
#        self.estudiantes.append(estudiante)
#
#    def agregar_maestro(self, maestro: Maestro):
#        self.maestros.append(maestro)
#
#    def agregar_materia(self, materia: Materia):
#        self.materias.append(materia)