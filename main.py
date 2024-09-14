class Curso:
    def __init__(self, nombre_curso, codigo_curso, instructor):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.instructor = instructor
    
    def mostrar_info_curso(self):
        print(f"Curso: {self.nombre_curso}, Código: {self.codigo_curso}, Instructor: {self.instructor}")

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

curso1 = Curso("Matemáticas", "M101", "Profesor García")
curso2 = Curso("Historia", "H202", "Profesora López")
curso3 = Curso("Programación", "P303", "Profesor Rodríguez")

estudiante1 = Estudiante("Karen", "S001", 21)
estudiante2 = Estudiante("Tito", "S002", 22)

estudiante1.agregar_curso(curso1)
estudiante1.agregar_curso(curso3)

estudiante2.agregar_curso(curso2)
estudiante2.agregar_curso(curso3)

estudiante1.mostrar_informacion()
estudiante2.mostrar_informacion()
