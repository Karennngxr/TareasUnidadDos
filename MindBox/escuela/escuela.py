from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from random import randint
from datetime import datetime

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        
    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control_estudiante(self):
        numero_control = f"1{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 10000)}"        
        return numero_control

    def generar_numero_control_maestro(self, maestro: Maestro):
        dia_actual = datetime.now().day
        anio_nacimiento = maestro.fecha_nacimiento.year
        numero_aleatorio = randint(500, 5000)
        primeras_letras_nombre = maestro.nombre[:2].upper()
        ultimas_letras_rfc = maestro.curp[-2:].upper()
        longitud_maestros = len(self.lista_maestros) + 1
        
        numero_control = f"M-{anio_nacimiento}-{dia_actual}-{numero_aleatorio}-{primeras_letras_nombre}-{ultimas_letras_rfc}-{longitud_maestros}"
        return numero_control
