from usuario import Usuario

class Maestro(Usuario):
    def __init__(self, nombre, edad, cedula):
        super().__init__(nombre, edad)
        self.cedula = cedula

    def obtener_informacion(self):
        info_base = super().obtener_informacion()
        return f"{info_base}, Cédula: {self.cedula}"

#from usuario import Usuario
#
#class Maestro(Usuario):
#    def __init__(self, nombre, edad, cedula):
#        super().__init__(nombre, edad)
#        self.cedula = cedula
#
#    def obtener_informacion(self):
#        info_base = super().obtener_informacion()
#        return f"{info_base}, Cédula: {self.cedula}"
#
#    # Métodos específicos de maestros





























#from datetime import datetime
#
#class Maestro:
#    def __init__(self, nombre:str, apellido:str, curp:str, fecha_nacimiento:datetime):
#        self.numero_control = "Por asignar"
#        self.nombre = nombre
#        self.apellido = apellido
#        self.curp = curp
#        self.fecha_nacimiento = fecha_nacimiento
    