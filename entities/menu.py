def menu_principal(policlinica):
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
            case 1: policlinica.dar_alta_especialidad()
            case 2: policlinica.dar_alta_socio()
            case 3: policlinica.dar_alta_medico()
            case 4: policlinica.dar_alta_consulta()
            case 5: policlinica.emitir_ticket()
            case 6: policlinica.realizar_consulta()
            case 7: break
            case _: print("[ (!) ERROR ] --> Un error inesperado ha ocurrido.")
