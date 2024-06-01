from datetime import datetime
from .especialidad import Especialidad
from .socio import Socio
from .medico import Medico
from .consulta import Consulta
from .utilidades import *
from .excepciones import *

class Policlinica:
  def __init__(self):
    self.__especialidades = []
    self.__socios = []
    self.__medicos = []
    self.__consultas = []
  
  @property
  def especialidades(self):
    return self.__especialidades
  
  @property
  def socios(self):
    return self.__socios

  @property
  def medicos(self):
    return self.__medicos
  
  @property
  def consultas(self):
    return self.__consultas




  def dar_alta_especialidad(self):
    print()

    nombre = pedir_especialidad(self.__especialidades)
    precio = None
    
    while True:
        try:
            precio = int(input("    - Ingrese el precio asociado: $"))
            break
        except ValueError:
            print("\n[ (!) ERROR ] --> El precio de la especialidad es incorrecto, ingréselo nuevamente.\n")

    especialidad = Especialidad(nombre, precio)
    self.__especialidades.append(especialidad)
    print("\n[ (✓) ] --> La especialidad se ha creado con éxito.\n")

    print(especialidad)




  def dar_alta_socio(self):
    print()

    nombre = pedir_identidad('nombre')
    apellido = pedir_identidad('apellido')
    cedula = pedir_cedula(self)
    fecha_nacimiento = pedir_fecha("nacimiento")
    fecha_ingreso = pedir_fecha("ingreso")
    celular = pedir_celular()
    bonificado = None

    while True:
        try:
            tipo_socio = int(input("    - Ingrese el tipo de socio: 1 - Bonificado, 2 - No bonificado: "))
            if tipo_socio != 1 and tipo_socio != 2: raise OutOfRange
            bonificado = bool(tipo_socio - 1)
            break
        except (ValueError, OutOfRange):
            print("\n[ (!) ERROR ] --> El valor ingresado no es correcto, elige la opción 1 o 2.\n")

    socio = Socio(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, bonificado, 0)
    self.__socios.append(socio)
    print("\n[ (✓) ] --> El socio ha sido ingresado con éxito.\n")

    print(socio)




  def dar_alta_medico(self):
    print()
    
    nombre = pedir_identidad('nombre')
    apellido = pedir_identidad('apellido')
    cedula = pedir_cedula(self)
    fecha_nacimiento = pedir_fecha('nacimiento')
    fecha_ingreso = pedir_fecha('ingreso')
    celular = pedir_celular()
    especialidad = consultar_especialidad(self) 

    medico = Medico(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, especialidad)
    self.__medicos.append(medico)
    print("\n[ (✓) ] --> El médico ha sido ingresado con éxito.\n")

    print(medico)




  def dar_alta_consulta(self):
    print()

    pacientes = None
    especialidad = consultar_especialidad(self)
    medico = consultar_medico(self, especialidad)
    fecha_consulta= pedir_fecha("consulta")

    while True:
        try:
            pacientes = int(input("    - Ingrese la cantidad de pacientes que se atenderán: "))
            if pacientes <= 0: raise OutOfRange
            break
        except (ValueError, OutOfRange):
            print("\n[ (!) ERROR ] --> La cantidad de pacientes no es válida, ingrésela nuevamente.\n")
    
    lista_turnos = [ (i + 1) for i in range(pacientes) ]

    consulta = Consulta(especialidad, medico, fecha_consulta, lista_turnos)      
    self.__consultas.append(consulta)
    print("\n[ (✓) ] --> La consulta ha sido ingresado con éxito.\n")

    print(consulta)





  def emitir_ticket(self):
    print()

    encontrados=[]
    especialidad = consultar_especialidad(self)

    print()
    if len(self.__consultas) > 0:
      for i in range(len(self.__consultas)):
        if self.__consultas[i].especialidad.nombre.upper() == especialidad.nombre.upper():
          encontrados.append(i)
          print(f"        {len(encontrados)} - {self.__consultas[i]}")
    
    if len(encontrados) == 0: print("[ (!) ERROR ] --> No hay consultas para esta especialidad.")
    else:
      print()
      opcion = None
      
      while True:
        try:
          opcion = int(input("    --> Opción: "))
          if  opcion < 0 or opcion > len(encontrados): raise OutOfRange
          break
        except (ValueError, OutOfRange):
          print("\n[ (!) ERROR ] --> La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")
    
      print(f"Lista de numeros disponibles: {self.__consultas[encontrados[opcion - 1]].lugar_dispo}")
      
      cedula = None
      while True:
          try:
              cedula = int(input("    - Ingrese la cédula de identidad del socio: "))
              if len(str(cedula)) != 8: raise ValueError
              break
          except ValueError:
              print("\n[ (!) ERROR ] --> No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.\n")
      # for i in range(len(self.__socios.cedula)):
      #     if self.__socios.cedula == cedula:
      #         return i
      # return -1
    


  def realizar_consulta(self):
    opcion = None

    print("\nSeleccione una opción:\n")
    print("     1. Obtener todos los médicos asociados a una especialidad específica.")
    print("     2. Obtener el precio de una consulta de una especialidad en específico.")
    print("     3. Listar todos los socios con sus deudas asociadas en orden ascendente.")
    print("     4. Realizar consultas respecto a cantidad de consultas entre dos fechas.")
    print("     5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.\n")
    
    while True:
        try:
            opcion = int(input("--> Opción: "))
            if  opcion < 1 or opcion > 5: raise OutOfRange
            break
        except (ValueError, OutOfRange):
            print("\n[ (!) ERROR ] --> La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")

    match opcion:
        case 1:
            especialidad = consultar_especialidad(self)
            encontrado = False
            if len(self.__medicos) > 0:
              for i in range(len(self.__medicos)):
                  if self.__medicos[i].especialidad.nombre == especialidad.nombre:
                      encontrado = True
                      print(f"[{i+1}] {self.__medicos[i]}")
                    
            if not encontrado: print("\n[ (!) ERROR ] --> No hay medicos para esta especialidad.\n")

        
        case 2: pass
        case 3: pass
        case 4: pass
        case 5: pass
        case _: print("[ (!) ERROR ] --> Un error inesperado ha ocurrido.")