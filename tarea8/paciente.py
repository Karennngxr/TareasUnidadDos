class Paciente:
    def __init__(self, id_paciente, nombre, edad):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"ID: {self.id_paciente}, Nombre: {self.nombre}, Edad: {self.edad}"
