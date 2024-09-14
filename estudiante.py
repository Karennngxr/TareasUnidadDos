class Estudiante:
    def __init__(self, nombre, id_estudiante, edad):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.edad = edad
        self.cursos = []
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)
    
    def mostrar_informacion(self):
        print(f"Estudiante: {self.nombre}, ID: {self.id_estudiante}, Edad: {self.edad}")
        print("Cursos inscritos:")
        for curso in self.cursos:
            curso.mostrar_info_curso()
