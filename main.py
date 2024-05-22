# from entities.policlinica import Policlinica

def menu_principal():
    opcion = None

    print("\nSeleccione una opcion del menu:\n")
    print("     1. Dar de alta una especialidad.")
    print("     2. Dar de alta un socio.")
    print("     3. Dar de alta un medico.")
    print("     4. Dar de alta una consulta medica.")
    print("     5. Emitir un ticket de consulta.")
    print("     6. Realizar consultas.")
    print("     7. Salir del programa.\n")
    
    while True:
        try:
            opcion = int(input("--> Opcion: "))
            if  1 <= opcion <= 7: break
            else: raise ValueError
        except ValueError:
            print("\n[ /!\ ERROR ] --> La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")

    match opcion:
        case 1:
            menu_especialidad()


def menu_especialidad():
    especialidad = None
    precio = None

    print()
    while True:
        try:
            especialidad = input("  - Ingrese el nombre de la especialidad: ")
            if especialidad.isalpha(): break
            else: raise ValueError
        except ValueError:
            print("\n[ /!\ ERROR ] --> El nombre de la especialidad es incorrecto, ingréselo nuevamente.\n")

    while True:
        try:
            precio = int(input("    - Ingrese el precio asociado: $"))
            break
        except ValueError:
            print("\n[ /!\ ERROR ] --> El precio de la especialidad es incorrecto, ingréselo nuevamente.\n")

    

if __name__ == "__main__":
    menu_principal()
