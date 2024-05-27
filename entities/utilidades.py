from datetime import datetime

def verificar_existe_especialidad(especialidad, especialidades):
    for i in range(len(especialidades)):
        if especialidades[i].nombre.upper() == especialidad.upper():
            return i
    return -1




def pedir_especialidad(especialidades):
    especialidad = None
    while True:
        try:
            especialidad = input("    - Ingrese el nombre de la especialidad: ")
            encontrado = False
            if especialidad.isalpha():
                encontrado = verificar_existe_especialidad(especialidad, especialidades)
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
            if identidad.isalpha(): break
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
            if especialidad.isalpha():
                especialidad_pos = verificar_existe_especialidad(especialidad, policlinica.especialidades) 
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
    