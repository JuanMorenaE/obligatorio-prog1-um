from .persona import Persona

class Socio(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular, bonificado):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular)
        self.__bonificado = bonificado
        self.__deuda = 0
        
    def __str__(self):
        return super().__str__() +f'\nBonificado: {self.__bonificado}\nDeuda: ${self.__deuda}'

    @property
    def bonificado(self):
        return self.__bonificado

    @property
    def deuda(self):
        return self.__deuda
    
    @deuda.setter
    def deuda(self, nueva_deuda):
        self.__deuda = nueva_deuda

    def subir_deuda(self, valor):
        self.deuda += valor
