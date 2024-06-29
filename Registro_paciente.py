def main():
    while True:
        print("\n==============================================")
        print("          REGISTRO DE UN NUEVO PACIENTE       ")
        print("==============================================")

        nombre = input("Ingrese el nombre del paciente o escriba C para terminar el proceso: ")
        if nombre.lower() == 'c':
            print("Registro cancelado")
            return
        elif not nombre:
            print("El campo no puede estar vacío")
            continue

        apellido_paterno = input("Ingrese el apellido paterno del paciente: ")
        if apellido_paterno.lower() == 'c':
            print("Registro cancelado")
            return
        elif not apellido_paterno:
            print("El campo no puede estar vacío")
            continue

        apellido_materno = input("Ingrese el apellido materno del paciente: ")
        if apellido_materno.lower() == 'c':
            print("Registro cancelado")
            return
        elif not apellido_materno:
            print("El campo no puede estar vacío")
            continue

        try:
            edad = int(input("Ingrese la edad del paciente (entre 1 y 100 años): "))
            if edad < 1 or edad > 100:
                print("La edad debe estar en el rango de 1 a 100 años")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido")
            continue

        while True:
            sexo = input("Ingrese el sexo del paciente (masculino, femenino, otro): ").lower()
            if sexo == 'c':
                print("Registro cancelado")
                return
            elif not sexo:
                print("El campo no puede estar vacío")
                continue
            if sexo in ["masculino", "femenino", "otro"]:
                break

        telefono = input("Ingrese el telefono del paciente: ")
        if telefono.lower() == 'c':
            print("Registro cancelado")
            return
        elif not telefono:
            print("El campo no puede estar vacío")
            continue

        distrito = input("Ingrese el distrito del paciente: ")
        if distrito.lower() == 'c':
            print("Registro cancelado")
            return
        elif not distrito:
            print("El campo no puede estar vacío")
            continue

        dni = input("Ingrese el DNI del paciente: ")
        if dni.lower() == 'c':
            print("Registro cancelado")
            return
        elif not dni:
            print("El campo no puede estar vacío")
            continue

        print("\n==============================================")
        print("       El paciente ha sido registrado exitosamente:")
        print("==============================================")
        print(f"Nombre:           {nombre}")
        print(f"Apellido Paterno: {apellido_paterno}")
        print(f"Apellido Materno: {apellido_materno}")
        print(f"Edad:             {edad} años")
        print(f"Sexo:             {sexo}")
        print(f"Teléfono:         {telefono}")
        print(f"Distrito:         {distrito}")
        print(f"DNI:              {dni}")

        opcion = input("\n¿Desea registrar otro paciente? (S/N): ").lower()
        if opcion != 's':
            break

    print("Registro finalizado. ¡Hasta luego!")

if __name__ == "__main__":
    main()
