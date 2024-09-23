import random

class Materia:
    def __init__(self, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        self.numero_control = self.generar_numero_control()
    
    def generar_numero_control(self) -> str:
        # Extraer los últimos 2 caracteres del nombre
        ultimos_digitos_nombre = self.nombre[-2:].upper()

        numero_control = f"MT{ultimos_digitos_nombre}{self.semestre}{self.creditos}{random.randint(1, 1000)}"
        return numero_control

    def __str__(self):
        return f"{self.nombre} - {self.numero_control} ({self.creditos} créditos, Semestre: {self.semestre})"

