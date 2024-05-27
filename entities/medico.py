from .persona import Persona

class Medico(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular, especialidad):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular)
        self.__especialidad= especialidad

    def __str__(self):
        return super().__str__() +f'\nEspecialidad:{self.__especialidad}'

    @property
    def especialidad(self):
        return self.__especialidad
    
    