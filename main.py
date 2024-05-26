from datetime import datetime

def menu_principal():
    while True:
        opcion = None

        print("\nSeleccione una opción del menú:\n")
        print("     1. Dar de alta una especialidad.")
        print("     2. Dar de alta un socio.")
        print("     3. Dar de alta un médico.")
        print("     4. Dar de alta una consulta médica.")
        print("     5. Emitir un ticket de consulta.")
        print("     6. Realizar consultas.")
        print("     7. Salir del programa.\n")
        
        while True:
            try:
                opcion = int(input("--> Opción: "))
                if  1 <= opcion <= 7: break
                else: raise ValueError
            except ValueError:
                print("\n[ (!) ERROR ] --> La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")

        match opcion:
            case 1:
                menu_alta_especialidad()

            case 2:
                menu_alta_socio()

            case 3:
                menu_alta_medico()

            case 4:
                menu_alta_consulta()

            case 7:
                break


def menu_alta_especialidad():
    especialidad = None
    precio = None

    print()
    while True:
        try:
            especialidad = input("    - Ingrese el nombre de la especialidad: ")
            if especialidad.isalpha(): break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> El nombre de la especialidad es incorrecto, ingréselo nuevamente.\n")

    while True:
        try:
            precio = int(input("    - Ingrese el precio asociado: $"))
            break
        except ValueError:
            print("\n[ (!) ERROR ] --> El precio de la especialidad es incorrecto, ingréselo nuevamente.\n")

    # <-- Funcion crear especialidad aqui...
    
    print("\n[ (✓) ] --> La especialidad se ha creado con éxito.\n")



def menu_alta_socio():
    nombre = None
    apellido = None
    cedula = None
    fecha_nacimiento = None
    fecha_ingreso = None
    celular = None
    tipo_socio = None

    print()
    while True:
        try:
            nombre = input("    - Ingrese el nombre: ")
            if nombre.isalpha(): break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es un nombre válido, ingréselo de nuevo.\n")

    while True:
        try:
            apellido = input("    - Ingrese el apellido: ")
            if apellido.isalpha(): break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es un apellido válido, ingréselo de nuevo.\n")

    while True:
        try:
            cedula = int(input("    - Ingrese la cédula de identidad: "))
            if len(str(cedula)) == 8: break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.\n")

    while True:
        try:
            fecha_nacimiento = input("    - Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            break
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.\n")

    while True:
        try:
            fecha_ingreso = input("    - Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
            fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
            break
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.\n")

    while True:
        try:
            celular = input("    - Ingrese el número de celular: ")
            if not celular.isnumeric(): raise ValueError

            if celular[0] == '0' and celular[1] == '9' and len(celular[2:]) == 7: break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.\n")

    while True:
        try:
            tipo_socio = int(input("    - Ingrese el tipo de socio: 1 - Bonificado, 2 - No bonificado: "))
            if tipo_socio == 1 or tipo_socio == 2: break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> El valor ingresado no es correcto, elige la opción 1 o 2.\n")

    # <-- Funcion dar de alta un socio aqui...

    print("\n[ (✓) ] --> El socio ha sido ingresado con éxito.\n")


def menu_alta_medico():
    nombre = None
    apellido = None
    cedula = None
    fecha_nacimiento = None
    fecha_ingreso = None
    celular = None
    especialidad = None

    print()
    while True:
        try:
            nombre = input("    - Ingrese el nombre: ")
            if nombre.isalpha(): break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es un nombre válido, ingréselo de nuevo.\n")

    while True:
        try:
            apellido = input("    - Ingrese el apellido: ")
            if apellido.isalpha(): break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es un apellido válido, ingréselo de nuevo.\n")

    while True:
        try:
            cedula = int(input("    - Ingrese la cédula de identidad: "))
            if len(str(cedula)) == 8: break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.\n")

    while True:
        try:
            fecha_nacimiento = input("    - Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            break
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.\n")

    while True:
        try:
            fecha_ingreso = input("    - Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
            fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
            break
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.\n")

    while True:
        try:
            celular = input("    - Ingrese el número de celular: ")
            if not celular.isnumeric(): raise ValueError

            if celular[0] == '0' and celular[1] == '9' and len(celular[2:]) == 7: break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.\n")

    while True:
        try:
            especialidad = input("    - Ingrese la especialidad: ")
            if especialidad.isalpha():

                # Chequeamos si la especialidad existe
                # Si no ...

                if especialidad.upper() != "Cirugia".upper():
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

                    if opcion == 2: menu_alta_especialidad()
                    else: pass
                else:
                    break

            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] -->  La especialidad debe ser un string.\n")
            


    # <-- Funcion dar de alta un médico aqui...

    print("\n[ (✓) ] --> El médico ha sido ingresado con éxito.\n")




def menu_alta_consulta():
    especialidad = None
    medico = None
    fecha_consulta = None
    pacientes = None

    print()
    while True:
        try:
            especialidad = input("    - Ingrese la especialidad: ")
            if especialidad.isalpha():

                # Chequeamos si la especialidad existe
                # Si no ...

                if especialidad.upper() != "Cirugia".upper():
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

                    if opcion == 2: menu_alta_especialidad()
                    else: pass
                else:
                    break

            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] -->  La especialidad debe ser un string.\n")

    while True:
        try:
            nombre = input("    - Ingrese el nombre del médico: ")
            if nombre.isalpha():
                
                # Chequeamos si el medico existe
                # Si no ...

                if especialidad.upper() != "Cirugia".upper():
                    print("\n    Este médico no está dado de alta, elija una opción:\n")
                    print("        1. Volver a ingresar el médico.")
                    print("        2. - Dar de alta el médico.\n")

                    while True:
                        try:
                            opcion = int(input("    --> Opción: "))
                            if  1 <= opcion <= 2: break
                            else: raise ValueError
                        except ValueError:
                            print("\n[ (!) ERROR ] --> La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")

                    if opcion == 2: menu_alta_medico()
                    else: pass
                else:
                    break
            else: raise ValueError
        except ValueError:
            print("\n[ (!) ERROR ] --> No es un nombre válido, ingréselo de nuevo.\n")

    while True:
        try:
            fecha_consulta = input("    - Ingrese la fecha de consulta: ")
            fecha_consulta = datetime.strptime(fecha_consulta, "%Y-%m-%d")
            break
        except ValueError:
            print("\n[ (!) ERROR ] --> No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.\n")

    while True:
        try:
            pacientes = int(input("    - Ingrese la cantidad de pacientes que se atenderán: "))
            break
        except ValueError:
            print("\n[ (!) ERROR ] --> La cantidad de pacientes no es válida, ingrésela nuevamente.\n")
            


    # <-- Funcion dar de alta una consulta aqui...

    print("\n[ (✓) ] --> La consulta ha sido ingresado con éxito.\n")


if __name__ == "__main__":
    menu_principal()
