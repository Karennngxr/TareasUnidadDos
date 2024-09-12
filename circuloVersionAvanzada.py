import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class GestorDeCirculos:
    def __init__(self):
        self.circulos = []

    def agregar_circulo(self, radio):
        nuevo_circulo = Circulo(radio)
        self.circulos.append(nuevo_circulo)
        print(f"Se ha agregado un círculo con radio {radio}.")

    def mostrar_circulos(self):
        if not self.circulos:
            print("No hay círculos en el sistema.")
        else:
            print("\n--- Lista de círculos ---")
            for i, circulo in enumerate(self.circulos):
                print(f"Círculo {i + 1}:")
                print(f"  Radio: {circulo.radio}")
                print(f"  Área: {circulo.calcular_area():.2f}")
                print(f"  Perímetro: {circulo.calcular_perimetro():.2f}")

    def eliminar_circulo(self, indice):
        if 0 <= indice < len(self.circulos):
            eliminado = self.circulos.pop(indice)
            print(f"Círculo con radio {eliminado.radio} eliminado.")
        else:
            print("Índice inválido. No se pudo eliminar el círculo.")

def menu():
    gestor = GestorDeCirculos()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar círculo")
        print("2. Mostrar círculos")
        print("3. Eliminar círculo")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            radio = float(input("Ingresa el radio del círculo: "))
            gestor.agregar_circulo(radio)
        elif opcion == "2":
            gestor.mostrar_circulos()
        elif opcion == "3":
            gestor.mostrar_circulos()
            indice = int(input("Ingresa el número del círculo que deseas eliminar: ")) - 1
            gestor.eliminar_circulo(indice)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
