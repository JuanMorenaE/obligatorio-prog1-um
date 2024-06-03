class Consulta:
    def __init__(self, especialidad, medico, fecha, lugar_dispo):
        self.__especialidad= especialidad
        self.__medico= medico
        self.__fecha= fecha
        self.__lugar_dispo= lugar_dispo
    
    def __str__(self):
        return f'Doctor: {self.__medico.nombre} {self.__medico.apellido}. Dia de la consulta: {self.__fecha.strftime("%Y-%m-%d")}.'

    @property
    def especialidad(self):
        return self.__especialidad
    
    @property
    def medico(self):
        return self.__medico
    
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def lugar_dispo(self):
        return self.__lugar_dispo
    
    def getLugaresDispoString(self):
        lugares = ''
        for i, turno in enumerate(self.lugar_dispo):
            lugares += str(turno)
            if (i + 1) < len(self.lugar_dispo) - 1: lugares += ', '
            if len(self.lugar_dispo) > 1 and i + 1 == len(self.lugar_dispo) - 1: lugares += ' y '
        return lugares