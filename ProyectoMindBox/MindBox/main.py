from datetime import datetime

from maestros.maestro import Maestro
from materias.materia import Materia
from grupos.grupo import Grupo
from horarios.horario import Horario

from estudiantes.estudiante import Estudiante
from escuela.escuela import Escuela

from carrera.carrera import Carrera
from semestre.semestre import Semestre  


escuela = Escuela()

# Funciones para registrar
def registrar_estudiante():
    print("---- REGISTRAR NUEVO ESTUDIANTE ----")
    nombre = input("Introduce el nombre del estudiante: ")
    apellido = input("Introduce el apellido del estudiante: ")
    curp = input("Introduce la CURP del estudiante: ")
    dia = int(input("Introduce el día de nacimiento del estudiante (DD): "))
    mes = int(input("Introduce el mes de nacimiento del estudiante (MM): "))
    anio = int(input("Introduce el año de nacimiento del estudiante (YYYY): "))

    fecha_nacimiento = datetime(anio, mes, dia)
    numero_control = escuela.numero_control_est()

    estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
    escuela.registrar_estudiante(estudiante)

    print("----- ESTUDIANTE REGISTRADO -----")
    print(estudiante.mostrar_info_estudiante())

def registrar_maestro():
    print("---- REGISTRAR NUEVO MAESTRO ----")
    nombre = input("Introduce el nombre del maestro: ")
    apellido = input("Introduce el apellido del maestro: ")
    curp = input("Introduce la CURP del maestro: ")
    dia = int(input("Introduce el día de nacimiento del maestro (DD): "))
    mes = int(input("Introduce el mes de nacimiento del maestro (MM): "))
    anio = int(input("Introduce el año de nacimiento del maestro (YYYY): "))

    fecha_nacimiento = datetime(anio, mes, dia)
    maestro = Maestro(nombre, apellido, curp, fecha_nacimiento)
    maestro.numero_control = escuela.numero_control_maest()

    escuela.registrar_maestros(maestro)

    print(f"Maestro registrado: {maestro.nombre} {maestro.apellido}, CURP: {maestro.curp}")
    print(f"Número de control: {maestro.numero_control}")

def registrar_materia():
    print("---- REGISTRAR NUEVA MATERIA ----")
    nombre = input("Introduce el nombre de la materia: ")
    descripcion = input("Introduce la descripción de la materia: ")
    semestre = int(input("Introduce el semestre de la materia: "))
    creditos = int(input("Introduce la cantidad de créditos: "))

    numero_control = escuela.numero_control_materias(nombre, semestre, creditos)
    nueva_materia = Materia(nombre, descripcion, semestre, creditos)
    nueva_materia.numero_control = numero_control

    escuela.agregar_materia(nueva_materia)

    print(f"Materia registrada: {nueva_materia}")
    print(f"Numero de control: {nueva_materia.numero_control}")


def registrar_grupo():
    print("---- REGISTRAR NUEVO GRUPO ----")
    tipo_grupo = input("Tipo de grupo (A/B/C): ")  # Pedimos solo el tipo de grupo
    id_Semestre = input("Ingresa el ID del semestre: ")  # Relacionamos el grupo con un semestre

    grupo = Grupo(tipo=tipo_grupo, id_Semestre=id_Semestre) # Creamos el objeto grupo (el ID se genera automáticamente dentro de la clase Grupo)
    
    escuela.registrar_grupo(grupo) # Registramos el grupo en la escuela
    print(f"Grupo registrado: {grupo.id} - {grupo.tipo}, Semestre: {grupo.id_Semestre}")


def registrar_horario():
    print("---- REGISTRAR NUEVO HORARIO ----")
    dia = input("Día de la semana: ")
    hora_inicio = input("Hora de inicio (HH:MM): ")
    hora_fin = input("Hora de fin (HH:MM): ")

    horario = Horario(dia, hora_inicio, hora_fin)
    print(f"Horario registrado: {horario.dia}: {horario.hora_inicio} - {horario.hora_fin}")

def registrar_carrera():
    print("---- REGISTRAR NUEVA CARRERA ----")
    nombre_carrera = input("Ingresa el nombre de la carrera: ")
    carrera = Carrera(nombre=nombre_carrera) # Crea la carrera
    escuela.registrar_carrera(carrera)  # Aquí registramos la carrera en la escuela
    print(f"Carrera {carrera.nombre} registrada con éxito. ID: {carrera.matricula}")

def registrar_semestre():
    print("---- REGISTRAR NUEVO SEMESTRE ----")
    numero = input("Introduce el número del semestre: ")
    id_carrera = input("Introduce el ID de la carrera a la que pertenece: ")
    
    semestre = Semestre(numero=numero, id_carrera=id_carrera) # Creamos el objeto Semestre
    
    escuela.registrar_semestre(semestre) # Registrar semestre en la escuela
    
    print(f"Semestre {semestre.numero} registrado exitosamente con ID: {semestre.id}")
    print(f"Semestre {semestre.numero} registrado con éxito. ID: {semestre.id}")

def menu():
    while True:
        print("\n------------ BIENVENIDO A MINDBOX ---------------")
        print("1. Registrar Estudiante")
        print("2. Registrar Maestro")
        print("3. Registrar Materia")
        print("4. Registrar Grupo")
        print("5. Registrar Horario")
        print("6. Registrar Carrera")
        print("7. Registrar Semestre")
        print("8. Mostrar estudiantes")
        print("9. Mostrar maestros")  
        print("10. Mostrar materias") 
        print("11. Mostrar grupos")
        print("12. Mostrar carreras")
        print("13. Mostrar semestres")
        print("14. Eliminar Estudiante")
        print("15. Eliminar Maestro")
        print("16. Eliminar Materia")
        print("17. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_maestro()
        elif opcion == "3":
            registrar_materia()
        elif opcion == "4":
            registrar_grupo()
        elif opcion == "5":
            registrar_horario()
        elif opcion == "6":
            registrar_carrera()
        elif opcion == "7":
            registrar_semestre() #No es que el ID de la carrera y del semestre sean el mismo, sino que utilizamos el ID de la carrera para asociar semestres y grupos a una carrera específica. 
        elif opcion == "8":
            escuela.listar_estudiantes()
        elif opcion == "9":
            escuela.mostrar_maestros()
        elif opcion == "10":
            escuela.mostrar_materias()
        elif opcion == "11":
            escuela.listar_grupos()  # Mostrar grupos
        elif opcion == "12":
            escuela.listar_carreras()
        elif opcion == "13":
            escuela.listar_semestres()
        elif opcion == "14":
            numero_control = input("Ingresa el número de control del estudiante: ")
            escuela.eliminar_estudiante(numero_control=numero_control)
        elif opcion == "15":
            numero_control = input("Ingresa el número de control del maestro: ")
            escuela.eliminar_maestro(numero_control=numero_control)
        elif opcion == "16":
            numero_control = input("Ingresa el número de control de la materia: ")
            escuela.eliminar_materia(numero_control=numero_control)
        elif opcion == "17":
            print("¡Hasta Luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()