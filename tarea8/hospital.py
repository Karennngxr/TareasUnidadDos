class Hospital:
    def __init__(self):
        self.pacientes = []
        self.medicos = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def eliminar_paciente(self, id_paciente):
        self.pacientes = [p for p in self.pacientes if p.id_paciente != id_paciente]

    def mostrar_pacientes_menores(self):
        return [p.mostrar_info() for p in self.pacientes if p.edad < 18]

    def mostrar_pacientes_mayores(self):
        return [p.mostrar_info() for p in self.pacientes if p.edad >= 18]

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def eliminar_medico(self, id_medico):
        self.medicos = [m for m in self.medicos if m.id_medico != id_medico]
