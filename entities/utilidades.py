from datetime import datetime
import re

string_regex = '^[a-zA-Z\s\xE1\xE9\xED\xF3\xFA\xC1\xC9\xCD\xD3\xDA]{3,}$'

def existe_verifica_objeto(objeto, lista_obj):
    for i in range(len(lista_obj)):
        if lista_obj[i].nombre.upper() == objeto.upper():
            return i
    return -1


def string_valido(self):
    return re.search(string_regex, self)



def pedir_especialidad(especialidades):
    especialidad = None
    while True:
        try:
            especialidad = input("    - Ingrese el nombre de la especialidad: ")
            encontrado = False
            if string_valido(especialidad):
                encontrado = existe_verifica_objeto(especialidad, especialidades)
                if encontrado != -1:
                      print("\n[ (!) ERROR ] --> La especialidad ya existe, ingreselo nuevamente.\n")
                else: break
            else: raise ValueError

        except ValueError:
            print("\n[ (!) ERROR ] --> El nombre de la especialidad es incorrecto, ingréselo nuevamente.\n")

    return especialidad




def pedir_identidad(tipo):
    identidad = None
    while True:
        try:
            identidad = input(f"    - Ingrese el {tipo}: ")
            if string_valido(identidad): break
            else: raise ValueError
        except ValueError:
            print(f"\n[ (!) ERROR ] --> No es un {tipo} válido, ingréselo de nuevo.\n")

    return identidad




def pedir_cedula():
    cedula = None
    while True:
        try:
            cedula = int(input("    - Ingrese la cédula de identidad: "))
            if len(str(cedula)) == 8: break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.\n")
    
    return cedula




def pedir_fecha(tipo):
    fecha = None
    while True:
        try:
            fecha = input(f"    - Ingrese la fecha de {tipo} en formato aaaa-mm-dd: ")
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            break
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.\n")
    
    return fecha




def pedir_celular():
    celular = None
    while True:
        try:
            celular = input("    - Ingrese el número de celular: ")
            if not celular.isnumeric(): raise ValueError

            if celular[0] == '0' and celular[1] == '9' and len(celular[2:]) == 7: break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.\n")
    
    return celular 

def consultar_especialidad(policlinica):
    especialidad_obj= None
    while True:
        try:
            especialidad = input("    - Ingrese la especialidad: ")
            if string_valido(especialidad):
                especialidad_pos = existe_verifica_objeto(especialidad, policlinica.especialidades) 
                if especialidad_pos == -1:
                    print("\n    Esta especialidad no está dada de alta elija una opción:\n")
                    print("        1. Volver a ingresar la especialidad.")
                    print("        2. Dar de alta esta especialidad.\n")

                    while True:
                        try:
                            opcion = int(input("    --> Opción: "))
                            if  1 <= opcion <= 2: break
                            else: raise ValueError
                        except ValueError:
                            print("\n[ (!) ERROR ] --> La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")

                    if opcion == 2: policlinica.dar_alta_especialidad()
                    else: pass
                else:
                    especialidad_obj = policlinica.especialidades[especialidad_pos]
                    break

            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] -->  La especialidad debe ser un string.\n")
    
    return especialidad_obj


def consultar_medico(policlinica, especialidad_dada):
    medico_obj= None
    while True:
        try:
            medico = input("    - Ingrese el medico: ")
            if string_valido(medico):
                medico_pos = existe_verifica_objeto(medico, policlinica.medicos) 
                if medico_pos == -1:
                    print("\n    El medico no está dado de alta elija una opción:\n")
                    print("        1. Volver a ingresar el medico.")
                    print("        2. Dar de alta esta medico.\n")

                    while True:
                        try:
                            opcion = int(input("    --> Opción: "))
                            if  1 <= opcion <= 2: break
                            else: raise ValueError
                        except ValueError:
                            print("\n[ (!) ERROR ] --> La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")

                    if opcion == 2: policlinica.dar_alta_medico()
                    else: pass
                else:
                    medico_obj = policlinica.medicos[medico_pos]
                    if medico_obj.especialidad.nombre.upper() == especialidad_dada.nombre.upper():
                        break
                    else:
                        print("\n[ (!) ERROR ] --> La oespecialidad del medico no coincide con la especialidad consulta.\n")
                        pass

            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] -->  El medico debe ser un string.\n")
    
    return medico_obj
    