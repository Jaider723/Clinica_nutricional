class Persona:
    def __init__(self, nombre, edad, rut, sexo, peso, altura):
        self._nombre = nombre
        self._edad = edad
        self._rut = rut
        self._sexo = sexo
        self._peso = peso
        self._altura = altura

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_rut(self):
        return self._rut

    def get_sexo(self):
        return self._sexo

    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        self._peso = peso

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura

class Medico(Persona):
    def __init__(self, nombre, edad, rut, sexo, peso, altura, precio_consulta, especialidad):
        super().__init__(nombre, edad, rut, sexo, peso, altura)
        self._precio_consulta = precio_consulta
        self._especialidad = especialidad

    def get_precio_consulta(self):
        return self._precio_consulta

    def get_especialidad(self):
        return self._especialidad

class Paciente(Persona):
    def __init__(self, nombre, edad, rut, sexo, peso, altura, fecha_primera_consulta, medico_tratante):
        super().__init__(nombre, edad, rut, sexo, peso, altura)
        self._fecha_primera_consulta = fecha_primera_consulta
        self._medico_tratante = medico_tratante

    def calcular_IMC(self):
        imc = int(self.get_peso()) / ((int(self.get_altura())/100) ** 2)
        if imc < 18.5:
            return -1  
        elif 18.5 <= imc < 25:
            return 0   
        else:
            return 1   

    def es_mayor_de_edad(self):
        return int(self.get_edad()) >= 18

    def comprobar_sexo(self, sexo):
        if sexo.upper() == 'H' or sexo.upper() == 'M':
            return sexo.upper()
        else:
            return 'H'  