from datetime import datetime
from usuario.usuario import Usuario

from usuario.utils.roles import Rol

class Estudiante(Usuario):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    def obtener_informacion(self):
        info_base = super().obtener_informacion()
        return f"{info_base}, Matrícula: {self.matricula}"

    # Métodos específicos de estudiantes

#class Estudiante(Usuario):
#    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime):
#        super().__init__(numero_control=numero_control, nombre=nombre, apellido = apellido)
#        self.numero_control = numero_control
#        self.nombre = nombre
#        self.apellido = apellido
#        self.curp = curp
#        self.fecha_nacimiento = fecha_nacimiento
#        self.Rol.Estudiante
#        

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