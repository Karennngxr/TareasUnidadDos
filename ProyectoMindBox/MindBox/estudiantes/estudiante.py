from datetime import datetime

class Estudiante:
    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info_estudiante(self):
        return f"{self.numero_control}: {self.nombre} {self.apellido}, CURP: {self.curp}, Fecha de nacimiento: {self.fecha_nacimiento}"




























#from datetime import datetime
#
#class Estudiante:
#    
#    def __init__(self, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime):
#        self.numero_control = "Por asignar"  
#        self.nombre = nombre # El número de control se asignará más tarde.
#        self.apellido = apellido  
#        self.curp = curp 
#        self.fecha_nacimiento = fecha_nacimiento  