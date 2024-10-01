from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint

class Semestre:
    def __init__(self, numero: int, id_carrera: str):
        self.id = self.generar_id(numero, id_carrera)
        self.numero = numero
        self.id_carrera = id_carrera
        self.materias: List[Materia] = []
        self.grupos: List[Grupo] = []
        
    def generar_id(self, numero_semestre: int, id_carrera: str) -> str:
        # Incluimos el ID de la carrera dentro del ID del semestre
        return f"{id_carrera}-S{numero_semestre}-{randint(1000, 9999)}"
