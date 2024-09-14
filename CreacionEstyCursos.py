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
