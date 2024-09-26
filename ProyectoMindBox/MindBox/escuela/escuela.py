from typing import List
from grupos.grupo import Grupo
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
import random


class Escuela:
    def __init__(self):
        self.estudiantes: List[Estudiante] = []
        self.maestros: List[Maestro] = []
        self.materias: List[Materia] = []
        self.grupos: List[Grupo] = []

    def numero_control_est(self) -> str:
        return f"EST{random.randint(1000, 9999)}"

    def numero_control_maest(self) -> str:
        return f"MAE{random.randint(1000, 9999)}"

    def numero_control_materias(self, nombre: str, semestre: int, creditos: int) -> str:
        ultimos_digitos_nombre = nombre[-2:].upper()
        return f"MT{ultimos_digitos_nombre}{semestre}{creditos}{random.randint(1, 1000)}"

    def registrar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for estudiante in self.estudiantes:
                print(estudiante.mostrar_info_estudiante())

    def eliminar_estudiante(self, numero_control: str):
        self.estudiantes = [est for est in self.estudiantes if est.numero_control != numero_control]

    def registrar_maestros(self, maestro: Maestro):
        self.maestros.append(maestro)

    def mostrar_maestros(self):
        if not self.maestros:
            print("No hay maestros registrados.")
        else:
            for maestro in self.maestros:
                print(f"{maestro.nombre} {maestro.apellido}, CURP: {maestro.curp}")

    def eliminar_maestro(self, numero_control: str):
        self.maestros = [maestro for maestro in self.maestros if maestro.numero_control != numero_control]

    def agregar_materia(self, materia: Materia):
        self.materias.append(materia)

    def mostrar_materias(self):
        if not self.materias:
            print("No hay materias registradas.")
        else:
            for materia in self.materias:
                print(materia)

    def eliminar_materia(self, numero_control: str):
        self.materias = [materia for materia in self.materias if materia.numero_control != numero_control]

    def registrar_grupo(self, grupo: Grupo):
        self.grupos.append(grupo)
        print(f"Grupo {grupo.id} registrado exitosamente.")

    def listar_grupos(self):
        if not self.grupos:
            print("No hay grupos registrados.")
        else:
            print("Grupos registrados:")
            for grupo in self.grupos:
                print(f"ID: {grupo.id}, Tipo: {grupo.tipo}")