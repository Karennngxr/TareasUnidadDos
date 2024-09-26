from datetime import time

class Horario:
    def __init__(self, dia: str, hora_inicio: str, hora_fin: str):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def __str__(self):
        return f"{self.dia}: {self.hora_inicio} - {self.hora_fin}"


























#class Horario:
#    def __init__(self, dia: str, hora_inicio: time, hora_fin: time):
#        self.dia = dia
#        self.hora_inicio = hora_inicio
#        self.hora_fin = hora_fin
#
#    def __str__(self):
#        return f"{self.dia}: {self.hora_inicio} - {self.hora_fin}"