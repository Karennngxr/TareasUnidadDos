import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Crear 3 círculos con radios diferentes
circulo1 = Circulo(5)  # Radio de 5
circulo2 = Circulo(10) # Radio de 10
circulo3 = Circulo(15) # Radio de 15

# Mostrar el área y perímetro de cada círculo
print(f"Círculo 1 (Radio 5) - Área: {circulo1.calcular_area():.2f}, Perímetro: {circulo1.calcular_perimetro():.2f}")
print(f"Círculo 2 (Radio 10) - Área: {circulo2.calcular_area():.2f}, Perímetro: {circulo2.calcular_perimetro():.2f}")
print(f"Círculo 3 (Radio 15) - Área: {circulo3.calcular_area():.2f}, Perímetro: {circulo3.calcular_perimetro():.2f}")
