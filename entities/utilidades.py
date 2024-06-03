from datetime import datetime
import re

string_regex = '^[a-zA-Z\s\xE1\xE9\xED\xF3\xFA\xC1\xC9\xCD\xD3\xDA]{3,}$'

def existe_verifica_objeto(objeto, lista_obj):
    for i, obj in enumerate(lista_obj):
        if obj.nombre.upper() == objeto.upper():
            return i
    return -1


def string_valido(self):
    return re.search(string_regex, self)



def pedir_especialidad(especialidades):    
    while True:
        try:
            especialidad = input("    - Ingrese el nombre de la especialidad: ")
            encontrado = False
            if string_valido(especialidad):
                encontrado = existe_verifica_objeto(especialidad, especialidades)
                if encontrado == -1: return especialidad
                print("\n[ (!) ERROR ] --> La especialidad ya existe, ingreselo nuevamente.\n")
            else: raise ValueError

        except ValueError:
            print("\n[ (!) ERROR ] --> El nombre de la especialidad es incorrecto, ingréselo nuevamente.\n")




def pedir_identidad(tipo):
    while True:
        try:
            identidad = input(f"    - Ingrese el {tipo}: ")
            if not string_valido(identidad): raise ValueError
            return identidad
        except ValueError:
            print(f"\n[ (!) ERROR ] --> No es un {tipo} válido, ingréselo de nuevo.\n")




def pedir_cedula(policlinica):
    while True:
        try:
            cedula = int(input("    - Ingrese la cédula de identidad: "))
            if len(str(cedula)) == 8:
                encontrado = None
                for socio in policlinica.socios:
                    if(socio.cedula == cedula):
                        encontrado = True
                        break
                    
                if not encontrado:
                    for medico in policlinica.medicos:
                        if(medico.cedula == cedula):
                            encontrado = True
                            break    
                    return cedula
                
                else: print("\n[ (!) ERROR ] --> Esta cedula ya pertenece a un usuario registrado.\n")
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.\n")




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
            if not celular.isnumeric(): raise ValueError

            if celular[0] != '0' or celular[1] != '9' or len(celular[2:]) != 7: raise ValueError
            return celular
        except ValueError:
            print("\n[ (!) ERROR ] --> No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.\n")




def consultar_especialidad(policlinica):
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
                    return especialidad_obj

            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] -->  La especialidad debe ser un string.\n")
    
    


def consultar_medico(policlinica, especialidad_dada):
    while True:
        try:
            nombre_medico = input("    - Ingrese el medico: ")
            if not string_valido(nombre_medico): raise ValueError

            medico_pos = -1

            for i, medico in enumerate(policlinica.medicos):
                if medico.nombre.upper() + ' ' + medico.apellido.upper() == nombre_medico.upper():
                    medico_pos = i
                    break
        
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
                    return medico_obj
                else:
                    print("\n[ (!) ERROR ] --> La oespecialidad del medico no coincide con la especialidad consulta.\n")

        except ValueError:
            print("\n[ (!) ERROR ] -->  El medico debe ser un string.\n")
    
    
def consultar_pos_socio(policlinica):
    while True:
        try:
            cedula = int(input("    - Ingrese la cedula del socio: "))
            if len(str(cedula)) == 8 :
                socio_pos=-1
                for i, socio in enumerate(policlinica.socios):
                    if socio.cedula == cedula:
                        socio_pos=i
                if socio_pos == -1:
                    print("\n    Este socio no esta dado de alta:\n")
                    print("        1. Volver a ingresar el socio.")
                    print("        2. Dar de alta este socio.\n")

                    while True:
                        try:
                            opcion = int(input("    --> Opción: "))
                            if  1 <= opcion <= 2: break
                            else: raise ValueError
                        except ValueError:
                            print("\n[ (!) ERROR ] --> La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")

                    if opcion == 2: policlinica.dar_alta_socio()
                    else: pass
                else:
                    return socio_pos

            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] -->  : No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.\n")
            
     


def imprimir_medicos(policlinica):
    for medico in policlinica.medicos:
        print(medico)