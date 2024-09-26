from typing import List
from random import randint
from materias.materia import Materia
from grupos.grupo import Grupo

class Semestre:
    def __init__(self, numero:int, id_carrera:str):
        self.id = self.generar_id(numero)
        self.numero = numero
        self.materias: List[Materia] = []
        self.grupos: List[Grupo] = []
        self.id_carrera = id_carrera
        
    def generar_id(self, numero_semestre:int) -> str:
        return f"{numero_semestre}-{randint(0,100000)}-{randint(0,100000)}"