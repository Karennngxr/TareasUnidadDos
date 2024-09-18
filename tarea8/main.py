from hospital import Hospital
from paciente import Paciente
from medico import Medico # type: ignore

def mostrar_menu():
    print("\n--- Sistema de Hospital ---")
    print("1. Agregar Paciente")
    print("2. Eliminar Paciente")
    print("3. Mostrar Pacientes Menores de Edad")
    print("4. Mostrar Pacientes Mayores de Edad")
    print("5. Agregar Médico")
    print("6. Eliminar Médico")
    print("7. Salir")

def main():
    hospital = Hospital()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_paciente = input("Ingrese ID del paciente: ")
            nombre = input("Ingrese nombre del paciente: ")
            edad = int(input("Ingrese edad del paciente: "))
            paciente = Paciente(id_paciente, nombre, edad)
            hospital.agregar_paciente(paciente)
            print("Paciente agregado.")
        
        elif opcion == '2':
            id_paciente = input("Ingrese ID del paciente a eliminar: ")
            hospital.eliminar_paciente(id_paciente)
            print("Paciente eliminado.")

        elif opcion == '3':
            print("Pacientes menores de edad:")
            menores = hospital.mostrar_pacientes_menores()
            for p in menores:
                print(p)

        elif opcion == '4':
            print("Pacientes mayores de edad:")
            mayores = hospital.mostrar_pacientes_mayores()
            for p in mayores:
                print(p)

        elif opcion == '5':
            id_medico = input("Ingrese ID del médico: ")
            nombre = input("Ingrese nombre del médico: ")
            especialidad = input("Ingrese especialidad del médico: ")
            medico = Medico(id_medico, nombre, especialidad)
            hospital.agregar_medico(medico)
            print("Médico agregado.")

        elif opcion == '6':
            id_medico = input("Ingrese ID del médico a eliminar: ")
            hospital.eliminar_medico(id_medico)
            print("Médico eliminado.")

        elif opcion == '7':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
