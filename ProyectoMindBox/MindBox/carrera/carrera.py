from typing import List
from materias.materia import Materia
from estudiantes.estudiante import Estudiante
from semestre.semestre import Semestre
from random import randint

class Carrera:
    def __init__(self, nombre: str):
        self.matricula = self.generar_id(nombre)  # Genera un ID único basado en el nombre
        self.nombre = nombre
        self.numero_semestres: int = 0
        self.semestres: List[Semestre] = []

    def generar_id(self, nombre: str) -> str:
        # Generar ID basado en el nombre de la carrera y números aleatorios
        return f"{nombre[:3].upper()}-{randint(1000, 9999)}-{randint(1000, 9999)}"

    def registrar_semestre(self, semestre: Semestre):
        self.semestres.append(semestre)

    def mostrar_info(self):
        return f"Carrera: {self.nombre}, ID: {self.matricula}"