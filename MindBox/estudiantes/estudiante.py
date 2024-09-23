from datetime import datetime

class Estudiante:
    def __init__(self, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime):
        self.numero_control = "Por asignar"  
        self.nombre = nombre # El número de control se asignará más tarde.
        self.apellido = apellido  
        self.curp = curp 
        self.fecha_nacimiento = fecha_nacimiento  


