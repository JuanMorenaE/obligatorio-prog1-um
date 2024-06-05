from entities.especialidad import Especialidad
from entities.socio import Socio
from entities.medico import Medico
from entities.consulta import Consulta
from entities.ticket import Ticket
from entities.utilidades import *

from exceptions.FueraDeRango import FueraDeRango
from exceptions.NumeroInvalido import NumeroInvalido
from exceptions.ValorInvalido import ValorInvalido

class Policlinica:
  def __init__(self):
    self.__especialidades = []
    self.__socios = []
    self.__medicos = []
    self.__consultas = []
    self.__tickets = []
  
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

  @property
  def tickets(self):
     return self.__tickets


  def dar_alta_especialidad(self):
    print()

    nombre = pedir_especialidad(self.especialidades)
    precio = None
    
    while True:
        try:
            precio = input("    - Ingrese el precio asociado: $")
            if not precio.isnumeric(): raise NumeroInvalido

            precio = int(precio)
            if precio <= 0: raise ValorInvalido
            break
        except (NumeroInvalido, ValorInvalido):
            print("\n[ (!) ERROR ] --> El precio de la especialidad es incorrecto, ingréselo nuevamente.\n")

    especialidad = Especialidad(nombre, precio)
    self.especialidades.append(especialidad)
    print("\n[ (✓) ] --> La especialidad se ha creado con éxito.\n")




  def dar_alta_socio(self):
    print()

    nombre = pedir_identidad('nombre')
    apellido = pedir_identidad('apellido')
    cedula = pedir_cedula(self)
    fecha_nacimiento = pedir_fecha("nacimiento")
    fecha_ingreso = pedir_fecha("ingreso")
    celular = pedir_celular()
    bonificado = None
    deuda = 0

    while True:
        try:
            tipo_socio = input("    - Ingrese el tipo de socio: 1 - Bonificado, 2 - No bonificado: ")
            if not tipo_socio.isnumeric(): raise NumeroInvalido

            tipo_socio = int(tipo_socio)
            if tipo_socio != 1 and tipo_socio != 2: raise FueraDeRango
            
            if tipo_socio == 1: bonificado = True
            else: bonificado = False
            
            break
        except (NumeroInvalido, FueraDeRango):
            print("\n[ (!) ERROR ] --> El valor ingresado no es correcto, elige la opción 1 o 2.\n")

    socio = Socio(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, bonificado, deuda)
    self.socios.append(socio)
    print("\n[ (✓) ] --> El socio ha sido ingresado con éxito.\n")




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
    self.medicos.append(medico)
    print("\n[ (✓) ] --> El médico ha sido ingresado con éxito.\n")




  def dar_alta_consulta(self):
    print()

    especialidad = consultar_especialidad(self)
    medico = consultar_medico(self, especialidad)
    fecha_consulta= pedir_fecha("consulta")
    pacientes = None

    while True:
        try:
            pacientes = input("    - Ingrese la cantidad de pacientes que se atenderán: ")
            if not pacientes.isnumeric(): raise NumeroInvalido

            pacientes = int(pacientes)
            if pacientes <= 0: raise FueraDeRango
            break
        except (NumeroInvalido, FueraDeRango):
            print("\n[ (!) ERROR ] --> La cantidad de pacientes no es válida, ingrésela nuevamente.\n")
    
    lista_turnos = [ (i + 1) for i in range(pacientes) ]

    consulta = Consulta(especialidad, medico, fecha_consulta, lista_turnos)      
    self.consultas.append(consulta)
    print("\n[ (✓) ] --> La consulta ha sido ingresado con éxito.\n")




  def emitir_ticket(self):
    print()

    encontrados = []
    especialidad = consultar_especialidad(self)

    print()
    
    if len(self.consultas) > 0:
      for i, consulta in enumerate(self.consultas):
        if consulta.especialidad.nombre.upper() == especialidad.nombre.upper() and len(consulta.lugar_dispo) > 0:
          encontrados.append(i)
          print(f"        {len(encontrados)} - {consulta}")
    
    if len(encontrados) == 0:
      print("[ (!) ERROR ] --> No hay consultas para esta especialidad.")
      return
    
    
    print()
    opciones = [i for i in range(1, len(encontrados) + 1)]
    opcion = obtener_opcion(tuple(opciones))
    
    consulta_seleccionada = self.consultas[encontrados[opcion - 1]]
  
    print(f"\n    Lista de numeros disponibles: {consulta_seleccionada.getLugaresDispoString()}\n")
    
    opcion_numeros = None
    while True:
      try:
        opcion_numeros = input("    --> Opción: ")
        if not opcion_numeros.isnumeric(): raise NumeroInvalido

        opcion_numeros = int(opcion_numeros)
        if opcion_numeros not in consulta_seleccionada.lugar_dispo: raise FueraDeRango
        break
      except (NumeroInvalido, FueraDeRango):
        print(f"\n[ (!) ERROR ] --> No es un número de consulta válido, los números válidos son: {consulta_seleccionada.getLugaresDispoString()}\n")
  
    print()

    socio = consultar_pos_socio(self)
    socio_seleccionado = self.socios[socio]
    precio = especialidad.precio
    if socio_seleccionado.bonificado: precio *= 0.8
        
    consulta_seleccionada.lugar_dispo.remove(opcion_numeros)
    socio_seleccionado.subir_deuda(precio)
    
    ticket = Ticket(consulta_seleccionada, socio_seleccionado, opcion_numeros, precio)
    self.tickets.append(ticket)
    print("\n[ (✓) ] --> El ticket ha sido creado con éxito.\n")




  def realizar_consulta(self):
    print("\nSeleccione una opción:\n")
    print("     1. Obtener todos los médicos asociados a una especialidad específica.")
    print("     2. Obtener el precio de una consulta de una especialidad en específico.")
    print("     3. Listar todos los socios con sus deudas asociadas en orden ascendente.")
    print("     4. Realizar consultas respecto a cantidad de consultas entre dos fechas.")
    print("     5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.\n")
    
    opcion = obtener_opcion((1,2,3,4,5))

    match opcion:
        case 1:
            especialidad = consultar_especialidad(self)
            encontrado = False
            if len(self.medicos) > 0:
              for i, medico in enumerate(self.medicos):
                  if medico.especialidad.nombre == especialidad.nombre:
                      encontrado = True
                      print(f"[{i+1}] {medico}")
                    
            if not encontrado: print("\n[ (!) ERROR ] --> No hay medicos para esta especialidad.\n")

        
        case 2: 
          especialidad = consultar_especialidad(self)
          print(f"El precio de consulta de {especialidad.nombre} es ${int(especialidad.precio)}")
          

        case 3:
          copiaLista = []
          listaOrdenada = []

          for socio in self.socios:
            copiaLista.append(socio)


          while len(copiaLista) > 0:
            maxDeuda = 0
            socioConMayorDeuda = None

            for socio in copiaLista:
              if socio.deuda >= maxDeuda:
                maxDeuda = socio.deuda
                socioConMayorDeuda = socio

            listaOrdenada.append(socioConMayorDeuda)
            copiaLista.remove(socioConMayorDeuda)

          print()
          for i, socio in enumerate(listaOrdenada):
             print(f"{i + 1}. Deuda: ${socio.deuda} Nombre: {socio.nombre} {socio.apellido}")
          
          
        case 4:
          fecha_inicio = pedir_fecha("inicio")
          fecha_final = pedir_fecha("final")
          consultas_det = []

          for consulta in self.consultas:
             if fecha_inicio <= consulta.fecha <= fecha_final:
                consultas_det.append(consulta)
  


          print(f"La cantidad de consultas entre {fecha_inicio.strftime('%Y-%m-%d')} y {fecha_final.strftime('%Y-%m-%d')} es: {len(consultas_det)}")
          for i, consulta in enumerate(consultas_det):
             print(f"{i + 1}. Doctor: {consulta.medico.nombre} {consulta.medico.apellido} Fecha: {consulta.fecha.strftime('%Y-%m-%d')}. {consulta.especialidad}")
        
        
        case 5: 
          fecha_inicio = pedir_fecha("inicio")
          fecha_final = pedir_fecha("final")
          ganancias = 0

          for ticket in self.tickets:
             if fecha_inicio <= ticket.consulta.fecha <= fecha_final:
                ganancias += ticket.precio_final
             
          print(f"Las ganancias entre {fecha_inicio.strftime('%Y-%m-%d')} y {fecha_final.strftime('%Y-%m-%d')} fueron: ${ganancias}.")

          
        case _: print("[ (!) ERROR ] --> Un error inesperado ha ocurrido.")