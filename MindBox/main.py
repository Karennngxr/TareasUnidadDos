from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from datetime import datetime

escuela = Escuela()

while True:
    print("** MINDBOX **")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Salir")
    
    opcion = input("Ingresa una opción para continuar: ")
    
    if opcion == "1":
        print("\nSeleccionaste la opción para registrar un estudiante")
        
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        curp = input("Ingrese la CURP del estudiante: ")
        ano = int(input("Ingrese el año de nacimiento del estudiante: "))
        mes = int(input("Ingrese el mes de nacimiento del estudiante: "))
        dia = int(input("Ingrese el día de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        
        estudiante = Estudiante(nombre, apellido, curp, fecha_nacimiento)
        estudiante.numero_control = escuela.generar_numero_control_estudiante()
        escuela.registrar_estudiante(estudiante)
        
        print(f"Estudiante registrado con número de control: {estudiante.numero_control}")
    
    elif opcion == "2":
        print("\nSeleccionaste la opción para registrar un maestro")
        
        nombre = input("Ingrese el nombre del maestro: ")
        apellido = input("Ingrese el apellido del maestro: ")
        curp = input("Ingrese la CURP del maestro: ")
        ano = int(input("Ingrese el año de nacimiento del maestro: "))
        mes = int(input("Ingrese el mes de nacimiento del maestro: "))
        dia = int(input("Ingrese el día de nacimiento del maestro: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        salario = float(input("Ingrese el salario del maestro: "))
        
        maestro = Maestro(nombre, apellido, curp, fecha_nacimiento, salario)
        maestro.numero_control = escuela.generar_numero_control_maestro(maestro)
        escuela.registrar_maestro(maestro)
        
        print(f"Maestro registrado con número de control: {maestro.numero_control}")
    
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        print("¡Hasta luego!")
        break
