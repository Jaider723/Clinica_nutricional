import os
from clases import Paciente, Medico
pacientes = []

class GestorPacientes():
    def __init__(self):
        self.pacientes = "pacientes.txt"
    def cargar_pacientes(self):
        pacientes.clear()
        with open(self.pacientes, "r") as file:
            for linea in file:
                nombre, edad, rut, sexo, peso, altura, fecha_primera_consulta, medico_tratante = linea.strip().split(',')
                paciente = Paciente(nombre, edad, rut, sexo, peso, altura, fecha_primera_consulta, medico_tratante)
                pacientes.append(paciente)
    
    def ingresar_paciente(self):
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        rut = input("Ingrese el rut del paciente: ")
        sexo = input("Ingrese el sexo del paciente: ")
        peso = float(input("Ingrese el peso del paciente: "))
        altura = float(input("Ingrese la altura del paciente: "))
        fecha_primera_consulta = input("Ingrese la fecha de la primera consulta del paciente: ")
        medico_tratante = input("Ingrese el rut del médico tratante del paciente: ")
        paciente = Paciente(nombre, edad, rut, sexo, peso, altura, fecha_primera_consulta, medico_tratante)
        pacientes.append(paciente)
        with open(self.pacientes, "a") as file:
            file.write(f"{paciente.get_nombre()},{paciente.get_edad()},{paciente.get_rut()},{paciente.get_sexo()},{paciente.get_peso()},{paciente.get_altura()},{paciente._fecha_primera_consulta},{paciente._medico_tratante}\n")
        print("Paciente ingresado exitosamente.")
        
    def editar_paciente(self):
        rut_buscar = input("Ingrese el rut del paciente que desea editar: ")
        nueva_edad = input("Ingrese la nueva edad: ")
        nuevo_peso = input("Ingrese el nuevo peso: ")
        nueva_altura = input("Ingrese la nueva altura: ")
        pacientes_actualizados = []
        with open(self.pacientes, 'r') as archivo:
            for linea in archivo:
                nombre, edad, rut, sexo, peso, altura, fecha_primera_consulta, medico_tratante = linea.strip().split(',')
                if rut == rut_buscar:
                    edad = nueva_edad
                    peso = nuevo_peso
                    altura = nueva_altura
                pacientes_actualizados.append(f"{nombre},{edad},{rut},{sexo},{peso},{altura},{fecha_primera_consulta},{medico_tratante}\n")
        with open(self.pacientes, 'w') as archivo:
            archivo.writelines(pacientes_actualizados)
        self.cargar_pacientes()
        print("Paciente editado.")
        
    def consultar_estado_salud(self):
        rut_buscar = input("Ingrese el rut del paciente que desea consultar: ")
        for paciente in pacientes:
            if paciente.get_rut() == rut_buscar:
                print(f"Nombre: {paciente.get_nombre()}")
                print(f"Edad: {paciente.get_edad()}")
                print(f"Altura: {paciente.get_altura()}")
                imc = paciente.calcular_IMC()
                if imc == -1:
                    print("Bajo peso.")
                elif imc == 0:
                    print("Peso normal.")
                else:
                    print("Sobrepeso.")
                if paciente.es_mayor_de_edad():
                    print("Es mayor de edad.")
                else:
                    print("Es menor de edad.")
                return
        print("Paciente no encontrado.")
