class Ticket:
    def __init__(self, consulta, socio, turno, precio_final):
        self.__consulta = consulta
        self.__socio = socio
        self.__turno = turno
        self.__precio_final = precio_final
        
    @property
    def consulta(self):
        return self.__consulta
    
    @property
    def socio(self):
        return self.__socio
    
    @property
    def turno(self):
        return self.__turno

    @property
    def precio_final(self):
        return self.__precio_final