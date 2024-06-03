class Especialidad:
    def __init__(self, nombre, precio):
        self.__nombre= nombre
        self.__precio= precio

    def __str__(self):
        return f'{self.__nombre}: ${self.__precio} por consulta.'
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    