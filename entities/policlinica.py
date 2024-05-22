from medico import Medico

class Policlinica:
  def __init__(self):
    self.__medicos = []
    self.__socios = []
    self.__especialidades = []
    self.__consultas = []

  @property
  def medicos(self):
    return self.__medicos
  
  @property
  def socios(self):
    return self.__socios
  
  @property
  def especialidades(self):
    return self.__especialidades
  
  @property
  def consultas(self):
    return self.__consultas

  def dar_alta_medico(self):
    nombre= None
    apellido= None
    cedula= None
    fecha_nacimiento= None
    fecha_ingreso= None
    nro_celular= None
    especialidad= None
    
    nombre= input("1. Ingrese el nombre: ")

  
    medico = Medico(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular, especialidad)
    self.__medicos.append(medico)

  def dar_alta_consulta(self):
    pass

  def emitir_ticket(self):
    pass

  def realizar_consulta(self):
    pass