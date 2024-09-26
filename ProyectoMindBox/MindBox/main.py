from datetime import datetime

from maestros.maestro import Maestro
from materias.materia import Materia
from grupos.grupo import Grupo
from horarios.horario import Horario

from estudiantes.estudiante import Estudiante
from escuela.escuela import Escuela

escuela = Escuela()

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
    id_grupo = int(input("ID del grupo: "))
    tipo_grupo = input("Tipo de grupo (A/B/C): ")

    # Creamos el objeto grupo
    grupo = Grupo(id_grupo, tipo_grupo)
    
    # Registramos el grupo en la escuela
    escuela.registrar_grupo(grupo)
    print(f"Grupo registrado: {grupo.id} - {grupo.tipo}")


def registrar_horario():
    print("---- REGISTRAR NUEVO HORARIO ----")
    dia = input("Día de la semana: ")
    hora_inicio = input("Hora de inicio (HH:MM): ")
    hora_fin = input("Hora de fin (HH:MM): ")

    horario = Horario(dia, hora_inicio, hora_fin)
    print(f"Horario registrado: {horario.dia}: {horario.hora_inicio} - {horario.hora_fin}")

def menu():
    while True:
        print("\n------------ BIENVENIDO A MINDBOX ---------------")
        print("1. Registrar Estudiante")
        print("2. Registrar Maestro")
        print("3. Registrar Materia")
        print("4. Registrar Grupo")
        print("5. Registrar Horario")
        print("6. Mostrar estudiantes")
        print("7. Mostrar maestros")  
        print("8. Mostrar materias") 
        print("9. Mostrar grupos") 
        print("10. Eliminar Estudiante")
        print("11. Eliminar Maestro")
        print("12. Eliminar Materia")
        print("13. Salir")
        
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
            escuela.listar_estudiantes()
        elif opcion == "7":
            escuela.mostrar_maestros()  
        elif opcion == "8":
            escuela.mostrar_materias()  
        elif opcion == "9":
            escuela.listar_grupos()  # Mostrar grupos
        elif opcion == "10":
            numero_control = input("Ingresa el número de control del estudiante: ")
            escuela.eliminar_estudiante(numero_control=numero_control)
        elif opcion == "11":
            numero_control = input("Ingresa el número de control del maestro: ")
            escuela.eliminar_maestro(numero_control=numero_control)  
        elif opcion == "12":
            numero_control = input("Ingresa el número de control de la materia: ")
            escuela.eliminar_materia(numero_control=numero_control)  
        elif opcion == "13":
            print("¡Hasta Luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
if __name__ == "__main__":
    menu()
