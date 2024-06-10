import re
from datetime import datetime

from entities.socio import Socio
from entities.medico import Medico

from exceptions.CedulaExistente import CedulaExistente
from exceptions.EspecialidadExistente import EspecialidadExistente

# from exceptions.FechaInvalida import FechaInvalida
from exceptions.FueraDeRango import FueraDeRango
from exceptions.MedicoInvalido import MedicoInvalido
from exceptions.NumeroInvalido import NumeroInvalido
from exceptions.ValorInvalido import ValorInvalido


string_regex = '^[a-zA-Z\s\xE1\xE9\xED\xF3\xFA\xC1\xC9\xCD\xD3\xDA]{3,}$'

def obtener_especialidad(policlinica, nombre):
    for especialidad in policlinica.especialidades:
        if especialidad.nombre.upper() == nombre.upper():
            return especialidad
    return None




def obtener_persona(policlinica, cedula):
    for socio in policlinica.socios:
        if socio.cedula == cedula:
            return socio
    
    for medico in policlinica.medicos:
        if medico.cedula == cedula:
            return medico
    return None




def obtener_medico(policlinica, nombre):
    for medico in policlinica.medicos:
        if f"{medico.nombre.upper()} {medico.apellido.upper()}" == nombre.upper():
            return medico
    return None




def string_valido(self):
    return re.search(string_regex, self)




def pedir_especialidad(policlinica):    
    while True:
        try:
            especialidad = input("    - Ingrese el nombre de la especialidad: ")
            if not string_valido(especialidad): raise ValorInvalido

            encontrado = obtener_especialidad(policlinica, especialidad)
            if encontrado is not None: raise EspecialidadExistente

            return especialidad
        except ValorInvalido:
            print("\n[ (!) ERROR ] --> El nombre de la especialidad es incorrecto, ingréselo nuevamente.\n")
        except EspecialidadExistente:
            print("\n[ (!) ERROR ] --> La especialidad ya existe, ingreselo nuevamente.\n")




def pedir_identidad(tipo):
    while True:
        try:
            identidad = input(f"    - Ingrese el {tipo}: ")
            if not string_valido(identidad): raise ValorInvalido

            return identidad
        except ValorInvalido:
            print(f"\n[ (!) ERROR ] --> No es un {tipo} válido, ingréselo de nuevo.\n")




def pedir_cedula(policlinica):
    while True:
        try:
            cedula = input("    - Ingrese la cédula de identidad: ")
            if not cedula.isnumeric(): raise NumeroInvalido
            if len(cedula) != 8: raise ValorInvalido
            cedula = int(cedula)
            
            if obtener_persona(policlinica, cedula) is not None:
                raise CedulaExistente                
                
            return cedula
        except (NumeroInvalido, ValorInvalido):
            print("\n[ (!) ERROR ] --> No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.\n")
        except CedulaExistente:
            print("\n[ (!) ERROR ] --> Esta cedula ya pertenece a un usuario registrado.\n")




def pedir_fecha(tipo):
    while True:
        try:
            fecha = input(f"    - Ingrese la fecha de {tipo} en formato aaaa-mm-dd: ")
            fecha = datetime.strptime(fecha, "%Y-%m-%d")

            return fecha
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.\n")




def pedir_celular():
    while True:
        try:
            celular = input("    - Ingrese el número de celular: ")
            if not celular.isnumeric(): raise NumeroInvalido
            if celular[0] != '0' or celular[1] != '9' or len(celular[2:]) != 7: raise ValorInvalido
            celular = int(celular)

            return celular
        except ValorInvalido:
            print("\n[ (!) ERROR ] --> No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.\n")




def consultar_especialidad(policlinica):
    while True:
        try:
            especialidad = input("    - Ingrese la especialidad: ")
            if not string_valido(especialidad): raise ValorInvalido

            especialidad_obj = obtener_especialidad(policlinica, especialidad)

            if especialidad_obj is not None: return especialidad_obj
            
            print("\n    Esta especialidad no está dada de alta elija una opción:\n")
            print("        1. Volver a ingresar la especialidad.")
            print("        2. Dar de alta esta especialidad.\n")

            opcion = obtener_opcion((1,2))
            if opcion == 2: policlinica.dar_alta_especialidad()
                
        except ValorInvalido:
            print("\n[ (!) ERROR ] -->  La especialidad debe ser un string.\n")

    


def consultar_medico(policlinica, especialidad_dada):
    while True:
        try:
            nombre_medico = input("    - Ingrese el medico: ")
            if not string_valido(nombre_medico): raise ValorInvalido

            medico = obtener_medico(policlinica, nombre_medico)
    
            if medico is not None:
                if medico.especialidad.nombre.upper() != especialidad_dada.nombre.upper():
                    raise MedicoInvalido
                return medico
        
            print("\n    El medico no está dado de alta elija una opción:\n")
            print("        1. Volver a ingresar el medico.")
            print("        2. Dar de alta esta medico.\n")

            opcion = obtener_opcion((1,2))
            if opcion == 2: policlinica.dar_alta_medico()

        except MedicoInvalido:
            print("\n[ (!) ERROR ] --> La especialidad del medico no coincide con la especialidad consultada.\n")
        except ValorInvalido:
            print("\n[ (!) ERROR ] -->  El medico debe ser un string.\n")




def consultar_socio(policlinica):
    while True:
        try:
            cedula = input("    - Ingrese la cedula del socio: ")
            if not cedula.isnumeric(): raise NumeroInvalido
            if len(cedula) != 8 : raise ValorInvalido
            cedula = int(cedula)

            persona = obtener_persona(policlinica, cedula)
            
            if persona is not None and isinstance(persona, Socio): return persona

            print("\n    Este socio no esta dado de alta:\n")
            print("        1. Volver a ingresar el socio.")
            print("        2. Dar de alta este socio.\n")

            opcion = obtener_opcion((1,2))
            if opcion == 2: policlinica.dar_alta_socio()

        except (NumeroInvalido, ValorInvalido):
            print("\n[ (!) ERROR ] -->  : No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.\n")
       
     


def obtener_opcion(opciones_validas):
    while True:
        try:
            opcion = input("    --> Opción: ")
            if not opcion.isnumeric(): raise NumeroInvalido

            opcion = int(opcion)
            if opcion not in opciones_validas: raise FueraDeRango

            return opcion
        except (NumeroInvalido, FueraDeRango):
            print("\n[ (!) ERROR ] --> La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")