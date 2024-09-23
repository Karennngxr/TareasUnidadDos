from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia

class Grupo:
    def __init__(self, id: int, tipo: str):
        self.id = id
        self.estudiantes: List[Estudiante] = []
        self.maestros: List[Maestro] = []
        self.materias: List[Materia] = []
        self.tipo = tipo

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def agregar_maestro(self, maestro: Maestro):
        self.maestros.append(maestro)

    def agregar_materia(self, materia: Materia):
        self.materias.append(materia)
