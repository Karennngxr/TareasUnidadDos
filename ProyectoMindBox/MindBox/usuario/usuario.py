from datetime import datetime
from .utils.roles import Rol

#class Usuario:
#    
#    def __init__(self, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contrasenia= str):
#        self.nombre = nombre
#        self.apellido = apellido
#        self.curp = curp
#        self.fecha_nacimiento = fecha_nacimiento
#        self.numero_control = ""
#        self.contrasenia = contrasenia
#        self.rol = Rol
        
# usuario.py

class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def mostrar_informacion(self):
        return f'Nombre: {self.nombre}, Correo: {self.correo}'
