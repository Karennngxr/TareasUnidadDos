from usuario import Usuario

class Coordinador(Usuario):
    def __init__(self, nombre, correo, contraseña, sueldo, rfc, años_antiguedad):
        super().__init__(nombre, correo, contraseña)
        self.sueldo = sueldo
        self.rfc = rfc
        self.años_antiguedad = años_antiguedad

    def mostrar_informacion(self):
        info_usuario = super().mostrar_informacion()
        return f'{info_usuario}, Sueldo: {self.sueldo}, RFC: {self.rfc}, Años de Antigüedad: {self.años_antiguedad}'
