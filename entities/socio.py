from .persona import Persona

class Socio(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular, tipo, deuda):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular)
        self.__tipo = tipo
        self.__deuda = int(deuda)
        
    def __str__(self):
        return super().__str__() +f'\nBonificado: {self.__tipo}\nDeuda: ${self.__deuda}'

    @property
    def tipo(self):
        return self.__tipo

    @property
    def deuda(self):
        return self.__deuda
    
    def subir_deuda(self, valor):
        self.__deuda += valor
