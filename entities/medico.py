from .persona import Persona

class Medico(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular, especialidad):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular)
        self.__especialidad= especialidad

    # def __str__(self):
    #     return f'\nNombre: {self.__nombre}\nApellido: {self.__apellido}\nCI: {self.__cedula}\nFecha de Nacimiento: {self.__fecha_nacimiento}\nFecha de Ingreso: {self.__fecha_ingreso}\nCelular: {self.__nro_celular}\n{self.__especialidad}\n'

    @property
    def especialidad(self):
        return self.__especialidad
    
    