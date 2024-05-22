class Consulta:
    def __init__(self, especialidad, medico, fecha, lugar_dispo):
        self.__especialidad= especialidad
        self.__medico= medico
        self.__fecha= fecha
        self.__lugar_dispo= lugar_dispo
    
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