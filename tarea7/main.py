class Medico:
    def __init__(self, id_medico, nombre, especialidad):
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad

    def mostrar_info(self):
        print(f"ID: {self.id_medico}, Nombre: {self.nombre}, Especialidad: {self.especialidad}")

class Paciente:
    def __init__(self, id_paciente, nombre, edad):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"ID: {self.id_paciente}, Nombre: {self.nombre}, Edad: {self.edad}")

class Hospital:
    def __init__(self):
        self.medicos = []
        self.pacientes = []

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def mostrar_medicos(self):
        for medico in self.medicos:
            medico.mostrar_info()

    def mostrar_pacientes_menores(self):
        for paciente in self.pacientes:
            if paciente.edad < 18:
                paciente.mostrar_info()

    def mostrar_pacientes_mayores(self):
        for paciente in self.pacientes:
            if paciente.edad >= 18:
                paciente.mostrar_info()

    def eliminar_medico(self, id_medico):
        self.medicos = [medico for medico in self.medicos if medico.id_medico != id_medico]

    def eliminar_paciente(self, id_paciente):
        self.pacientes = [paciente for paciente in self.pacientes if paciente.id_paciente != id_paciente]

hospital = Hospital()

medico1 = Medico(1, "Dr. Pérez", "Cardiología")
medico2 = Medico(2, "Dra. López", "Neurología")

hospital.registrar_medico(medico1)
hospital.registrar_medico(medico2)

paciente1 = Paciente(1, "Ana", 16)
paciente2 = Paciente(2, "Carlos", 22)

hospital.registrar_paciente(paciente1)
hospital.registrar_paciente(paciente2)

hospital.mostrar_medicos()
hospital.mostrar_pacientes_menores()
hospital.mostrar_pacientes_mayores()

hospital.eliminar_medico(1)
hospital.eliminar_paciente(2)
