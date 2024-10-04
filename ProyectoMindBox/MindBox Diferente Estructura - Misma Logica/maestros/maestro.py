from usuario.usuario import Usuario
from usuario.utils.roles import Roles

class Maestro(Usuario):
    rfc: str
    sueldo: float
    año_nacimiento: int

    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float, numero_control: str, año: int, contraseña: str):
        super().__init__(nuemro_de_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Roles.MAESTRO)
        self.rfc=rfc
        self.sueldo=sueldo
        self.año_nacimiento=año

    def mostrar_info_maestro(self):
        nombre_completo=f"{self.nombre} {self.apellido}"
        info=f"-Numero de control: {self.numero_control}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}, Rol{self.rol.value}"
        return info



























#from datetime import datetime
#
#class Maestro:
#    def __init__(self, nombre:str, apellido:str, curp:str, fecha_nacimiento:datetime):
#        self.numero_control = "Por asignar"
#        self.nombre = nombre
#        self.apellido = apellido
#        self.curp = curp
#        self.fecha_nacimiento = fecha_nacimiento
    