from datetime import datetime

class Maestro:
    
    numero_control: str
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime
    salario: float
    
    def __init__(self, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, salario: float):
        self.numero_control = "Por asignar"
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento
        self.salario = salario
