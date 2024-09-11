from coche import Coche

coche1 = Coche("Toyota", "Corolla", 2015)
coche2 = Coche("Ford", "Mustang", 2018)
coche3 = Coche("Honda", "Civic", 2020)

print("Detalles del coche 1:")
coche1.mostrar_informacion()
print()

print("Detalles del coche 2:")
coche2.mostrar_informacion()
print()

print("Detalles del coche 3:")
coche3.mostrar_informacion()
print()

año_actual = 2024
print(f"Edad del coche 1: {coche1.calcular_edad_del_coche(año_actual)} años")
print(f"Edad del coche 2: {coche2.calcular_edad_del_coche(año_actual)} años")
print(f"Edad del coche 3: {coche3.calcular_edad_del_coche(año_actual)} años")
