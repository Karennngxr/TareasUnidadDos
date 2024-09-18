class Medico:
    def __init__(self, id_medico, nombre, especialidad):
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad

    def mostrar_info(self):
        return f"ID: {self.id_medico}, Nombre: {self.nombre}, Especialidad: {self.especialidad}"
