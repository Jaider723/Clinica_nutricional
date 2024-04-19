from gestor import GestorPacientes
def main():
    archivo = GestorPacientes()
    archivo.cargar_pacientes()
    while True:
        print("\n--- MENU ---")
        print("1. Ingresar paciente")
        print("2. Editar paciente")
        print("3. Consultar estado de salud de paciente")
        print("0. Salir")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            archivo.ingresar_paciente()
        elif opcion == "2":
            archivo.editar_paciente()
        elif opcion == "3":
            archivo.consultar_estado_salud()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        
if __name__ == "__main__":
    main()