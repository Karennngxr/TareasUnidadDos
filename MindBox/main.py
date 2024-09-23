from typing import List
from random import randint
from datetime import datetime

from estudiantes.estudiante import Estudiante
from escuela.escuela import Escuela
from maestros.maestro import Maestro
from materias.materia import Materia
from grupos.grupo import Grupo
from horarios.horario import Horario

escuela = Escuela()

def registrar_estudiante():
    print("---- REGISTRAR NUEVO ESTUDIANTE ----")
    nombre = input("Introduce el nombre del estudiante: ")
    apellido = input("Introduce el apellido del estudiante: ")
    curp = input("Introduce la CURP del estudiante: ")
    dia = int(input("Introduce el día de nacimiento del estudiante (DD): "))
    mes = int(input("Introduce el mes de nacimiento del estudiante (MM): "))
    anio = int(input("Introduce el año de nacimiento del estudiante (YYYY): "))

    #objeto estudiante
    fecha_nacimiento = datetime(anio, mes, dia)
    estudiante = Estudiante(nombre, apellido, curp, fecha_nacimiento)

    # Generar n control
    estudiante.numero_control = escuela.numero_control_est()

    # Registramos al estudiante en la escuela
    escuela.registrar_estudiante(estudiante)

    print(f"Estudiante registrado: {estudiante.nombre} {estudiante.apellido} {estudiante.curp}{estudiante.fecha_nacimiento}")
    print(f"Número de control: {estudiante.numero_control}")

def registrar_maestro():
    print("---- REGISTRAR NUEVO MAESTRO ----")
    nombre = input("Introduce el nombre del maestro: ")
    apellido = input("Introduce el apellido del maestro: ")
    curp = input("Introduce la CURP del maestro: ")
    dia = int(input("Introduce el día de nacimiento del maestro (DD): "))
    mes = int(input("Introduce el mes de nacimiento del maestro (MM): "))
    anio = int(input("Introduce el año de nacimiento del maestro (YYYY): "))

    # Objeto maestro
    fecha_nacimiento = datetime(anio, mes, dia)
    maestro = Maestro(nombre, apellido, curp, fecha_nacimiento)

    maestro.numero_control = escuela.numero_control_maest()

    # Registrar maestro
    escuela.registrar_maestros(maestro)

    print(f"Maestro registrado: {maestro.nombre} {maestro.apellido} {maestro.curp}{maestro.fecha_nacimiento}")
    print(f"Número de control: {maestro.numero_control}")

def registrar_materia():

    print("---- REGISTRAR NUEVA MATERIA ----")
    nombre = input("Introduce el nombre de la materia: ")
    descripcion = input("Introduce la descripción de la materia: ")
    semestre = int(input("Introduce el semestre de la materia: "))
    creditos = int(input("Introduce la cantidad de créditos: "))

    nueva_materia = Materia(nombre, descripcion, semestre, creditos)
    nueva_materia.numero_control = escuela.numero_control_materias()    
    escuela.agregar_materia(nueva_materia)

    print(f"Materia registrada: {nueva_materia}")
    print(f"Numero de control y codificacion: {nueva_materia.numero_control}")


def registrar_grupo():
    print("---- REGISTRAR NUEVO GRUPO ----")
    id_grupo = int(input("ID del grupo: "))
    tipo_grupo = input("Tipo de grupo (A/B/C): ")

    # Creamos el objeto grupo
    grupo = Grupo(id_grupo, tipo_grupo)
    print(f"Grupo registrado: {grupo.id} - {grupo.tipo}")

def registrar_horario():
    print("---- REGISTRAR NUEVO HORARIO ----")
    dia = input("Día de la semana: ")
    hora_inicio = input("Hora de inicio (HH:MM): ")
    hora_fin = input("Hora de fin (HH:MM): ")

    # Creamos el objeto horario
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
        print("6. Salir")
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
            print("¡Hasta Luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar menu
if __name__ == "__main__":
    menu()
